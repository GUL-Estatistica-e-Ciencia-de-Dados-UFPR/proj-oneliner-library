# Find users with largest storage usage {#find-users-with-largest-storage-usage .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-21

Displays the top 10 users on the system by storage consumption in their
home directories, sorted in descending order by disk usage.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

disk-usage

# Command {#command .unnumbered}

    du -sh /home/* 2>/dev/null | sort -hr | head -10

# Explanation {#explanation .unnumbered}

The command uses 'du -sh' to calculate the total disk usage in
human-readable format for each home directory. The '2\>/dev/null'
suppresses permission denied errors for inaccessible directories. The
output is piped to 'sort -hr' to sort in descending order (largest
first) using human-readable number comparison. Finally, 'head -10'
limits the output to the top 10 users.

# Tags {#tags .unnumbered}

disk-usage, storage, users, system-administration, du, sort

# Dependencies {#dependencies .unnumbered}

coreutils, findutils

# Arguments {#arguments .unnumbered}

1.  **PATH** (Optional): Home directory path to analyze (default:
    /home)\
    Default: /home

2.  **COUNT** (Optional): Number of top users to display (default: 10)\
    Default: 10

# Examples {#examples .unnumbered}

1.  `du -sh /home/* 2>/dev/null | sort -hr | head -10` - Show top 10
    users by storage usage in /home

2.  `du -sh /home/* 2>/dev/null | sort -hr` - Show all users sorted by
    storage usage without limit

3.  `du -sh /home/* 2>/dev/null | sort -hr | head -5` - Show top 5 users
    by storage usage

4.  `du -sh /root /home/* 2>/dev/null | sort -hr | head -10` - Include
    root's home directory in the analysis

# Output {#output .unnumbered}

    450G    /home/alice
    320G    /home/bob
    215G    /home/charlie
    156G    /home/diana
    98G /home/eve
    67G /home/frank
    45G /home/grace
    32G /home/henry
    28G /home/iris
    19G /home/jack

# Notes {#notes .unnumbered}

-   The command suppresses permission errors with '2\>/dev/null',
    allowing users to see results without elevated privileges

-   Human-readable format (-h) displays sizes in K, M, G, etc., making
    interpretation easier

-   Sort with -h flag properly handles human-readable numbers (not
    lexicographic sorting)

-   Symbolic links in /home are counted separately if they point outside
    /home

-   Hidden files and directories within user homes are included in the
    totals

-   Results may vary if some home directories are mounted on different
    filesystems

# Warnings {#warnings .unnumbered}

-   Results may be incomplete if you lack read permissions on certain
    home directories

-   On systems with many users, this command may take considerable time
    to complete

-   NFS-mounted or slow storage may cause noticeable delays

# See Also {#see-also .unnumbered}

-   find-large-files-recursive

-   disk-space-usage-per-directory

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd

# Created At {#created-at .unnumbered}

2026-04-21

# Updated At {#updated-at .unnumbered}

2026-04-21
