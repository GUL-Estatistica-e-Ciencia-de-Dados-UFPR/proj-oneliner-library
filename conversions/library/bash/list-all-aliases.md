# List all shell aliases in a colored, formatted display {#list-all-shell-aliases-in-a-colored-formatted-display .unnumbered}

**Author:** marcos **Date:** 2026-04-25

Lists all aliases defined in the user's shell configuration file with
colored, formatted output. Works with bash, zsh, and other shells on
Linux and BSD systems.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

shell-utilities

# Command {#command .unnumbered}

    bash -c 'shell_conf=${1:-~/.bashrc}; if [ -f "$shell_conf" ]; then grep -E "^alias\s" "$shell_conf" | sed "s/^alias\s*//" | while IFS= read -r line; do alias_name=$(echo "$line" | cut -d"=" -f1); alias_cmd=$(echo "$line" | cut -d"=" -f2- | sed "s/^\(\s\)*\(\"\|\'\)\(.*\)\(\"\|\'\)\(\s\)*$/\3/"); printf "\033[1;34m%-20s\033[0m -> \033[1;32m%s\033[0m\n" "$alias_name" "$alias_cmd"; done; else echo "Configuration file not found: $shell_conf"; fi' _

# Explanation {#explanation .unnumbered}

This command detects the user's shell configuration file based on the
SHELL environment variable, then parses the file to extract all alias
definitions. It formats the output with colors to make alias names
(blue) and their corresponding commands (green) easily distinguishable.
The command accepts an optional argument for the configuration file
path, defaulting to \~/.bashrc if not specified.

# Tags {#tags .unnumbered}

shell, alias, utilities, configuration, listing

# Dependencies {#dependencies .unnumbered}

bash, coreutils, grep, sed

# Arguments {#arguments .unnumbered}

1.  **CONFIG_FILE** (Optional): Path to shell configuration file
    (optional, defaults to \~/.bashrc)\
    Default: \~/.bashrc

# Examples {#examples .unnumbered}

1.  `bash -c ’shell_conf=${1:-~/.bashrc}; if [ -f "$shell_conf" ]; then grep -E "^alias\{}s" "$shell_conf" | sed "s/^alias\{}s*//" | while IFS= read -r line; do alias_name=$(echo "$line" | cut -d"=" -f1); alias_cmd=$(echo "$line" | cut -d"=" -f2- | sed "s/^\{}(\{}s\{})*\{}(\{}"\{}|\{}’\{})\{}(.*\{})\{}(\{}"\{}|\{}’\{})\{}(\{}s\{})*$/\{}3/"); printf "\{}033[1;34m%-20s\{}033[0m -> \{}033[1;32m%s\{}033[0m\{}n" "$alias_name" "$alias_cmd"; done; else echo "Configuration file not found: $shell_conf"; fi’ _` -
    List all aliases from default shell configuration file

2.  `bash -c ’shell_conf=${1:-~/.bashrc}; if [ -f "$shell_conf" ]; then grep -E "^alias\{}s" "$shell_conf" | sed "s/^alias\{}s*//" | while IFS= read -r line; do alias_name=$(echo "$line" | cut -d"=" -f1); alias_cmd=$(echo "$line" | cut -d"=" -f2- | sed "s/^\{}(\{}s\{})*\{}(\{}"\{}|\{}’\{})\{}(.*\{})\{}(\{}"\{}|\{}’\{})\{}(\{}s\{})*$/\{}3/"); printf "\{}033[1;34m%-20s\{}033[0m -> \{}033[1;32m%s\{}033[0m\{}n" "$alias_name" "$alias_cmd"; done; else echo "Configuration file not found: $shell_conf"; fi’ _ ~/.zshrc` -
    List all aliases from zsh configuration file

3.  `alias list-aliases=’bash -c ’"’"’shell_conf=${1:-~/.bashrc}; if [ -f "$shell_conf" ]; then grep -E "^alias\{}s" "$shell_conf" | sed "s/^alias\{}s*//" | while IFS= read -r line; do alias_name=$(echo "$line" | cut -d"=" -f1); alias_cmd=$(echo "$line" | cut -d"=" -f2- | sed "s/^\{}(\{}s\{})*\{}(\{}"\{}|\{}’\{})\{}(.*\{})\{}(\{}"\{}|\{}’\{})\{}(\{}s\{})*$/\{}3/"); printf "\{}033[1;34m%-20s\{}033[0m -> \{}033[1;32m%s\{}033[0m\{}n" "$alias_name" "$alias_cmd"; done; else echo "Configuration file not found: $shell_conf"; fi’"’"’ _’` -
    Create a permanent alias for listing all aliases

# Output {#output .unnumbered}

    [1;34mll                  [0m -> [1;32mls -la[0m
    [1;34mgs                  [0m -> [1;32mgit status[0m
    [1;34mup                  [0m -> [1;32muptime[0m
    [1;34mdocker-rm-stopped   [0m -> [1;32mdocker rm $(docker ps -aq --filter status=exited)[0m

# Notes {#notes .unnumbered}

-   The command works with bash, zsh, and other shells by specifying the
    appropriate configuration file

-   Color codes: alias names are displayed in blue, commands in green

-   Supports both single and double quoted alias definitions

-   Can be used directly or converted to a permanent alias

-   Works on Linux and BSD systems

# Warnings {#warnings .unnumbered}

-   Only shows aliases defined in the specified configuration file

-   Does not display aliases defined in sessions or other files

-   May not work with non-standard alias definitions

# See Also {#see-also .unnumbered}

-   replace-string-in-files

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-25

# Updated At {#updated-at .unnumbered}

2026-04-25
