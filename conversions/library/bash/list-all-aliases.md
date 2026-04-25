# List all shell aliases in a colored, formatted display {#list-all-shell-aliases-in-a-colored-formatted-display .unnumbered}

**Author:** marcos **Date:** 2026-04-25

Lists all aliases defined in the user's shell configuration file in
alphabetical order with colored, formatted output. Works with bash, zsh,
and other shells on Linux and BSD systems.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

shell-utilities

# Command {#command .unnumbered}

    bash -c 'shell_conf="${1:-$HOME/.bashrc}"; [ -f "$shell_conf" ] || { echo "Configuration file not found: $shell_conf"; exit 1; }; grep -E "^[[:space:]]*alias[[:space:]]" "$shell_conf" | sed -E "s/^[[:space:]]*alias[[:space:]]*//" | sort -f | while IFS= read -r line; do alias_name=${line%%=*}; alias_cmd=${line#*=}; printf "\\033[1;34m%-20s\\033[0m -> \\033[1;32m%s\\033[0m\\n" "$alias_name" "$alias_cmd"; done' _

# Explanation {#explanation .unnumbered}

This command reads the user's shell configuration file from the path
passed as the first argument (defaulting to \~/.bashrc), extracts alias
definitions, sorts them alphabetically by alias name, and prints the
alias name in blue and the stored alias command in green. It preserves
the command text as written after the equals sign, which keeps the
direct shell syntax intact and avoids fragile quote-stripping logic.

# Tags {#tags .unnumbered}

shell, alias, utilities, configuration, listing

# Dependencies {#dependencies .unnumbered}

bash, grep, sed, sort

# Arguments {#arguments .unnumbered}

1.  **CONFIG_FILE** (Optional): Path to shell configuration file
    (optional, defaults to \~/.bashrc)\
    Default: \~/.bashrc

# Examples {#examples .unnumbered}

1.  `bash -c ’shell_conf="${1:-$HOME/.bashrc}"; [ -f "$shell_conf" ] || { echo "Configuration file not found: $shell_conf"; exit 1; }; grep -E "^[[:space:]]*alias[[:space:]]" "$shell_conf" | sed -E "s/^[[:space:]]*alias[[:space:]]*//" | sort -f | while IFS= read -r line; do alias_name=${line%%=*}; alias_cmd=${line#*=}; printf "\{}\{}033[1;34m%-20s\{}\{}033[0m -> \{}\{}033[1;32m%s\{}\{}033[0m\{}\{}n" "$alias_name" "$alias_cmd"; done’ _` -
    List all aliases from the default shell configuration file in
    alphabetical order

2.  `bash -c ’shell_conf="${1:-$HOME/.bashrc}"; [ -f "$shell_conf" ] || { echo "Configuration file not found: $shell_conf"; exit 1; }; grep -E "^[[:space:]]*alias[[:space:]]" "$shell_conf" | sed -E "s/^[[:space:]]*alias[[:space:]]*//" | sort -f | while IFS= read -r line; do alias_name=${line%%=*}; alias_cmd=${line#*=}; printf "\{}\{}033[1;34m%-20s\{}\{}033[0m -> \{}\{}033[1;32m%s\{}\{}033[0m\{}\{}n" "$alias_name" "$alias_cmd"; done’ _ ~/.zshrc` -
    List all aliases from a zsh configuration file in alphabetical order

3.  `alias list-aliases=’bash -c ’"’"’shell_conf="${1:-$HOME/.bashrc}"; [ -f "$shell_conf" ] || { echo "Configuration file not found: $shell_conf"; exit 1; }; grep -E "^[[:space:]]*alias[[:space:]]" "$shell_conf" | sed -E "s/^[[:space:]]*alias[[:space:]]*//" | sort -f | while IFS= read -r line; do alias_name=${line%%=*}; alias_cmd=${line#*=}; printf "\{}\{}033[1;34m%-20s\{}\{}033[0m -> \{}\{}033[1;32m%s\{}\{}033[0m\{}\{}n" "$alias_name" "$alias_cmd"; done’"’"’ _’` -
    Create a permanent alias for listing all aliases in alphabetical
    order

# Output {#output .unnumbered}

    \033[1;34mdocker-rm-stopped   \033[0m -> \033[1;32m'docker rm $(docker ps -aq --filter status=exited)'\033[0m
    \033[1;34mgs                  \033[0m -> \033[1;32m"git status"\033[0m
    \033[1;34mll                  \033[0m -> \033[1;32m'ls -la'\033[0m
    \033[1;34mup                  \033[0m -> \033[1;32m'uptime'\033[0m

# Notes {#notes .unnumbered}

-   The command works with bash, zsh, and other shells by specifying the
    appropriate configuration file

-   Color codes: alias names are displayed in blue, commands in green

-   Alias names are listed in alphabetical order

-   The command text is shown exactly as stored after the equals sign

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
