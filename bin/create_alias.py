#!/usr/bin/env python3
"""
Create aliases from GOLL entries.

This script reads a GOLL JSON entry file and displays key information,
then helps the user create a shell alias for the command.
"""

import json
import os
import sys
import subprocess
from pathlib import Path


def load_goll_entry(filepath):
    """Load and parse a GOLL JSON entry file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading GOLL entry: {e}")
        sys.exit(1)


def detect_shell():
    """Detect the user's shell and return shell type and config file path."""
    shell_path = os.environ.get("SHELL", "")
    shell = os.path.basename(shell_path)
    
    home = Path.home()
    
    # Map shells to their config files
    shell_configs = {
        "bash": home / ".bashrc",
        "zsh": home / ".zshrc",
        "fish": home / ".config" / "fish" / "config.fish",
        "ksh": home / ".kshrc",
        "dash": home / ".bashrc",  # dash typically uses .bashrc
        "ash": home / ".bashrc",   # ash typically uses .bashrc
        "yash": home / ".yashrc",
        "mksh": home / ".mkshrc",
    }
    
    # Default to bash if shell not recognized
    if shell not in shell_configs:
        shell = "bash"
    
    config_file = shell_configs[shell]
    
    # Ensure fish config directory exists
    if shell == "fish":
        config_file.parent.mkdir(parents=True, exist_ok=True)
    
    return shell, config_file


def create_alias_in_config(config_file, alias_name, command, shell):
    """Add alias to the appropriate shell config file."""
    try:
        # Prepare alias line based on shell
        if shell == "fish":
            alias_line = f"alias {alias_name} \"{command}\""
        else:
            # Escape any existing double quotes in command
            escaped_command = command.replace('"', '\\"')
            alias_line = f"alias {alias_name}=\"{escaped_command}\""
        
        # Add alias with comment for identification
        alias_with_comment = f"\n# GOLL alias - added on {os.popen('date').read().strip()}\n{alias_line}\n"
        
        # Append to config file
        with open(config_file, "a", encoding="utf-8") as f:
            f.write(alias_with_comment)
        
        return True
    except Exception as e:
        print(f"Error writing to config file: {e}")
        return False


def source_config_file(config_file, shell):
    """Source the config file to activate the alias in current session."""
    try:
        # We can't directly source from Python to affect the parent shell,
        # but we can show the command the user needs to run
        print(f"\nTo activate the alias in your current session, run:")
        print(f"  source {config_file}")
        print("Or open a new terminal session.")
        return True
    except Exception as e:
        print(f"Note: {e}")
        return False


def print_colored_goll_info(entry_id, description, command):
    """Print GOLL entry information with colors and better formatting."""
    # ANSI color codes
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    print(f"{BOLD}{BLUE}{'=' * 60}{END}")
    print(f"{BOLD}{GREEN}ID:{END} {entry_id}")
    print(f"{BOLD}{YELLOW}Description:{END} {description}")
    print(f"{BOLD}{RED}Command:{END} {command}")
    print(f"{BOLD}{BLUE}{'=' * 60}{END}")


def main():
    """Main function to process GOLL entry and create alias."""
    if len(sys.argv) != 2:
        print("Usage: python3 create_alias.py <path_to_goll_entry.json>")
        sys.exit(1)
    
    # Load the GOLL entry
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    entry = load_goll_entry(filepath)
    
    # Extract key information
    entry_id = entry.get("id", "unknown")
    description = entry.get("description", "No description available")
    command = entry.get("command", "")
    
    # Display information with colors
    print_colored_goll_info(entry_id, description, command)
    
    # Ask user if they want to create an alias
    response = input("\nDo you want to create an alias for this command? (y/N): ").strip().lower()
    
    if response not in ['y', 'yes']:
        print("No alias created.")
        return
    
    # Ask for alias name, defaulting to entry ID
    alias_name = input(f"Enter alias name (default: {entry_id}): ").strip()
    if not alias_name:
        alias_name = entry_id
    
    # Detect shell and config file
    shell, config_file = detect_shell()
    print(f"\nDetected shell: {shell}")
    print(f"Config file: {config_file}")
    
    # Create alias in config file
    if create_alias_in_config(config_file, alias_name, command, shell):
        print(f"\nAlias '{alias_name}' created successfully in {config_file}")
        print("To activate the alias in your current session, run:")
        print(f"  source {config_file}")
        print("Or open a new terminal session.")
    else:
        print("Failed to create alias.")
        sys.exit(1)


if __name__ == "__main__":
    main()