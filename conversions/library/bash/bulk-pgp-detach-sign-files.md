# Create detached PGP signatures for all files in a directory {#create-detached-pgp-signatures-for-all-files-in-a-directory .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-28

Iterates over every file in a given directory and creates a detached PGP
signature (.sig) for each one using GnuPG.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

cryptography

# Command {#command .unnumbered}

    bash -c 'dir=$1; shift; for f in "$dir"/*; do [ -f "$f" ] && gpg --detach-sign "$f"; done' _

# Explanation {#explanation .unnumbered}

This oneliner uses a bash -c subshell to accept the target directory as
a trailing argument. The variable dir receives \$1 (the directory path),
then shift removes it so remaining arguments are available via \$@. A
for loop iterates over all entries matching \"\$dir\"/\*, and \[ -f
\"\$f\" \] ensures only regular files are processed (skipping
subdirectories, symlinks, etc.). For each file, gpg --detach-sign
creates a separate .sig file containing the PGP signature. The \_
placeholder serves as \$0 inside the subshell, ensuring \$1 maps to the
first real argument.

# Tags {#tags .unnumbered}

gpg, pgp, cryptography, signature, detach-sign, bulk, verification

# Dependencies {#dependencies .unnumbered}

gnupg

# Arguments {#arguments .unnumbered}

1.  **DIR** (Optional): Path to the directory whose files will be
    signed.\
    Default: .

# Examples {#examples .unnumbered}

1.  `bash -c ’dir=$1; shift; for f in "$dir"/*; do [ -f "$f" ] && gpg –detach-sign "$f"; done’ _ /path/to/releases` -
    Sign all files in /path/to/releases

2.  `bash -c ’dir=$1; shift; for f in "$dir"/*; do [ -f "$f" ] && gpg –detach-sign "$f"; done’ _ .` -
    Sign all files in the current directory

3.  `alias bsign="bash -c ’dir=\{}$1; shift; for f in \{}"\{}$dir\{}"/*; do [ -f \{}"\{}$f\{}" ] && gpg –detach-sign \{}"\{}$f\{}"; done’ _"` -
    Create an alias named 'bsign' for easy bulk signing

4.  `bsign /path/to/releases` - Use the alias to sign all files in a
    directory

# Output {#output .unnumbered}

    file1.tar.gz.sig
    file2.iso.sig
    file3.deb.sig

# Notes {#notes .unnumbered}

-   Each original file gets a corresponding .sig file in the same
    directory

-   GPG will prompt for passphrase if the private key is
    passphrase-protected

-   Uses the default signing key; set GPGKEY env var or use
    --default-key to specify another

-   The \[ -f \"\$f\" \] check skips subdirectories and non-regular
    files

-   Hidden files (dotfiles) are not matched by the glob \*; use .\* as
    well if needed

-   For large numbers of files, consider using gpg --batch --yes to skip
    confirmation prompts

# Warnings {#warnings .unnumbered}

-   Existing .sig files will be silently overwritten without
    confirmation

-   Ensure you have sufficient disk space for the signature files

-   If GPG cannot access your private key, the loop will fail for every
    file

-   Signatures are created in the same directory as the source files

# See Also {#see-also .unnumbered}

-   find-large-files-recursive

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

caution

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-28

# Updated At {#updated-at .unnumbered}

2026-04-28
