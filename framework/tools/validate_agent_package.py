#!/usr/bin/env python3
"""
Agent Package Validator: Verifies agent specifications, manifest consistency, skills, and MCP paths.

Usage:
    python3 framework/tools/validate_agent_package.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

TOOLS_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_ROOT.parent.parent
AGENT_ROOT = REPO_ROOT / "agent"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate DRAFT framework agent package manifests and skills.")
    parser.add_argument(
        "--agent-dir",
        type=Path,
        default=AGENT_ROOT,
        help="Path to agent package directory.",
    )
    return parser.parse_args(argv)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"File '{path}' does not exist.")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"File '{path}' must be a YAML mapping.")
    return data


def validate_agent_package(agent_dir: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []

    spec_path = agent_dir / "agent-spec.yaml"
    hermes_path = agent_dir / "bindings" / "hermes" / "agent.yaml"
    skills_dir = agent_dir / "skills"

    if not spec_path.exists():
        failures.append(f"{spec_path}: Missing agent-spec.yaml")
        return failures, warnings

    try:
        spec_data = load_yaml(spec_path)
    except Exception as exc:
        failures.append(f"{spec_path}: {exc}")
        return failures, warnings

    # 1. Validate skills exist
    spec_skills = spec_data.get("skills") or []
    if not isinstance(spec_skills, list):
        failures.append(f"{spec_path}: skills must be a list")
    else:
        for skill in spec_skills:
            skill_path = skills_dir / str(skill)
            if not skill_path.exists() or not skill_path.is_dir():
                failures.append(f"{spec_path}: Declared skill '{skill}' does not exist as a directory in agent/skills/")

    # 2. Validate MCP paths exist
    spec_mcps = spec_data.get("mcps") or []
    if not isinstance(spec_mcps, list):
        failures.append(f"{spec_path}: mcps must be a list")
    else:
        for mcp_path_str in spec_mcps:
            mcp_path = REPO_ROOT / str(mcp_path_str)
            if not mcp_path.exists():
                failures.append(f"{spec_path}: Referenced MCP file '{mcp_path_str}' does not exist")

    # 3. Validate Hermes binding consistency
    if hermes_path.exists():
        try:
            hermes_data = load_yaml(hermes_path)
            hermes_skills = hermes_data.get("skills") or []
            if spec_skills != hermes_skills:
                failures.append(f"{hermes_path}: skills list does not match agent-spec.yaml ({hermes_skills} != {spec_skills})")
            
            hermes_mcps = hermes_data.get("mcps") or []
            if spec_mcps != hermes_mcps:
                failures.append(f"{hermes_path}: mcps list does not match agent-spec.yaml ({hermes_mcps} != {spec_mcps})")

            hermes_channels = hermes_data.get("channels") or {}
            spec_channels = spec_data.get("channels") or {}
            if spec_channels != hermes_channels:
                warnings.append(f"{hermes_path}: channels declaration differs from agent-spec.yaml")

        except Exception as exc:
            failures.append(f"{hermes_path}: {exc}")

    return failures, warnings


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    failures, warnings = validate_agent_package(args.agent_dir)

    for warning in warnings:
        print(f"WARNING: {warning}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        print(f"\nAgent package validation failed with {len(failures)} error(s).", file=sys.stderr)
        return 1

    print("PASS: Agent package validation successful.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
