# Create multiple users from a CSV file containing username and password {#create-multiple-users-from-a-csv-file-containing-username-and-password .unnumbered}

**Author:** marcos **Date:** 2026-04-25

Creates multiple user accounts on a Linux system by reading username and
password pairs from a CSV file passed as an argument.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

system-administration

# Command {#command .unnumbered}

    sudo awk -F, 'NR>1 {print $1,$2}' "$1" | while read user pass; do sudo useradd -m "$user" && echo "$user:$pass" | sudo chpasswd; done

# Explanation {#explanation .unnumbered}

The command reads a CSV file (passed as first argument) where each row
contains a username and password. It skips the header row (NR\>1), then
for each subsequent row extracts the username and password fields. For
each user, it creates a system account with a home directory (-m) and
then uses chpasswd to set the plain text password from the CSV file.

# Tags {#tags .unnumbered}

user-management, bulk-operations, system-administration, csv, automation

# Dependencies {#dependencies .unnumbered}

coreutils, shadow-utils, openssl

# Arguments {#arguments .unnumbered}

1.  **CSV_FILE** (Required): Path to CSV file with username,password
    format

# Examples {#examples .unnumbered}

1.  `echo -e ’username,password\{}nuser1,pass123\{}nuser2,pass456’ > users.csv && sudo awk -F, ’NR>1 {print $1,$2}’ "users.csv" | while read user pass; do sudo useradd -m -p $(openssl passwd -1 "$pass") "$user"; done` -
    Create users from users.csv file with username,password format

2.  `sudo awk -F, ’NR>1 {print $1,$2}’ "/path/to/users.csv" | while read user pass; do sudo useradd -m -p $(openssl passwd -1 "$pass") "$user"; done` -
    Create users from a specific CSV file path

3.  `alias bulkaddusers=’sudo awk -F, ’"’"’NR>1 {print $1,$2}’"’"’ "$1" | while read user pass; do sudo useradd -m -p $(openssl passwd -1 "$pass") "$user"; done’` -
    Create an alias for bulk user creation

# Output {#output .unnumbered}

    Creating users from users.csv:
    user1: user created
    user2: user created

# Notes {#notes .unnumbered}

-   The CSV file should have a header row and contain username,password
    in each subsequent row

-   Requires sudo privileges to create users

-   Uses openssl to properly hash passwords for useradd

-   The -m flag creates a home directory for each user

-   The command skips the first line (header) with NR\>1

-   For better security, consider using a more robust password hashing
    method

-   The CSV file must be passed as the first argument to the command

# Warnings {#warnings .unnumbered}

-   This command requires sudo access and will modify system user
    accounts

-   Passwords are passed in cleartext in the CSV file which is a
    security risk

-   The default password hashing method (openssl passwd -1) uses MD5
    which is not the most secure

-   Always backup your system before running bulk user creation

-   Ensure CSV file permissions are secured to prevent unauthorized
    access

-   Test with a single entry first before running on multiple users

-   Consider using a more secure method for password handling in
    production environments

# See Also {#see-also .unnumbered}

-   user-activity-and-quota-report

-   nonhuman-user-activity-and-quota-report

# Status {#status .unnumbered}

draft

# Safety {#safety .unnumbered}

caution

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux

# Created At {#created-at .unnumbered}

2026-04-25

# Updated At {#updated-at .unnumbered}

2026-04-25
