# Show system executables with errors/failures from today's journal {#show-system-executables-with-errorsfailures-from-todays-journal .unnumbered}

**Author:** marcos **Date:** 2026-04-22

Lists system executables that have generated failure, error, or fatal
messages in today's journal logs, sorted by frequency.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

system-monitoring

# Command {#command .unnumbered}

    echo "=== Errors/Failures in Today's Journal ==="; journalctl --no-pager --since today --grep 'fail|error|fatal' --output json | jq -r '._EXE' | sort | uniq -c | sort -nr | awk '{printf "%4d  %s\n", $1, $2}'

# Explanation {#explanation .unnumbered}

The command retrieves all journal entries from today (since midnight),
filters for messages containing the keywords 'fail', 'error', or 'fatal'
(case-insensitive regex), outputs the results in JSON format for
parsing, extracts the executable name (\_EXE field) from each log entry,
counts occurrences of each executable, sorts them numerically in
descending order (most frequent first), and formats the output with a
header and aligned columns for readability.

# Tags {#tags .unnumbered}

journalctl, systemd, logs, monitoring, troubleshooting, errors, failure,
system-administration, diagnostics, debugging, logging, bash, jq,
text-processing, process-management

# Dependencies {#dependencies .unnumbered}

systemd, jq

# Arguments {#arguments .unnumbered}

None

# Examples {#examples .unnumbered}

1.  `journalctl-errors-today` - Show errors/failures from today's
    journal

2.  `journalctl –no-pager –since yesterday –grep ’fail|error|fatal’ –output json | jq -r ’._EXE’ | sort | uniq -c | sort -nr` -
    Show errors/failures from yesterday's journal (raw output)

# Output {#output .unnumbered}

    === Errors/Failures in Today's Journal ===
       5  /usr/bin/systemd
       3  /usr/bin/foo-daemon
       1  /usr/lib/bar-service

# Notes {#notes .unnumbered}

-   Requires journalctl (systemd) and jq to be installed

-   Only shows entries from the current day (midnight to now)

-   Requires appropriate permissions to read journal logs

-   The regex pattern 'fail\|error\|fatal' matches any of these words in
    log messages

-   Output is sorted by count (highest first) for easy identification of
    frequent issues

# Warnings {#warnings .unnumbered}

None

# See Also {#see-also .unnumbered}

-   dmesg-errors-pretty

-   user-activity-and-quota-report

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux

# Created At {#created-at .unnumbered}

2026-04-22

# Updated At {#updated-at .unnumbered}

2026-04-22
