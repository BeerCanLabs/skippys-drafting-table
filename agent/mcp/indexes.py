#!/usr/bin/env python3
"""
Standalone Index Loader & Query Helpers for Draftsman Agent MCP Server.
Self-contained within agent/mcp/ directory.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path
from typing import Any

MCP_DIR = Path(__file__).resolve().parent
AGENT_ROOT = MCP_DIR.parent


def load_catalog_index() -> dict[str, Any]:
    url = os.getenv("DRAFT_CATALOG_INDEX_URL")
    path_str = os.getenv("DRAFT_CATALOG_INDEX_PATH")
    read_token = os.getenv("GITHUB_READ_TOKEN") or os.getenv("GITHUB_TOKEN")

    if url:
        try:
            req = urllib.request.Request(url)
            if read_token and ("github" in url.lower() or "githubusercontent" in url.lower()):
                req.add_header("Authorization", f"Bearer {read_token}")
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    if isinstance(data, dict):
                        return data
        except Exception as exc:
            sys.stderr.write(f"Warning: Failed to fetch index from DRAFT_CATALOG_INDEX_URL ({url}): {exc}\n")

    if path_str:
        file_path = Path(path_str)
        if file_path.exists():
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    return data
            except Exception as exc:
                sys.stderr.write(f"Warning: Failed to read index from DRAFT_CATALOG_INDEX_PATH ({file_path}): {exc}\n")

    for fallback in [
        Path("catalog_indexes.json"),
        Path("docs/catalog_indexes.json"),
        AGENT_ROOT.parent / "catalog_indexes.json",
        AGENT_ROOT.parent / "docs" / "catalog_indexes.json",
    ]:
        if fallback.exists():
            try:
                data = json.loads(fallback.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    return data
            except Exception:
                pass

    return {
        "version": "1.0.3",
        "objects": [],
        "generatedAt": "2026-08-26T00:00:00Z"
    }
