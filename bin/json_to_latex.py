#!/usr/bin/env python3
"""
Convert JSON oneliner entries to LaTeX files.
Traverses the library directory and converts each JSON file to a LaTeX source file,
preserving the directory structure under conversions/library/.
"""

import json
import os
import sys
from pathlib import Path


def escape_latex(text):
    """
    Escape special LaTeX characters in a string.
    """
    if text is None:
        return ""
    # Characters that need escaping in LaTeX (outside of lstlisting)
    # Process backslash first to avoid double-escaping other characters
    text = text.replace("\\", "\\textbackslash{}")
    special_chars = {
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
        "~": "\\textasciitilde{}",
        "^": "\\textasciicircum{}",
    }
    for char, replacement in special_chars.items():
        text = text.replace(char, replacement)
    return text


def escape_latex_for_lstlisting(text):
    """
    Escape special LaTeX characters for use within lstlisting environment.
    lstlisting is a verbatim environment, so it handles backslashes
    and most other special characters natively.
    """
    if text is None:
        return ""
    # We do not need to escape anything for lstlisting,
    # it treats content as verbatim.
    return text


def format_list(items):
    """
    Format a list of strings as a comma-separated string, escaped for LaTeX.
    """
    if not items:
        return "None"
    return ", ".join(escape_latex(item) for item in items)


def format_object_list(items, key1, key2=None):
    """
    Format a list of objects, extracting key1 and optionally key2.
    """
    if not items:
        return "None"
    if key2 is None:
        return ", ".join(escape_latex(item[key1]) for item in items if key1 in item)
    else:
        return ", ".join(
            f"{escape_latex(item[key1])}: {escape_latex(item[key2])}"
            for item in items
            if key1 in item and key2 in item
        )


def format_examples(examples):
    """
    Format examples as an enumerated list in LaTeX.
    """
    if not examples:
        return "None"
    result = "\\begin{enumerate}\n"
    for ex in examples:
        cmd = escape_latex(ex.get("command", ""))
        desc = escape_latex(ex.get("description", ""))
        result += f"  \\item \\texttt{{{cmd}}} - {desc}\n"
    result += "\\end{enumerate}"
    return result


def format_string_array(array):
    """
    Format an array of strings as an itemized list in LaTeX.
    """
    if not array:
        return "None"
    result = "\\begin{itemize}\n"
    for item in array:
        result += f"  \\item {escape_latex(item)}\n"
    result += "\\end{itemize}"
    return result


