# Display disk space usage for all directories with hierarchical breakdown {#display-disk-space-usage-for-all-directories-with-hierarchical-breakdown .unnumbered}

**Author:** marcos **Date:** 2026-04-21

Shows disk space usage for directories up to 2 levels deep in the
current directory tree, sorted by size in descending order with
human-readable format, providing a hierarchical breakdown of disk
consumption.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

disk-usage

# Command {#command .unnumbered}

    du -h --max-depth=2 . | sort -hr

# Explanation {#explanation .unnumbered}

The command uses 'du -h' to calculate disk usage in human-readable
format. The '--max-depth=2' flag limits output to directories up to 2
levels deep from the current directory, avoiding excessive detail while
still showing the hierarchy. The '.' specifies the starting directory.
The output is piped to 'sort -hr' to sort in descending order by
human-readable sizes, making it easy to identify which directories
consume the most space at each level.

# Tags {#tags .unnumbered}

du, disk-usage, directories, storage, hierarchical, sort,
system-administration

# Dependencies {#dependencies .unnumbered}

coreutils

# Arguments {#arguments .unnumbered}

1.  **PATH** (Optional): Root directory to analyze (default: current
    directory)\
    Default: .

2.  **DEPTH** (Optional): Maximum directory depth to traverse (default:
    2)\
    Default: 2

# Examples {#examples .unnumbered}

1.  `du -h –max-depth=2 . | sort -hr` - Show disk usage up to 2 levels
    deep from current directory

2.  `du -h –max-depth=1 . | sort -hr` - Show only immediate
    subdirectories (1 level deep)

3.  `du -h –max-depth=3 /home | sort -hr` - Show disk usage in /home up
    to 3 levels deep

4.  `du -h –max-depth=2 . | sort -hr | head -20` - Show top 20
    directories by size (2 levels deep)

5.  `du -ah –max-depth=2 . | sort -hr | head -15` - Include files in the
    listing, show top 15 items

# Output {#output .unnumbered}

    1.2T    .
    847G    ./data
    512G    ./data/cache
    256G    ./data/backups
    244G    ./media
    128G    ./media/videos
    116G    ./media/archives
    156G    ./documents
    96G ./documents/projects
    60G ./documents/reports

# Notes {#notes .unnumbered}

-   The --max-depth flag controls recursion depth: 0 shows only the
    starting directory, 1 shows immediate children, etc.

-   The -h flag makes output human-readable (K, M, G, T); use -B 1M for
    sizes in fixed block units

-   The -s flag is not needed here as du summarizes by default

-   Hidden directories (those starting with .) are included
    automatically

-   Each line shows cumulative size for that directory and all its
    contents

-   Symbolic links are not followed by default; add -L to follow
    symlinks

-   On filesystems with many nested directories, increasing --max-depth
    may significantly increase runtime

# Warnings {#warnings .unnumbered}

-   Results may be incomplete if you lack read permissions on some
    directories

-   On network filesystems (NFS, SMB), this command can be slow due to
    network latency

-   Very deep directory hierarchies combined with high --max-depth
    values may cause excessive output

-   Sparse files may report misleading sizes on some filesystems

# See Also {#see-also .unnumbered}

-   disk-space-sort-largest-directories

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
