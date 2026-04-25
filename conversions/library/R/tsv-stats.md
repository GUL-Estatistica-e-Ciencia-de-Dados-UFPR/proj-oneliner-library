# Load TSV file and print dataset statistics using R {#load-tsv-file-and-print-dataset-statistics-using-r .unnumbered}

**Author:** marcos **Date:** 2026-04-25

Loads a TSV (tab-separated) file using R's read.delim and prints rows,
columns, total cells, file size, and object memory usage.

# Language {#language .unnumbered}

rscript

# Category {#category .unnumbered}

data-processing

# Command {#command .unnumbered}

    Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop('Need filename');df<-read.delim(args[1]);cat('Rows:',nrow(df),'Cols:',ncol(df),'Cells:',nrow(df)*ncol(df),'File size:',file.size(args[1]),'Object size:',format(object.size(df),units='auto'),'\n')"

# Explanation {#explanation .unnumbered}

The command uses Rscript to execute R code that reads a TSV file
specified as argument, computes basic statistics (rows, columns, cells),
gets file size via file.size(), and reports object memory usage via
object.size(). read.delim uses tab as separator by default.

# Tags {#tags .unnumbered}

rscript, tsv, statistics, data-analysis, memory

# Dependencies {#dependencies .unnumbered}

r-base-core

# Arguments {#arguments .unnumbered}

1.  **TSV_FILE** (Required): TSV (tab-separated) file to analyze

# Examples {#examples .unnumbered}

1.  `Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop(’Need filename’);df<-read.delim(args[1]);cat(’Rows:’,nrow(df),’Cols:’,ncol(df),’Cells:’,nrow(df)*ncol(df),’File size:’,file.size(args[1]),’Object size:’,format(object.size(df),units=’auto’),’\{}n’)" data.tsv` -
    Analyze data.tsv

2.  `Rscript -e "args<-commandArgs(trailingOnly=TRUE);if(length(args)<1)stop(’Need filename’);df<-read.delim(args[1]);cat(’Rows:’,nrow(df),’Cols:’,ncol(df),’Cells:’,nrow(df)*ncol(df),’File size:’,file.size(args[1]),’Object size:’,format(object.size(df),units=’auto’),’\{}n’)" large_dataset.tsv 2>/dev/null` -
    Analyze suppressing warnings

# Output {#output .unnumbered}

    Rows: 100 Cols: 10 Cells: 1000 File size: 12345 Object size: 78.2 Kb

# Notes {#notes .unnumbered}

-   Uses read.delim with default settings (header=TRUE, sep='\\{}t',
    stringsAsFactors=FALSE in R\>=4.0)

-   File size reported in bytes

-   Object size includes R overhead

-   For large files, consider adding options(stringsAsFactors=FALSE)

# Warnings {#warnings .unnumbered}

-   May load entire file into memory

-   Very large TSV files could exhaust memory

# See Also {#see-also .unnumbered}

-   csv-stats

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
