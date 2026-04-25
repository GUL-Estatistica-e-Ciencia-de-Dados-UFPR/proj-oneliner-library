# Convert TSV (tab-separated values) file to CSV using Python stdlib {#convert-tsv-tab-separated-values-file-to-csv-using-python-stdlib .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-25

Converts tab-separated values (TSV) to comma-separated values (CSV)
using Python's standard library csv module.

# Language {#language .unnumbered}

python

# Category {#category .unnumbered}

data-processing

# Command {#command .unnumbered}

    python3 -c "import sys,csv; csv.writer(sys.stdout).writerows(csv.reader(sys.stdin, delimiter='\t'))"

# Explanation {#explanation .unnumbered}

The command reads TSV data from stdin, parses it with csv.reader using
tab delimiter, and writes it to stdout using csv.writer with default
comma delimiter. It preserves quoting and escaping rules.

# Tags {#tags .unnumbered}

python, tsv, csv, data-conversion, text-processing

# Dependencies {#dependencies .unnumbered}

python3

# Arguments {#arguments .unnumbered}

1.  **INPUT_FILE** (Optional): TSV input file (use stdin redirection)\
    Default: stdin

2.  **OUTPUT_FILE** (Optional): CSV output file (use stdout
    redirection)\
    Default: stdout

# Examples {#examples .unnumbered}

1.  `python3 -c "import sys,csv; csv.writer(sys.stdout).writerows(csv.reader(sys.stdin, delimiter=’\{}t’))" < data.tsv > data.csv` -
    Convert data.tsv to data.csv

2.  `cat data.tsv | python3 -c "import sys,csv; csv.writer(sys.stdout).writerows(csv.reader(sys.stdin, delimiter=’\{}t’))" | head -20` -
    Preview first 20 rows converted

# Output {#output .unnumbered}

    col1,col2,col3
    value1,value2,value3

# Notes {#notes .unnumbered}

-   Handles quoted fields with tabs correctly

-   Preserves newlines within quoted fields

-   Works with any TSV dialect compatible with Python's csv module

# Warnings {#warnings .unnumbered}

-   Large files may consume memory as all rows are read into list

-   Input must be valid TSV format

# See Also {#see-also .unnumbered}

-   csv-to-tsv

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
