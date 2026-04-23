# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

diagnostics

# Command {#command .unnumbered}

    dmesg -T -x --level=emerg,alert,crit,err,warn --color=always 2>/dev/null | awk 'BEGIN { print "\033[1m=== KERNEL MESSAGE SUMMARY ===\033[0m" } { lines[NR] = \$0; lvl = \$2; gsub(/\x1B\[[0-9;]*[mK]/, \"\", lvl); gsub(/[: \t]/, \"\", lvl); if(lvl ~ /^(emerg|alert|crit|err|warn|notice|info|debug)\$/) cnt[lvl]++; if(lvl ~ /^\w+\$/) all_cnt[lvl]++ } END { if(NR>0) { print "\033[1m--- ERRORS & WARNINGS ---\033[0m"; for(l in cnt) printf \"  %-7s : %d\n\", l, cnt[l]; print "\033[1m--- ALL MESSAGES (by severity) ---\033[0m"; for(l in all_cnt) printf \"  %-7s : %d\n\", l, all_cnt[l]; print "\033[1m======================================\033[0m\n"; for(i=1; i<=NR; i++) print lines[i] } else print "No kernel messages found for selected levels." }'

# Explanation {#explanation .unnumbered}

The one-liner uses 'dmesg -T -x' to extract kernel messages with
human-readable timestamps (-T) and decode the facility/level prefixes
(-x). We filter for all severity levels
(emerg,alert,crit,err,warn,notice,info,debug) via '--level'. The
'--color=always' flag preserves standard color coding. The output is
piped into 'awk', which does several tasks: (1) strips ANSI escape
sequences from the second column to cleanly count occurrences, (2)
maintains two counters: one for 'errors/warnings'
(emerg,alert,crit,err,warn) and another for 'all messages' (all severity
levels), and (3) stores all log lines in memory. The END block prints a
formatted summary frontmatter with both the 'errors/warnings' and 'all
messages' counts, followed by the original colorized logs.

# Tags {#tags .unnumbered}

dmesg, kernel, errors, warnings, logs, troubleshooting, monitoring,
summary, awk, diagnostics, severity, log-analysis, linux, system,
administration

# Dependencies {#dependencies .unnumbered}

util-linux, gawk

# Arguments {#arguments .unnumbered}

None

# Examples {#examples .unnumbered}

1.  `dmesg -T -x –level=emerg,alert,crit,err,warn –color=always 2>/dev/null | awk ’BEGIN { print "\{}033[1m=== KERNEL MESSAGE SUMMARY ===\{}033[0m" } { lines[NR] = \{}$0; lvl = \{}$2; gsub(/\{}x1B\{}[[0-9;]*[mK]/, \{}"\{}", lvl); gsub(/[: \{}t]/, \{}"\{}", lvl); if(lvl ~ /^(emerg|alert|crit|err|warn|notice|info|debug)\{}$/) cnt[lvl]++; if(lvl ~ /^\{}w+\{}$/) all_cnt[lvl]++ } END { if(NR>0) { print "\{}033[1m— ERRORS & WARNINGS —\{}033[0m"; for(l in cnt) printf \{}" %-7s : %d\{}n\{}", l, cnt[l]; print "\{}033[1m— ALL MESSAGES (by severity) —\{}033[0m"; for(l in all_cnt) printf \{}" %-7s : %d\{}n\{}", l, all_cnt[l]; print "\{}033[1m======================================\{}033[0m\{}n"; for(i=1; i<=NR; i++) print lines[i] } else print "No kernel messages found for selected levels." }’` -
    Show full severity summary and colorized kernel messages

2.  `dmesg -T -x –level=emerg,alert,crit,err,warn –color=always 2>/dev/null | awk ’BEGIN { print "\{}033[1m=== KERNEL MESSAGE SUMMARY ===\{}033[0m" } { lines[NR] = \{}$0; lvl = \{}$2; gsub(/\{}x1B\{}[[0-9;]*[mK]/, \{}"\{}", lvl); gsub(/[: \{}t]/, \{}"\{}", lvl); if(lvl ~ /^(emerg|alert|crit|err|warn|notice|info|debug)\{}$/) cnt[lvl]++; if(lvl ~ /^\{}w+\{}$/) all_cnt[lvl]++ } END { if(NR>0) { print "\{}033[1m— ERRORS & WARNINGS —\{}033[0m"; for(l in cnt) printf \{}" %-7s : %d\{}n\{}", l, cnt[l]; print "\{}033[1m— ALL MESSAGES (by severity) —\{}033[0m"; for(l in all_cnt) printf \{}" %-7s : %d\{}n\{}", l, all_cnt[l]; print "\{}033[1m======================================\{}033[0m\{}n"; for(i=1; i<=NR; i++) print lines[i] } else print "No kernel messages found for selected levels." }’ | less -R` -
    Show the summary and logs with a pager, preserving colors

