# Comprehensive system/service non-human user report with disk quota, usage, and activity {#comprehensive-systemservice-non-human-user-report-with-disk-quota-usage-and-activity .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-21

Generates a comprehensive system audit report for all non-human
(system/service) users (requires sudo) showing username, disk quota
limit, home directory path, actual disk usage, account creation date,
file count, last login timestamp, and last executed command. All
information is formatted in a readable table with elevated privileges
for complete data access.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

system-administration

# Command {#command .unnumbered}

    sudo bash -c "printf 'USER\tQUOTA\tHOME\tDISK_USAGE\tCREATED\tFILES\tLAST_LOGIN\tLAST_CMD\n'; getent passwd | awk -F: '\$3 < 1000 || \$1 ~ /^nobody$/ { print \$1,\$6 }' | while read u h; do q=\$(quota -u \"\$u\" 2>/dev/null | tail -1 | awk '{print \$2}'); [ -z \"\$q\" ] && q=none; d=\$(du -sh \"\$h\" 2>/dev/null | cut -f1); c=\$(stat -c %y \"\$h\" 2>/dev/null | cut -d' ' -f1 || echo N/A); f=\$(find \"\$h\" -type f 2>/dev/null | wc -l); l=\$(lastlog -u \"\$u\" 2>/dev/null | tail -1 | awk '{print \$5,\$6,\$7}'); [ -z \"\$l\" ] && l=Never; cmd=\$(tail -1 \"\$h\"/.bash_history 2>/dev/null | head -c 30); [ -z \"\$cmd\" ] && cmd=N/A; printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \"\$u\" \"\$q\" \"\$h\" \"\$d\" \"\$c\" \"\$f\" \"\$l\" \"\$cmd\"; done" | column -t -s $'\t'

# Explanation {#explanation .unnumbered}

The command uses 'sudo bash -c' to execute the entire script with
elevated privileges, ensuring access to all user data. It retrieves
users with UID \< 1000 (or 'nobody') via getent, then for each user
gathers: disk quota from 'quota -u', home disk usage from 'du -sh',
account creation date via 'stat', file count using 'find', last login
from 'lslogins', and last command from .bash_history. The 'bash -c'
wrapper allows proper variable expansion and quoting within the sudo
context. Output is joined by tabs and formatted by 'column -t' for
readability, avoiding issues with spaces in values.

# Tags {#tags .unnumbered}

user-management, disk-usage, system-administration, activity, report,
quota, audit, system-users, service-accounts

# Dependencies {#dependencies .unnumbered}

coreutils, util-linux, shadow-utils, findutils

# Arguments {#arguments .unnumbered}

1.  **UID_THRESHOLD** (Optional): Maximum UID to consider a system user
    (default: 1000 for non-human users)\
    Default: 1000

# Examples {#examples .unnumbered}

1.  `sudo bash -c "printf ’USER\{}tQUOTA\{}tHOME\{}tDISK_USAGE\{}tCREATED\{}tFILES\{}tLAST_LOGIN\{}tLAST_CMD\{}n’; getent passwd | awk -F: ’\{}$3 < 1000 || \{}$1 ~ /^nobody$/ { print \{}$1,\{}$6 }’ | while read u h; do q=\{}$(quota -u \{}"\{}$u\{}" 2>/dev/null | tail -1 | awk ’{print \{}$2}’); [ -z \{}"\{}$q\{}" ] && q=none; d=\{}$(du -sh \{}"\{}$h\{}" 2>/dev/null | cut -f1); c=\{}$(stat -c %y \{}"\{}$h\{}" 2>/dev/null | cut -d’ ’ -f1 || echo N/A); f=\{}$(find \{}"\{}$h\{}" -type f 2>/dev/null | wc -l); l=\{}$(lastlog -u \{}"\{}$u\{}" 2>/dev/null | tail -1 | awk ’{print \{}$5,\{}$6,\{}$7}’); [ -z \{}"\{}$l\{}" ] && l=Never; cmd=\{}$(tail -1 \{}"\{}$h\{}"/.bash_history 2>/dev/null | head -c 30); [ -z \{}"\{}$cmd\{}" ] && cmd=N/A; printf ’%s\{}t%s\{}t%s\{}t%s\{}t%s\{}t%s\{}t%s\{}t%s\{}n’ \{}"\{}$u\{}" \{}"\{}$q\{}" \{}"\{}$h\{}" \{}"\{}$d\{}" \{}"\{}$c\{}" \{}"\{}$f\{}" \{}"\{}$l\{}" \{}"\{}$cmd\{}"; done" | column -t -s $’\{}t’` -
    Generate complete report for all non-human (system) users with all
    metrics (requires sudo)

