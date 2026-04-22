# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

disk-usage

# Command {#command .unnumbered}

    du -sh */ | sort -hr | head -10

# Explanation {#explanation .unnumbered}

The command uses 'du -sh' to calculate the total disk usage for each
directory in human-readable format. The '\*/' glob pattern matches only
directories (not files). The output is piped to 'sort -hr' to sort in
descending order using human-readable number comparison, with the
largest directories appearing first. Finally, 'head -10' limits output
to the top 10 directories.

# Tags {#tags .unnumbered}

du, disk-usage, directories, storage, sort, system-administration

# Dependencies {#dependencies .unnumbered}

coreutils

# Arguments {#arguments .unnumbered}

1.  **PATH** (Optional): Directory path to analyze (default: current
    directory)\
    Default: .

2.  **COUNT** (Optional): Number of largest directories to display
    (default: 10)\
    Default: 10

# Examples {#examples .unnumbered}

1.  `du -sh */ | sort -hr | head -10` - Show top 10 largest
    subdirectories in current directory

2.  `du -sh */ | sort -hr` - Show all subdirectories sorted by size
    without limit

3.  `du -sh */ | sort -hr | head -5` - Show top 5 largest subdirectories

4.  `du -sh ./* | sort -hr | head -10` - Include hidden files and
    directories (those starting with dot)

5.  `cd /var && du -sh */ | sort -hr | head -10` - Find largest
    subdirectories in /var

# Output {#output .unnumbered}

    847G    cache/
    512G    data/
    256G    backups/
    128G    logs/
    96G documents/
    64G downloads/
    32G pictures/
    16G videos/
    8.5G    archives/
    2.1G    temp/

# Notes {#notes .unnumbered}

-   The '\*/' pattern matches only directories; use '\*' to include
    files as well

-   The -h flag makes output human-readable (K, M, G, T); use -B for a
    specific block size

-   The -s flag summarizes each directory's total size instead of
    listing contents recursively

-   Hidden directories (starting with .) are excluded; use './\*' or
    '\*' (with shopt) to include them

-   On systems with many subdirectories, results are calculated quickly
    since du only traverses each directory once

-   Symbolic links are not followed by default; add -L flag to follow
    symlinks

-   Results may vary if some directories are mounted on different
    filesystems or are inaccessible due to permissions

# Warnings {#warnings .unnumbered}

-   Results may be incomplete or misleading if you lack read permissions
    on some directories

-   On network filesystems (NFS, SMB), the command may be slower due to
    network latency

-   If dealing with millions of directories, the command can consume
    considerable memory and time

-   Sparse files may cause inaccurate size reporting on some filesystems

# See Also {#see-also .unnumbered}

-   find-largest-storage-users

-   find-large-files-recursive

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-21

# Updated At {#updated-at .unnumbered}

2026-04-21