3.  `sudo dmesg -T -x –level=emerg,alert,crit,err,warn –color=always 2>/dev/null | awk ’BEGIN { print "\{}033[1m=== KERNEL MESSAGE SUMMARY ===\{}033[0m" } { lines[NR] = \{}$0; lvl = \{}$2; gsub(/\{}x1B\{}[[0-9;]*[mK]/, \{}"\{}", lvl); gsub(/[: \{}t]/, \{}"\{}", lvl); if(lvl ~ /^(emerg|alert|crit|err|warn|notice|info|debug)\{}$/) cnt[lvl]++; if(lvl ~ /^\{}w+\{}$/) all_cnt[lvl]++ } END { if(NR>0) { print "\{}033[1m— ERRORS & WARNINGS —\{}033[0m"; for(l in cnt) printf \{}" %-7s : %d\{}n\{}", l, cnt[l]; print "\{}033[1m— ALL MESSAGES (by severity) —\{}033[0m"; for(l in all_cnt) printf \{}" %-7s : %d\{}n\{}", l, all_cnt[l]; print "\{}033[1m======================================\{}033[0m\{}n"; for(i=1; i<=NR; i++) print lines[i] } else print "No kernel messages found for selected levels." }’` -
    Run with sudo to access kernel ring buffer on restricted systems

# Output {#output .unnumbered}

    \u001b[1m=== KERNEL MESSAGE SUMMARY ===\u001b[0m
    \u001b[1m--- ERRORS & WARNINGS ---\u001b[0m
      err     : 2
      warn    : 3
      crit    : 1
    \u001b[1m--- ALL MESSAGES (by severity) ---\u001b[0m
      err     : 2
      warn    : 3
      crit    : 1
      notice  : 5
      info    : 12
      debug   : 0
    \u001b[1m======================================\u001b[0m

    kern  :err   : [Tue Apr 21 10:00:00 2026] sd 0:0:0:0: [sda] Write cache: enabled
    kern  :warn  : [Tue Apr 21 10:01:23 2026] WARNING: CPU: 0 PID: 1234
    kern  :crit  : [Tue Apr 21 10:02:45 2026] Critical hardware error
    kern  :warn  : [Tue Apr 21 10:05:00 2026] ext4-fs: mounted with warnings
    kern  :err   : [Tue Apr 21 10:06:12 2026] usb 1-1: device descriptor read/64, error -71
    kern  :warn  : [Tue Apr 21 10:08:34 2026] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
    kern  :notice: [Tue Apr 21 10:10:00 2026] Kernel log system initialized
    kern  :info  : [Tue Apr 21 10:15:00 2026] Network interface eth0 up and running

# Notes {#notes .unnumbered}

-   Requires read access to the kernel ring buffer, which often requires
    sudo or being in the 'adm' group on some distributions.

-   The '-x' (--decode) flag is critical here as it explicitly outputs
    the severity level on every line, making awk parsing reliable.

-   ANSI stripping regex in awk ensures color codes don't interfere with
    severity counting.

-   This command counts all message severity levels: emerg, alert, crit,
    err, warn, notice, info, debug.

-   The 'errors & warnings' summary includes: emerg, alert, crit, err,
    warn.

-   The 'all messages' summary includes all severity levels, providing
    complete log statistics.

-   The entire dmesg output is stored in awk's memory (the 'lines'
    array) before printing, which is perfectly safe for typical volumes
    but could consume slightly more memory on massively flooded systems.

# Warnings {#warnings .unnumbered}

-   Running without sufficient privileges (like sudo) will result in a
    blank output or a permission denied error on most modern secure
    Linux distributions.

# See Also {#see-also .unnumbered}

-   find-large-files-recursive

-   disk-space-sort-largest-directories

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux

# Created At {#created-at .unnumbered}

2026-04-21

# Updated At {#updated-at .unnumbered}

2026-04-21
