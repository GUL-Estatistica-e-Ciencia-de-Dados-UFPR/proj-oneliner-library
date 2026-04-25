# Convert CSV file to TSV (tab-separated values) using Python stdlib {#convert-csv-file-to-tsv-tab-separated-values-using-python-stdlib .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-25

Converts comma-separated values (CSV) to tab-separated values (TSV)
using Python's standard library csv module.

# Language {#language .unnumbered}

python

# Category {#category .unnumbered}

data-processing

# Command {#command .unnumbered}

    python3 -c "import sys,csv; csv.writer(sys.stdout, delimiter='\t').writerows(csv.reader(sys.stdin))"

# Explanation {#explanation .unnumbered}

The command reads CSV data from stdin, parses it with csv.reader
(default delimiter is comma), and writes it to stdout using csv.writer
with tab delimiter. It preserves quoting and escaping rules.

# Tags {#tags .unnumbered}

python, csv, tsv, data-conversion, text-processing

# Dependencies {#dependencies .unnumbered}

python3

# Arguments {#arguments .unnumbered}

1.  **INPUT_FILE** (Optional): CSV input file (use stdin redirection)\
    Default: stdin

2.  **OUTPUT_FILE** (Optional): TSV output file (use stdout
    redirection)\
    Default: stdout

# Examples {#examples .unnumbered}

1.  `python3 -c "import sys,csv; csv.writer(sys.stdout, delimiter=’\{}t’).writerows(csv.reader(sys.stdin))" < data.csv > data.tsv` -
    Convert data.csv to data.tsv

2.  `cat data.csv | python3 -c "import sys,csv; csv.writer(sys.stdout, delimiter=’\{}t’).writerows(csv.reader(sys.stdin))" | head -20` -
    Preview first 20 rows converted

# Output {#output .unnumbered}

    col1    col2    col3
    value1  value2  value3

# Notes {#notes .unnumbered}

-   Handles quoted fields with commas correctly

-   Preserves newlines within quoted fields

-   Works with any CSV dialect compatible with Python's csv module

# Warnings {#warnings .unnumbered}

-   Large files may consume memory as all rows are read into list

-   Input must be valid CSV format

# See Also {#see-also .unnumbered}

-   tsv-to-csv

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
