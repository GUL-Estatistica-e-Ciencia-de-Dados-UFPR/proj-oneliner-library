#!/usr/bin/env python3
"""
Convert LaTeX files to PDF, Markdown, and HTML.
Traverses the conversions/library directory and for each .tex file found,
creates corresponding .pdf, .md, and .html files in the same directory.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_command_exists(command):
    """Check if a command exists in the system PATH."""
    return shutil.which(command) is not None


def run_command(cmd, cwd=None):
    """Run a command and return success status and output."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def convert_latex_to_pdf(tex_file_path):
    """Convert a LaTeX file to PDF using pdflatex."""
    # Get the directory and filename
    tex_dir = tex_file_path.parent
    tex_name = tex_file_path.stem

    # Run pdflatex (run twice to resolve references)
    for i in range(2):
        success, stdout, stderr = run_command(
            f"pdflatex -interaction=nonstopmode -halt-on-error {tex_name}.tex",
            cwd=tex_dir,
        )
        if not success:
            return False, f"pdflatex run {i + 1} failed: {stderr}"

    # Check if PDF was created
    pdf_path = tex_dir / f"{tex_name}.pdf"
    if pdf_path.exists():
        # Remove auxiliary files
        aux_extensions = [
            ".aux",
            ".log",
            ".out",
            ".toc",
            ".lof",
            ".lot",
            ".fls",
            ".fdb_latexmk",
        ]
        for ext in aux_extensions:
            aux_file = tex_dir / f"{tex_name}{ext}"
            if aux_file.exists():
                try:
                    aux_file.unlink()
                except OSError:
                    pass  # Ignore errors in deletion
        return True, f"PDF created: {pdf_path}"
    else:
        return False, "PDF file was not created"


def convert_latex_to_markdown(tex_file_path):
    """Convert a LaTeX file to Markdown using pandoc."""
    md_path = tex_file_path.with_suffix(".md")
    success, stdout, stderr = run_command(
        f"pandoc {tex_file_path} -t markdown -o {md_path}"
    )
    if success and md_path.exists():
        return True, f"Markdown created: {md_path}"
    else:
        return False, f"Markdown conversion failed: {stderr}"


def convert_latex_to_html(tex_file_path):
    """Convert a LaTeX file to HTML using pandoc."""
    html_path = tex_file_path.with_suffix(".html")
    success, stdout, stderr = run_command(
        f"pandoc {tex_file_path} -t html -o {html_path}"
    )
    if success and html_path.exists():
        return True, f"HTML created: {html_path}"
    else:
        return False, f"HTML conversion failed: {stderr}"


def main():
    """Main function: traverse conversions/library and convert LaTeX files."""
    # Get the repository root (parent of bin directory)
    repo_root = Path(__file__).parent.parent
    conversions_dir = repo_root / "conversions" / "library"

    if not conversions_dir.exists():
        print(f"Error: Conversions directory not found at {conversions_dir}")
        sys.exit(1)

    # Check for required tools
    required_tools = ["pdflatex", "pandoc"]
    missing_tools = [tool for tool in required_tools if not check_command_exists(tool)]
    if missing_tools:
        print(f"Error: Missing required tools: {', '.join(missing_tools)}")
        print("Please install them:")
        print("  - pdflatex: part of a TeX distribution (e.g., TeX Live, MikTeX)")
        print("  - pandoc: https://pandoc.org/installing.html")
        sys.exit(1)

    # Walk through conversions directory
    converted_count = 0
    error_count = 0

    for root, dirs, files in os.walk(conversions_dir):
        for file in files:
            if file.lower().endswith(".tex"):
                tex_path = Path(root) / file
                print(f"Processing: {tex_path}")

                # Convert to PDF
                pdf_success, pdf_msg = convert_latex_to_pdf(tex_path)
                if pdf_success:
                    print(f"  ✓ {pdf_msg}")
                else:
                    print(f"  ✗ PDF conversion failed: {pdf_msg}")
                    error_count += 1

                # Convert to Markdown
                md_success, md_msg = convert_latex_to_markdown(tex_path)
                if md_success:
                    print(f"  ✓ {md_msg}")
                else:
                    print(f"  ✗ Markdown conversion failed: {md_msg}")
                    error_count += 1

                # Convert to HTML
                html_success, html_msg = convert_latex_to_html(tex_path)
                if html_success:
                    print(f"  ✓ {html_msg}")
                else:
                    print(f"  ✗ HTML conversion failed: {html_msg}")
                    error_count += 1

                if pdf_success and md_success and html_success:
                    converted_count += 1
                print()  # Empty line for readability

    print(
        f"Conversion complete: {converted_count} files successfully converted, {error_count} errors."
    )
    if error_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
