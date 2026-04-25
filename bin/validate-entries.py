#!/usr/bin/env python3
"""
Validate all JSON entries in the library against the GOLL schema.
"""

import json
import os
import sys
import traceback
from collections import defaultdict

try:
    import jsonschema
except ImportError:
    print(
        "Error: jsonschema package is required. Install it with: pip install jsonschema"
    )
    sys.exit(1)


def load_schema(schema_path):
    """Load the JSON schema from the given path."""
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_json_file(filepath, schema):
    """Validate a single JSON file against the schema."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}", None
    except Exception as e:
        return False, f"Error reading file: {e}", None

    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, "Valid", data
    except jsonschema.ValidationError as e:
        return False, f"Validation error: {e.message}", None
    except jsonschema.SchemaError as e:
        return False, f"Schema error: {e}", None
    except Exception as e:
        return False, f"Unexpected error during validation: {e}", None


def write_status_entries(status_dict, filename, status_name):
    """Write entries with specific status to a markdown file."""
    filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "library", filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        if status_dict:
            f.write(f"# {status_name.capitalize()} Entries\n\n")
            f.write("| Entry ID | File Path |\n")
            f.write("|----------|-----------|\n")
            for path, entry_id in status_dict:
                f.write(f"| {entry_id} | {path} |\n")
        else:
            f.write(f'No entries with "{status_name}" status found in the library\n')
    
    print(f"{status_name.capitalize()} entries list written to {filename}")


def main():
    """Main validation function."""
    # Get the repository root (parent of bin directory)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(repo_root, "schema", "goll.schema.json")
    library_path = os.path.join(repo_root, "library")

    # Check if schema exists
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        sys.exit(1)

    # Check if library directory exists
    if not os.path.exists(library_path):
        print(f"Error: Library directory not found at {library_path}")
        sys.exit(1)

    # Load the schema
    try:
        schema = load_schema(schema_path)
    except Exception as e:
        print(f"Error loading schema: {e}")
        sys.exit(1)

    # Walk through the library directory
    validation_errors = []
    total_files = 0
    valid_files = 0
    draft_entries = []
    deprecated_entries = []

    for root, dirs, files in os.walk(library_path):
        for file in files:
            if file.lower().endswith(".json"):
                total_files += 1
                filepath = os.path.join(root, file)
                is_valid, message, data = validate_json_file(filepath, schema)
                if is_valid:
                    valid_files += 1
                    # Check for status field
                    if data and "status" in data:
                        if data["status"] == "draft":
                            # Get relative path from library directory
                            rel_path = os.path.relpath(filepath, library_path)
                            draft_entries.append((rel_path, data.get("id", "unknown")))
                        elif data["status"] == "deprecated":
                            # Get relative path from library directory
                            rel_path = os.path.relpath(filepath, library_path)
                            deprecated_entries.append((rel_path, data.get("id", "unknown")))
                else:
                    validation_errors.append((filepath, message))

    # Print summary
    print(f"Validation complete: {valid_files}/{total_files} files are valid.")

    # Write draft entries list
    write_status_entries(draft_entries, "draft_entries.md", "draft")
    
    # Write deprecated entries list
    write_status_entries(deprecated_entries, "deprecated_entries.md", "deprecated")

    if validation_errors:
        print("\nValidation errors:")
        for filepath, error in validation_errors:
            print(f"  ✗ {filepath}: {error}")
        sys.exit(1)
    else:
        print("All files are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
