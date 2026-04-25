# Initialize git repository, stage all files and create empty .gitignore {#initialize-git-repository-stage-all-files-and-create-empty-.gitignore .unnumbered}

**Author:** marcos **Date:** 2026-04-25

Initializes a new git repository in current directory, stages all
existing files, and creates an empty .gitignore file.

# Language {#language .unnumbered}

git

# Category {#category .unnumbered}

version-control

# Command {#command .unnumbered}

    git init && git add . && touch .gitignore

# Explanation {#explanation .unnumbered}

This command sequence creates a new git repository (git init), adds all
files in the current directory to the staging area (git add .), and
creates an empty .gitignore file (touch .gitignore) for future ignore
patterns.

# Tags {#tags .unnumbered}

git, version-control, repository, init, gitignore

# Dependencies {#dependencies .unnumbered}

git

# Arguments {#arguments .unnumbered}

1.  **DIRECTORY** (Optional): Directory where to initialize repository\
    Default: .

# Examples {#examples .unnumbered}

1.  `git init && git add . && touch .gitignore` - Initialize repository
    in current directory

2.  `cd /path/to/project && git init && git add . && touch .gitignore` -
    Initialize repository in specific directory

# Output {#output .unnumbered}

    Initialized empty Git repository in /home/user/project/.git/

# Notes {#notes .unnumbered}

-   The .gitignore file is empty after creation; you should add patterns
    to ignore unnecessary files

-   If .gitignore already exists, touch command updates its timestamp

-   Use git status to verify files are staged

# Warnings {#warnings .unnumbered}

-   git add . stages all files including potentially sensitive data

-   Review staged files before committing

# See Also {#see-also .unnumbered}

-   git-commit-initial

-   git-ignore-patterns

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

posix

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-25

# Updated At {#updated-at .unnumbered}

2026-04-25
