#!/usr/bin/env python3
"""
Consolidate LaTeX files into a single document.
Traverses conversions/library/, creates a consolidated LaTeX document,
and compiles it to PDF, Markdown, and HTML.
"""

import os
import subprocess
import shutil
from pathlib import Path


def extract_body(file_path):
    """Extract the body content of a LaTeX file (between \\maketitle and \\end{document})."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        start = content.find(r"\maketitle")
        if start == -1:
            start = content.find(r"\begin{document}")
            if start == -1:
                return content
            start += len(r"\begin{document}")
        else:
            start += len(r"\maketitle")

        end = content.find(r"\end{document}")
        if end == -1:
            return content[start:].strip()
        return content[start:end].strip()


def consolidate():
    repo_root = Path(__file__).parent.parent
    library_dir = repo_root / "conversions" / "library"
    output_root = repo_root / "conversions" / "consolidated"

    # Environment detail: timestamp
    timestamp = "2026-04-23T08-25-30"
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    consolidated_tex = output_root / "consolidated.tex"

    with open(consolidated_tex, "w", encoding="utf-8") as f:
        # Write preamble
        f.write(r"""\documentclass[openany]{book}
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[margin=1in]{geometry}

\lstset{
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    backgroundcolor=\color{gray!5},
}

\title{Consolidated Oneliner Library}
\author{GULECD-UFPR}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

""")

        # Traverse and append
        for root, dirs, files in os.walk(library_dir):
            rel_path = Path(root).relative_to(library_dir)
            if rel_path != Path("."):
                f.write(f"\n\\chapter{{{rel_path.name.replace('-', ' ').title()}}}\n")

            for file in sorted(files):
                if file.endswith(".tex"):
                    file_path = Path(root) / file
                    f.write(
                        f"\n\\section{{{file_path.stem.replace('-', ' ').title()}}}\n"
                    )
                    f.write(extract_body(file_path))
                    f.write("\n")

        f.write("\n\\end{document}\n")

    print(f"Consolidated LaTeX file created: {consolidated_tex}")

    # Compile
    print("Compiling...")
    # Move tex file to output_dir for compilation
    shutil.copy(consolidated_tex, output_dir / "consolidated.tex")
    os.chdir(output_dir)

    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "consolidated.tex"], check=True
    )
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "consolidated.tex"], check=True
    )

    # Cleanup auxiliary files
    aux_extensions = [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"]
    for ext in aux_extensions:
        aux_file = output_dir / f"consolidated{ext}"
        if aux_file.exists():
            aux_file.unlink()

    subprocess.run(
        ["pandoc", "consolidated.tex", "-t", "markdown", "-o", "consolidated.md"],
        check=True,
    )
    subprocess.run(
        ["pandoc", "consolidated.tex", "-t", "html", "-o", "consolidated.html"],
        check=True,
    )

    print(f"Consolidated files generated in {output_dir}")


if __name__ == "__main__":
    consolidate()
