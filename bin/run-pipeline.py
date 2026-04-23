#!/usr/bin/env python3
"""
Pipeline coordinator for building the oneliner library documentation.
Executes validation, conversion, and consolidation scripts in sequence.
"""

import subprocess
import sys
from pathlib import Path


def run_pipeline():
    repo_root = Path(__file__).parent.parent

    # List of scripts to run in order
    pipeline = [
        repo_root / "bin" / "validate-entries.py",
        repo_root / "bin" / "json_to_latex.py",
        repo_root / "bin" / "convert_latex.py",
        repo_root / "bin" / "consolidate_latex.py",
    ]

    for script_path in pipeline:
        print(f"==> Executing: {script_path.name}")

        try:
            # Execute the script
            result = subprocess.run(
                [sys.executable, str(script_path)],
                check=True,
                capture_output=True,
                text=True,
            )
            # Print script output for visibility
            if result.stdout:
                print(result.stdout)
            print(f"==> Completed: {script_path.name}")

        except subprocess.CalledProcessError as e:
            # Standardized error reporting
            print(f"\n[ERROR] Pipeline failed at step: {script_path.name}")
            print(f"Exit code: {e.returncode}")
            if e.stderr:
                print(f"Error output:\n{e.stderr}")
            elif e.stdout:
                print(f"Script output:\n{e.stdout}")
            sys.exit(1)

    print("\n[SUCCESS] All pipeline steps completed successfully.")


if __name__ == "__main__":
    run_pipeline()
