# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

filesystem

# Command {#command .unnumbered}

    find . -type f -size +100M -exec ls -lh \{\} + | awk '\{print \$5, \$9\}' | sort -hr

# Explanation {#explanation .unnumbered}

The command uses 'find' to recursively traverse the directory tree,
filter for regular files (-type f), and select those exceeding 100 MB
(-size +100M). The '-exec ls -lh {} +' displays detailed information for
each file in a batch operation, which is more efficient than using
'\\{};'. The output is piped to 'awk' to extract the file size and path,
then 'sort -hr' sorts the results by human-readable sizes in descending
order, showing the largest files first.

# Tags {#tags .unnumbered}

find, filesystem, disk-usage, large-files, recursive, storage

# Dependencies {#dependencies .unnumbered}

findutils, coreutils

# Arguments {#arguments .unnumbered}

1.  **PATH** (Optional): Root directory to start the recursive search
    (default: current directory)\
    Default: .

2.  **SIZE** (Optional): Minimum file size threshold (default: 100M,
    supports K, M, G suffixes)\
    Default: 100M

# Examples {#examples .unnumbered}

1.  `find . -type f -size +100M -exec ls -lh {} + | awk ’{print $5, $9}’ | sort -hr` -
    Find files larger than 100 MB in current directory and
    subdirectories

2.  `find /var -type f -size +500M -exec ls -lh {} + | awk ’{print $5, $9}’ | sort -hr` -
    Find large files in /var directory

3.  `find . -type f -size +1G -exec ls -lh {} + | awk ’{print $5, $9}’ | sort -hr` -
    Find files larger than 1 GB

4.  `find . -type f -size +50M -exec ls -lh {} + | awk ’{print $5, $9}’ | sort -hr | head -20` -
    Show top 20 largest files over 50 MB

# Output {#output .unnumbered}

    1.5G ./videos/archive.tar.gz
    987M ./backups/database.sql.bz2
    756M ./datasets/training-data.bin
    543M ./cache/node\_modules.tar
    387M ./downloads/ubuntu-22.04-iso
    256M ./logs/app-2026.log
    198M ./tmp/large-temp-file

# Notes {#notes .unnumbered}

-   The -size option supports various units: c (bytes), k (kilobytes), M
    (megabytes), G (gigabytes), and b (512-byte blocks)

-   By default, -size rounds up (e.g., +100M matches files larger than
    100 MiB)

-   Use -size -100M to find files smaller than 100 MB

-   The command may take considerable time on large directory trees

-   Using '{} +' instead of '{} \\{};' is more efficient as it batches
    the command executions

-   Results may be incomplete in directories where you lack read
    permissions

# Warnings {#warnings .unnumbered}

-   On network filesystems (NFS, SMB), this command may be significantly
    slower

-   Does not follow symbolic links by default; add -L flag if needed

-   Very large directory trees may cause the command to run for extended
    periods

-   Some filesystems may not report accurate sizes for sparse files

# See Also {#see-also .unnumbered}

-   find-largest-storage-users

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
