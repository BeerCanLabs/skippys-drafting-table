#!/usr/bin/env python3
"""
Migrate Shared Services in DRAFT Catalog to explicit provisioningModel choices.

Sets `provisioningModel: reference-only` (or `deployable` with `--deployable`) for
all `host`, `runtime_service`, `data_store_service`, `network_service`, and `ai_gateway` objects.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import yaml

SHARED_SERVICE_TYPES = {
    "host",
    "runtime_service",
    "data_store_service",
    "network_service",
    "ai_gateway",
}


def migrate_catalog(workspace_root: Path, set_deployable: bool = False, dry_run: bool = False) -> int:
    catalog_dir = workspace_root / "catalog"
    if not catalog_dir.exists():
        catalog_dir = workspace_root / "examples" / "catalog"

    if not catalog_dir.exists():
        print(f"Error: Catalog directory not found in {workspace_root}", file=sys.stderr)
        return 1

    updated_count = 0
    yaml_files = sorted(catalog_dir.rglob("*.yaml")) + sorted(catalog_dir.rglob("*.yml"))

    for filepath in yaml_files:
        try:
            content = filepath.read_text(encoding="utf-8")
            data = yaml.safe_load(content)
            if not isinstance(data, dict):
                continue
            obj_type = data.get("type")
            if obj_type in SHARED_SERVICE_TYPES:
                if "provisioningModel" not in data:
                    if set_deployable:
                        data["provisioningModel"] = "deployable"
                        if "deployablePackage" not in data:
                            data["deployablePackage"] = {
                                "registry": "github",
                                "source": f"company-infrastructure/terraform-{data.get('uid', 'module')}",
                                "version": "v1.0.0",
                            }
                    else:
                        data["provisioningModel"] = "reference-only"

                    if not dry_run:
                        with open(filepath, "w", encoding="utf-8") as f:
                            yaml.dump(data, f, sort_keys=False, default_flow_style=False)
                    print(f"[{'DRY-RUN ' if dry_run else ''}MIGRATED] {filepath.relative_to(workspace_root)} -> provisioningModel: {data['provisioningModel']}")
                    updated_count += 1
        except Exception as exc:
            print(f"Error processing {filepath}: {exc}", file=sys.stderr)

    print(f"\nMigration complete. Updated {updated_count} shared service objects.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate DRAFT catalog shared services to explicit provisioningModel.")
    parser.add_argument("--workspace", type=str, default=".", help="Path to DRAFT workspace directory (default: .)")
    parser.add_argument("--deployable", action="store_true", help="Set provisioningModel to 'deployable' with stub deployablePackage instead of 'reference-only'")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without modifying files on disk")

    args = parser.parse_args()
    workspace_root = Path(args.workspace).resolve()
    sys.exit(migrate_catalog(workspace_root, set_deployable=args.deployable, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
