#!/usr/bin/env python3
"""
Agent Package Validator: Verifies agent specifications, manifest consistency, skills, and MCP server execution.

Usage:
    python3 framework/tools/validate_agent_package.py
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

TOOLS_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_ROOT.parent.parent
AGENT_ROOT = REPO_ROOT / "agent"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate DRAFT framework agent package manifests, skills, and MCP server handshakes.")
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


def test_mcp_server_handshake(mcp_file: Path) -> list[str]:
    failures: list[str] = []
    try:
        data = json.loads(mcp_file.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"{mcp_file}: Invalid JSON: {exc}")
        return failures

    servers = data.get("mcpServers", {})
    if not isinstance(servers, dict) or not servers:
        failures.append(f"{mcp_file}: Must declare non-empty mcpServers mapping")
        return failures

    for server_name, config in servers.items():
        cmd = config.get("command")
        args = config.get("args", [])
        if not cmd:
            failures.append(f"{mcp_file}: Server '{server_name}' missing command")
            continue

        full_cmd = [cmd] + args
        try:
            proc = subprocess.Popen(
                full_cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(REPO_ROOT),
                text=True,
            )
        except Exception as exc:
            failures.append(f"{mcp_file}: Failed to launch MCP server '{server_name}' ({full_cmd}): {exc}")
            continue

        # Send initialize and tools/list requests
        init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}) + "\n"
        list_req = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}) + "\n"

        try:
            stdout_data, stderr_data = proc.communicate(input=init_req + list_req, timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            failures.append(f"{mcp_file}: MCP server '{server_name}' timed out on JSON-RPC handshake")
            continue

        lines = [line.strip() for line in stdout_data.splitlines() if line.strip()]
        tools_found = False

        for line in lines:
            try:
                msg = json.loads(line)
                if msg.get("id") == 2 and "result" in msg:
                    tools = msg["result"].get("tools", [])
                    if isinstance(tools, list) and len(tools) > 0:
                        tools_found = True
            except Exception:
                pass

        if not tools_found:
            failures.append(f"{mcp_file}: MCP server '{server_name}' failed handshake: did not return a non-empty tool list over stdio (output: {lines})")

    return failures


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

    # 2. Validate MCP paths exist and execute stdio handshake
    spec_mcps = spec_data.get("mcps") or []
    if not isinstance(spec_mcps, list):
        failures.append(f"{spec_path}: mcps must be a list")
    else:
        for mcp_path_str in spec_mcps:
            mcp_path = REPO_ROOT / str(mcp_path_str)
            if not mcp_path.exists():
                failures.append(f"{spec_path}: Referenced MCP file '{mcp_path_str}' does not exist")
            else:
                mcp_failures = test_mcp_server_handshake(mcp_path)
                failures.extend(mcp_failures)

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