2.  `sudo bash -c "printf ’USER\{}tQUOTA\{}tDISK_USAGE\{}tCREATED\{}tFILES\{}tLAST_LOGIN\{}n’; getent passwd | awk -F: ’\{}$3 < 1000 || \{}$1 ~ /^nobody$/ { print \{}$1,\{}$6 }’ | while read u h; do q=\{}$(quota -u \{}"\{}$u\{}" 2>/dev/null | tail -1 | awk ’{print \{}$2}’); [ -z \{}"\{}$q\{}" ] && q=none; d=\{}$(du -sh \{}"\{}$h\{}" 2>/dev/null | cut -f1); c=\{}$(stat -c %y \{}"\{}$h\{}" 2>/dev/null | cut -d’ ’ -f1 || echo N/A); f=\{}$(find \{}"\{}$h\{}" -type f 2>/dev/null | wc -l); l=\{}$(lastlog -u \{}"\{}$u\{}" 2>/dev/null | tail -1 | awk ’{print \{}$5,\{}$6,\{}$7}’); [ -z \{}"\{}$l\{}" ] && l=Never; printf ’%s\{}t%s\{}t%s\{}t%s\{}t%s\{}t%s\{}n’ \{}"\{}$u\{}" \{}"\{}$q\{}" \{}"\{}$d\{}" \{}"\{}$c\{}" \{}"\{}$f\{}" \{}"\{}$l\{}"; done | sort -t $’\{}t’ -k3 -hr" | column -t -s $’\{}t’` -
    Sort by disk usage descending, exclude home path and last command

3.  `sudo bash -c "printf ’USER\{}tQUOTA\{}tDISK_USAGE\{}tFILES\{}n’; getent passwd | awk -F: ’\{}$3 < 1000 || \{}$1 ~ /^nobody$/ { print \{}$1,\{}$6 }’ | while read u h; do q=\{}$(quota -u \{}"\{}$u\{}" 2>/dev/null | tail -1 | awk ’{print \{}$2}’); [ -z \{}"\{}$q\{}" ] && q=none; d=\{}$(du -sh \{}"\{}$h\{}" 2>/dev/null | cut -f1); f=\{}$(find \{}"\{}$h\{}" -type f 2>/dev/null | wc -l); printf ’%s\{}t%s\{}t%s\{}t%s\{}n’ \{}"\{}$u\{}" \{}"\{}$q\{}" \{}"\{}$d\{}" \{}"\{}$f\{}"; done" | column -t -s $’\{}t’` -
    Simplified report showing only quota, disk usage, and file count

# Output {#output .unnumbered}

    USER        QUOTA HOME            DISK_USAGE CREATED    FILES  LAST_LOGIN      LAST_CMD
    root        none  /root           1.5G       2023-01-15 15340  May  20 13:45   apt update
    daemon      none  /usr/sbin       32K        2023-01-15 12     Never           N/A
    bin         none  /bin            0          2023-01-15 0      Never           N/A
    www-data    none  /var/www        4.2G       2023-05-10 45678  Never           N/A
    nobody      none  /nonexistent    0          2023-01-15 0      Never           N/A

# Notes {#notes .unnumbered}

-   This command is designed to run with sudo for complete information;
    running without sudo will show incomplete results

-   The 'sudo bash -c' wrapper preserves the entire command context and
    allows proper variable expansion

-   Disk quota requires quota system to be enabled on the filesystem;
    shows 'none' if unavailable

-   File count calculation uses 'find' which can be slow on directories
    with millions of files

-   Account creation date uses home directory birth time (%w) if
    available, falling back to modification time (%y)

-   Last command is truncated to 30 characters; extracted from
    .bash_history. Note: Bash only flushes history to disk upon session
    exit or when 'history -a' is run, so this shows the last saved
    command, not necessarily the active session's most recent command.

-   Users with UIDs \>= 1000 are standard human accounts and are
    excluded by default. Note that system/service accounts typically
    lack valid login shells or history files, making LAST_CMD frequently
    N/A and LAST_LOGIN Never.

-   The command uses getent instead of /etc/passwd for better
    compatibility with different user databases (LDAP, NIS, etc.)

# Warnings {#warnings .unnumbered}

-   Requires sudo access to function properly; user must have sudo
    privileges without password prompt configured in sudoers for
    unattended execution

-   Large file counts or extensive directory trees will cause
    significant performance degradation

-   Running with find on large home directories can consume considerable
    IO and CPU resources

-   The lslogins command retrieves last login information depending on
    wtmp/btmp logs; accuracy varies by distribution logging policies

-   Last command information depends on .bash_history being available
    and enabled; other shells use different history files

-   Network-mounted home directories (NFS, SMB) will significantly
    increase command execution time

-   On systems with many users, overall execution time can be
    substantial; consider running during off-peak hours

# See Also {#see-also .unnumbered}

-   find-largest-storage-users

-   du-sort-largest-directories

-   disk-space-usage-per-directory

-   find-large-files-recursive

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

caution

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux

# Created At {#created-at .unnumbered}

2026-04-21

# Updated At {#updated-at .unnumbered}

2026-04-21
