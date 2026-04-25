# Load CSV file and print dataset statistics using R {#load-csv-file-and-print-dataset-statistics-using-r .unnumbered}

**Author:** Marcos de Carvalho **Date:** 2026-04-25

Loads a CSV file using R's read.csv and prints rows, columns, total
cells, file size, and object memory usage.

# Language {#language .unnumbered}

rscript

# Category {#category .unnumbered}

data-processing

# Command {#command .unnumbered}

    Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop('Need filename');df<-read.csv(args[1]);cat('Rows:',nrow(df),'Cols:',ncol(df),'Cells:',nrow(df)*ncol(df),'File size:',file.size(args[1]),'Object size:',format(object.size(df),units='auto'),'\n')"

# Explanation {#explanation .unnumbered}

The command uses Rscript to execute R code that reads a CSV file
specified as argument, computes basic statistics (rows, columns, cells),
gets file size via file.size(), and reports object memory usage via
object.size().

# Tags {#tags .unnumbered}

rscript, csv, statistics, data-analysis, memory

# Dependencies {#dependencies .unnumbered}

r-base-core

# Arguments {#arguments .unnumbered}

1.  **CSV_FILE** (Required): CSV file to analyze

# Examples {#examples .unnumbered}

1.  `Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop(’Need filename’);df<-read.csv(args[1]);cat(’Rows:’,nrow(df),’Cols:’,ncol(df),’Cells:’,nrow(df)*ncol(df),’File size:’,file.size(args[1]),’Object size:’,format(object.size(df),units=’auto’),’\{}n’)" data.csv` -
    Analyze data.csv

2.  `Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop(’Need filename’);df<-read.csv(args[1]);cat(’Rows:’,nrow(df),’Cols:’,ncol(df),’Cells:’,nrow(df)*ncol(df),’File size:’,file.size(args[1]),’Object size:’,format(object.size(df),units=’auto’),’\{}n’)" large_dataset.csv 2>/dev/null` -
    Analyze suppressing warnings

# Output {#output .unnumbered}

    Rows: 100 Cols: 10 Cells: 1000 File size: 12345 Object size: 78.2 Kb

# Notes {#notes .unnumbered}

-   Uses read.csv with default settings (header=TRUE,
    stringsAsFactors=FALSE in R\>=4.0)

-   File size reported in bytes

-   Object size includes R overhead

-   For large files, consider adding options(stringsAsFactors=FALSE)

# Warnings {#warnings .unnumbered}

-   May load entire file into memory

-   Very large CSV files could exhaust memory

# See Also {#see-also .unnumbered}

-   tsv-stats

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