def json_to_latex(data):
    """
    Convert a JSON oneliner entry to a LaTeX string.
    """
    # Extract fields with defaults for optional ones
    title = data.get("title", "Untitled")
    language = data.get("language", "unknown")
    category = data.get("category", "uncategorized")
    command = data.get("command", "")
    description = data.get("description", "No description provided.")
    explanation = data.get("explanation", "No detailed explanation provided.")
    tags = data.get("tags", [])
    author = data.get("author", "Unknown")
    created_at = data.get("created_at", "2026-01-01")
    updated_at = data.get("updated_at", created_at)
    safety = data.get("safety", "safe")
    shell = data.get("shell", "not-applicable")
    platforms = data.get("platforms", [])
    dependencies = data.get("dependencies", [])
    arguments = data.get("arguments", [])
    examples = data.get("examples", [])
    output = data.get("output", "No example output provided.")
    notes = data.get("notes", [])
    warnings = data.get("warnings", [])
    see_also = data.get("see_also", [])
    status = data.get("status", "draft")

    latex = "\\documentclass{article}\n"
    latex += "\\usepackage[utf8]{inputenc}\n"
    latex += "\\usepackage{hyperref}\n"
    latex += "\\usepackage{listings}\n"
    latex += "\\usepackage{xcolor}\n"
    latex += "\\usepackage{enumitem}\n\n"
    latex += "\\lstset{\n"
    latex += "    basicstyle=\\ttfamily\\small,\n"
    latex += "    breaklines=true,\n"
    latex += "    frame=single,\n"
    latex += "    backgroundcolor=\\color{gray!5},\n"
    latex += "}\n\n"
    latex += "\\title{" + escape_latex(title) + "}\n"
    latex += "\\author{" + escape_latex(author) + "}\n"
    latex += "\\date{" + escape_latex(created_at) + "}\n\n"
    latex += "\\begin{document}\n\n"
    latex += "\\section*{" + escape_latex(title) + "}\n"
    latex += (
        "\\textbf{Author:} "
        + escape_latex(author)
        + " \\hfill \\textbf{Date:} "
        + escape_latex(created_at)
        + "\n\n"
    )
    latex += "\\noindent " + escape_latex(description) + "\n\n"
    latex += "\\section*{Language}\n" + escape_latex(language) + "\n\n"
    latex += "\\section*{Category}\n" + escape_latex(category) + "\n\n"
    latex += (
        "\\section*{Command}\n\\begin{lstlisting}\n"
        + escape_latex_for_lstlisting(command)
        + "\n\\end{lstlisting}\n\n"
    )
    latex += "\\section*{Explanation}\n" + escape_latex(explanation) + "\n\n"
    latex += "\\section*{Tags}\n" + format_list(tags) + "\n\n"
    latex += "\\section*{Dependencies}\n" + format_list(dependencies) + "\n\n"
    latex += "\n\\section*{Arguments}\n"
    if arguments:
        latex += "\\begin{enumerate}\n"
        for arg in arguments:
            name = escape_latex(arg.get("name", ""))
            desc = escape_latex(arg.get("description", ""))
            required = "Required" if arg.get("required", False) else "Optional"
            default = arg.get("default", "None")
            if default is not None:
                default_str = escape_latex(str(default))
            else:
                default_str = "None"
            latex += f"  \\item \\textbf{{{name}}} ({required}): {desc}"
            if default_str != "None":
                latex += f" \\\\ Default: {default_str}"
            latex += "\n"
        latex += "\\end{enumerate}\n"
    else:
        latex += "None\n"
    latex += "\n\\section*{Examples}\n" + format_examples(examples) + "\n"
    latex += (
        "\n\\section*{Output}\n\\begin{lstlisting}\n" + output + "\n\\end{lstlisting}\n"
    )
    latex += "\n\\section*{Notes}\n" + format_string_array(notes) + "\n"
    latex += "\n\\section*{Warnings}\n" + format_string_array(warnings) + "\n"
    latex += "\n\\section*{See Also}\n" + format_string_array(see_also) + "\n"
    latex += "\n\\section*{Status}\n" + escape_latex(status) + "\n"
    latex += "\n\\section*{Safety}\n" + escape_latex(safety) + "\n"
    latex += "\n\\section*{Shell}\n" + escape_latex(shell) + "\n"
    latex += "\n\\section*{Platforms}\n" + format_list(platforms) + "\n"
    latex += "\n\\section*{Created At}\n" + escape_latex(created_at) + "\n"
    latex += "\n\\section*{Updated At}\n" + escape_latex(updated_at) + "\n"
    latex += "\n\\end{document}\n"
    return latex


def main():
    """
    Main function: traverse library and convert JSON to LaTeX.
    """
    repo_root = Path(__file__).parent.parent
    library_dir = repo_root / "library"
    conversions_dir = repo_root / "conversions" / "library"

    if not library_dir.exists():
        print(f"Error: Library directory not found at {library_dir}")
        sys.exit(1)

    # Create conversions directory if it doesn't exist
    conversions_dir.mkdir(parents=True, exist_ok=True)

    converted_count = 0
    error_count = 0

    # Walk through library directory
    for root, dirs, files in os.walk(library_dir):
        for file in files:
            if file.lower().endswith(".json"):
                json_path = Path(root) / file
                # Compute relative path from library_dir
                relative_path = json_path.relative_to(library_dir)
                # Change extension to .tex
                tex_path = conversions_dir / relative_path.with_suffix(".tex")
                # Create parent directories if needed
                tex_path.parent.mkdir(parents=True, exist_ok=True)

                try:
                    # Read JSON file
                    with open(json_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    # Convert to LaTeX
                    latex_content = json_to_latex(data)

                    # Write LaTeX file
                    with open(tex_path, "w", encoding="utf-8") as f:
                        f.write(latex_content)

                    print(f"Converted: {json_path} -> {tex_path}")
                    converted_count += 1
                except Exception as e:
                    print(f"Error processing {json_path}: {e}", file=sys.stderr)
                    error_count += 1

    print(
        f"\nConversion complete: {converted_count} files converted, {error_count} errors."
    )
    if error_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
