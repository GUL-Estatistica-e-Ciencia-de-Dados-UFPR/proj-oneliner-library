# Create a large file of a specific size quickly {#create-a-large-file-of-a-specific-size-quickly .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-21

Quickly creates a file of a specific size (e.g., 1 GB) using fallocate,
which is much faster than dd because it allocates blocks without writing
actual data.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

filesystem

# Command {#command .unnumbered}

    fallocate -l 1G test_file

# Explanation {#explanation .unnumbered}

The 'fallocate' command communicates directly with the filesystem to
preallocate disk space for a file. Unlike 'dd', which must write every
byte to disk, 'fallocate' simply marks the space as allocated in the
filesystem's metadata. This is extremely efficient for creating large
test files, swap files, or preallocating space for databases. The length
(-l) can be specified in bytes or using suffixes like K, M, G, T, P, E.

# Tags {#tags .unnumbered}

fallocate, filesystem, storage, disk-usage, allocation, testing

# Dependencies {#dependencies .unnumbered}

util-linux

# Arguments {#arguments .unnumbered}

1.  **SIZE** (Optional): The size of the file to create (e.g., 10M, 1G,
    500M).\
    Default: 1G

2.  **FILENAME** (Optional): The name of the file to be created.\
    Default: test_file

# Examples {#examples .unnumbered}

1.  `fallocate -l 100M dummy_file` - Create a 100 MB file named
    dummy_file

2.  `fallocate -l 1G large_test_file` - Create a 1 GB file for testing

3.  `fallocate -l 10G /swapfile` - Preallocate 10 GB for a swap file
    (requires subsequent mkswap and swapon)

# Output {#output .unnumbered}

    (No output on success)

# Notes {#notes .unnumbered}

-   Not all filesystems support fallocate. It is well-supported on ext4,
    xfs, btrfs, and ocfs2.

-   If the filesystem doesn't support fallocate, you can use 'truncate
    -s SIZE FILENAME' as a fallback, though it creates a sparse file.

-   For older systems or filesystems, 'dd if=/dev/zero of=FILENAME bs=1M
    count=SIZE_IN_MB' is the most compatible but much slower method.

# Warnings {#warnings .unnumbered}

-   This command will overwrite the specified file if it already exists.

-   On some filesystems, the allocated space may contain 'stale' data
    from previously deleted files, though modern Linux filesystems
    (ext4, xfs) zero-fill or mark it as uninitialized for security.

-   Ensure you have enough free disk space before running this command.

# See Also {#see-also .unnumbered}

-   find-large-files-recursive

-   disk-space-usage-per-directory

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

caution

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux

# Created At {#created-at .unnumbered}

2026-04-21

# Updated At {#updated-at .unnumbered}

2026-04-21
