# System memory report with top 10 consuming processes {#system-memory-report-with-top-10-consuming-processes .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-22

Displays system memory usage in human-readable format and lists the top
10 memory-consuming processes by percentage of memory used and resident
set size in MB.

# Language {#language .unnumbered}

bash

# Category {#category .unnumbered}

monitoring

# Command {#command .unnumbered}

    echo -e "Memory Report:\n$(free -h)\n\nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\n$(ps -eo pid,comm,%mem,rss --sort=-%mem | awk 'NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\n", $1, $2, $3, $4/1024}' | head -n 11)"

# Explanation {#explanation .unnumbered}

The command uses 'free -h' to show memory statistics in human-readable
units (e.g., MB, GB). It then uses 'ps' to list all processes sorted by
memory usage (%MEM) in descending order, showing the top 10 processes
including their RSS (Resident Set Size) converted to MB. The awk command
formats the output to display PID, COMMAND, %MEM, and RSS(MB) with
proper headers. The output is formatted with clear section headers and
spacing for readability.

# Tags {#tags .unnumbered}

memory, system-monitoring, top-processes, ram, ps, free

# Dependencies {#dependencies .unnumbered}

bash, coreutils, procps-ng

# Arguments {#arguments .unnumbered}

None

# Examples {#examples .unnumbered}

1.  `echo -e "Memory Report:\{}n$(free -h)\{}n\{}nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\{}n$(ps -eo pid,comm,%mem,rss –sort=-%mem | awk ’NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\{}n", $1, $2, $3, $4/1024}’ | head -n 11)"` -
    Run the memory report oneliner directly in the shell

2.  `alias memreport=’echo -e "Memory Report:\{}n$(free -h)\{}n\{}nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\{}n$(ps -eo pid,comm,%mem,rss –sort=-%mem | awk ’NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\{}n", $1, $2, $3, $4/1024}’ | head -n 11)"’ && memreport` -
    Define as an alias and then execute it

# Output {#output .unnumbered}

    Memory Report:
                  total        used        free      shared  buff/cache   available
    Mem:           7.7G        2.3G        3.1G        256M        2.3G        5.0G
    Swap:          2.0G          0B        2.0G

    Top 10 Memory Consuming Processes (%MEM and RSS in MB):
      PID COMMAND         %MEM  RSS(MB)
     1234 firefox         15.2  1175.04
     5678 chrome          12.8   991.42
     9012 code             8.5   657.92
     3456 thunderbird      6.2   479.74
     7890 slack            4.1   317.12
     1122 python3          3.8   293.76
     3344 java             3.5   270.85
     5566 docker           2.9   224.26
     7788 Xorg             2.5   193.28
     9900 gnome-shell      2.2   170.24

# Notes {#notes .unnumbered}

-   The %MEM column shows the percentage of available physical memory
    used by the process.

-   The RSS(MB) column shows the Resident Set Size in megabytes
    (non-swapped physical memory used).

-   The header line is included in the top 10 output for clarity.

-   The awk command converts RSS from KB to MB by dividing by 1024 and
    formats to 2 decimal places.

# Warnings {#warnings .unnumbered}

None

# See Also {#see-also .unnumbered}

-   disk-usage-summary

-   cpu-top-processes

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

safe

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-22

# Updated At {#updated-at .unnumbered}

2026-04-22
