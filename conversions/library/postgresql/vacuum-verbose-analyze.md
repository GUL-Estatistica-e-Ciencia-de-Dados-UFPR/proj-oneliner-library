# Perform PostgreSQL VACUUM with VERBOSE and ANALYZE options {#perform-postgresql-vacuum-with-verbose-and-analyze-options .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-25

Executes PostgreSQL VACUUM operation with VERBOSE output and ANALYZE for
statistics update, following best practices for database maintenance.
Accepts arguments: username password database host.

# Language {#language .unnumbered}

postgresql

# Category {#category .unnumbered}

database

# Command {#command .unnumbered}

    PGPASSWORD="$2" psql -U "$1" -d "$3" -h "$4" -c "VACUUM (VERBOSE, ANALYZE);"

# Explanation {#explanation .unnumbered}

The command connects to PostgreSQL via psql and runs VACUUM with VERBOSE
(detailed output) and ANALYZE (update statistics). VACUUM reclaims
storage occupied by dead tuples, while ANALYZE updates planner
statistics. This combination is recommended for routine maintenance.
Arguments: \$1=username, \$2=password (sets PGPASSWORD), \$3=database,
\$4=host.

# Tags {#tags .unnumbered}

postgresql, database, maintenance, vacuum, optimization

# Dependencies {#dependencies .unnumbered}

postgresql-client

# Arguments {#arguments .unnumbered}

1.  **USERNAME** (Required): PostgreSQL username

2.  **PASSWORD** (Required): PostgreSQL password (sets PGPASSWORD
    environment variable)

3.  **DATABASE** (Required): Database name

4.  **HOST** (Optional): Database host\
    Default: localhost

# Examples {#examples .unnumbered}

1.  `vacuum_pg() { PGPASSWORD="$2" psql -U "$1" -d "$3" -h "$4" -c "VACUUM (VERBOSE, ANALYZE);"; }` -
    Define shell function for alias usage

2.  `vacuum_pg postgres secret123 mydb localhost` - Call function with
    arguments: user password db host

3.  `PGPASSWORD="secret456" psql -U "appuser" -d "production" -h "db.example.com" -c "VACUUM (VERBOSE, ANALYZE);"` -
    Direct command with explicit values

# Output {#output .unnumbered}

    VACUUM
    INFO:  vacuuming "public.some_table"
    INFO:  "some_table": removed 1000 row versions in 5 pages
    INFO:  "some_table": found 1000 removable, 5000 nonremovable row versions
    DETAIL:  0 dead row versions cannot be removed yet.
    CPU 0.00s/0.00u sec elapsed 0.00 sec.
    INFO:  analyzing "public.some_table"
    INFO:  "some_table": scanned 3000 of 3000 pages, containing 5000 live rows and 0 dead rows
    VACUUM

# Notes {#notes .unnumbered}

-   Run during periods of low database activity

-   VERBOSE provides detailed output for monitoring

-   ANALYZE updates statistics for query planner

-   Consider using .pgpass file for password management

-   Monitor pg_stat_activity for concurrent sessions

-   For alias usage: vacuum_pg() { PGPASSWORD=\"\$2\" psql -U \"\$1\" -d
    \"\$3\" -h \"\$4\" -c \"VACUUM (VERBOSE, ANALYZE);\"; }

# Warnings {#warnings .unnumbered}

-   VACUUM requires ACCESS SHARE lock on tables (conflicts with DDL)

-   Avoid running during peak hours or critical operations

-   For aggressive cleanup, consider VACUUM FULL but it requires
    exclusive lock

-   Ensure adequate maintenance_work_mem setting for performance

# See Also {#see-also .unnumbered}

-   postgresql-reindex

-   postgresql-analyze-only

# Status {#status .unnumbered}

reviewed

# Safety {#safety .unnumbered}

caution

# Shell {#shell .unnumbered}

bash

# Platforms {#platforms .unnumbered}

linux, gnu-linux, freebsd, openbsd, netbsd

# Created At {#created-at .unnumbered}

2026-04-25

# Updated At {#updated-at .unnumbered}

2026-04-25
