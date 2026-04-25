# GOLL - The GULECD-UFPR Oneliner Library

Official repository for **GOLL**, the **Oneliner Library Project** by  
**GULECD-UFPR (Linux and Free Software Users Group - Statistics and Data Science at UFPR)**.

---

## 📌 About the Project

This project aims to build a **collaborative, structured, and validated library of one-liner commands** focused on **Linux and free and open source operating systems**.

Each entry represents a minimal operational unit of knowledge:  
a concise, functional command that is properly documented, categorized, and validated.

Unlike informal collections of commands, this repository is designed as a **structured knowledge base**, enabling:

- deterministic parsing  
- automated validation  
- reproducibility  
- future integration with tools and interfaces  

---

## 🎯 Objectives

- Build a high-quality reference library of useful one-liner commands  
- Promote best practices in Unix-like environments  
- Provide educational material for students and professionals  
- Enable future integration with:
  - web interfaces  
  - CLI tools  
  - semantic search systems  
- Create a reusable structured dataset  

---

## 🧠 Design Principles

Each entry should be:

- **Minimal**: one command per file  
- **Clear**: concise and well-described  
- **Reproducible**: with sufficient context  
- **Structured**: follows a strict schema  
- **Safe**: includes a risk classification  

---

## 📂 Repository Structure

```
schema/
  goll.schema.json

library/
  <language-or-tool>/
    example-entry.json

docs/
  ...

README.md
LICENSE
```


---

## 📄 Schema Overview

Each oneliner is defined as a `.json` file validated against:

```
schema/goll.schema.json
```


### Required Fields

| Field       | Description |
|------------|------------|
| `id`        | Unique identifier (kebab-case) |
| `title`     | Short descriptive title |
| `language`  | Tool, language, or command family |
| `category`  | Functional category |
| `command`   | The one-liner command |
| `description` | Short explanation |
| `tags`      | Array of tags |
| `author`    | Contributor name |
| `safety`    | `safe`, `caution`, or `dangerous` |

### Optional Fields

- `explanation`  
- `created_at`  
- `updated_at`  
- `shell`  
- `platforms`  
- `dependencies`  
- `arguments`  
- `examples`  
- `output`  
- `notes`  
- `warnings` (required if `safety = dangerous`)  
- `see_also`  
- `status`  

---

## ⚠️ Safety Classification

All commands must include a safety level:

| Level       | Meaning |
|------------|--------|
| `safe`      | No side effects |
| `caution`   | May modify system state |
| `dangerous` | Can cause data loss or irreversible changes |

If `dangerous`, the `warnings` field is **mandatory**.

---

## 🤝 How to Contribute

### 1. Clone the Repository

```bash
git clone git@github.com:GUL-Estatistica-e-Ciencia-de-Dados-UFPR/proj-oneliner-library.git
```


---

### 2. Choose a Template

Go to `docs/` and copy a template:

- `commented-full-entry-example.md` → reference documentation with annotations (If you use this as template, remove the comments before submitting)

Or use examples from the repository:

```bash
cp docs/minimal-example.json library/<language-or-tool>/<your-id>.json
```
(Contains only required fields)

or

```bash
cp docs/full-example.json library/<language-or-tool>/<your-id>.json
```
(Contains all fields)


---

### 3. Edit Your Entry

- Replace all fields with your content  
- Follow naming rules:
  - `id`: lowercase kebab-case  
  - `tags`: lowercase kebab-case  
- Keep commands concise and correct  
- Add `warnings` if needed  

---

### 4. Place the File Correctly

Store your file in the appropriate language/tool directory:

```
library/<language-or-tool>/<your-id>.json
```
If your language/tool doesn't exist, create a new directory.

Examples:

```
library/bash/find-large-files.json
library/git/reset-hard-origin.json
```


---

### 5. Commit and Push

```bash
git add .
git commit -m "Add oneliner: find-large-files"
git push
```


---

### 6. Open a Pull Request

Describe:

- what the command does  
- why it is useful  
- any risks or caveats  

---

## ✅ Contribution Guidelines

- One oneliner per file  
- File name must match `id`  
- JSON must be valid (no comments)  
- Do not introduce new schema fields  
- Avoid redundant entries  
- Ensure command correctness  
- Design commands to accept parameters as positional arguments ($1, $2, etc.) rather than hardcoded values  
- Ensure commands work consistently when pasted directly or used in aliases/functions  

---

## 🔍 Validation

All entries are automatically validated via:

- JSON Schema validation  
- Repository rules (unique IDs, structure, etc.)  

Invalid submissions will fail CI checks.

---

## 📚 Examples

See:

- [docs/minimal-validated-example.json](docs/minimal-validated-example.json)
- [docs/full-validated-example.json](docs/full-validated-example.json)
- [docs/commented-full-entry-example.md](docs/commented-full-entry-example.md)

These serve as canonical templates.

---

## 📈 Future Directions

This project is designed to evolve into:

- a searchable web interface  
- a CLI query tool  
- a structured dataset for automation and research  
- integration with documentation systems  

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to:

- use  
- modify  
- distribute  

under the terms of the GPL-3.0 license.

---

## 🌍 Scope

This project is strictly focused on:

- Linux systems  
- Unix-like systems  
- Free and open source operating systems  

It does **not** include proprietary operating systems.

---

## 💡 Final Notes

This is not just a collection of commands.

It is a **structured operational knowledge base**.

Design decisions prioritize:

- long-term scalability  
- machine interoperability  
- educational value  
- community collaboration  

---

## 🚀 Join Us

Contributions from all levels are welcome.

Whether you are:

- a beginner learning shell  
- an advanced user  
- a systems engineer  
- a researcher  

Your contribution helps build a high-quality shared resource.

---
---
---
---

## 💡 Using Oneliners as Aliases

All commands in GOLL are designed to be easily added as aliases in your shell for quick access. This allows you to remember and execute complex operations with simple shortcuts.

### Temporary Aliases (Current Session Only)

To create an alias that lasts only for your current terminal session:

```bash
alias shortname='your-command-here'
```

Example using the system memory report oneliner:
```bash
alias memreport='echo -e "Memory Report:\n$(free -h)\n\nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\n$(ps -eo pid,comm,%mem,rss --sort=-%mem | awk '\''NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\n", $1, $2, $3, $4/1024}''' | head -n 11)"'
```

### Permanent Aliases (Across Sessions)

To make aliases permanent, add them to your shell's configuration file:

#### Bash (~/.bashrc or ~/.bash_profile)
```bash
# Add to ~/.bashrc or ~/.bash_profile
alias memreport='echo -e "Memory Report:\n$(free -h)\n\nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\n$(ps -eo pid,comm,%mem,rss --sort=-%mem | awk '\''NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\n", $1, $2, $3, $4/1024}''' | head -n 11)"'
```
Then reload: `source ~/.bashrc`

#### Zsh (~/.zshrc)
```bash
# Add to ~/.zshrc
alias memreport='echo -e "Memory Report:\n$(free -h)\n\nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\n$(ps -eo pid,comm,%mem,rss --sort=-%mem | awk '\''NR==1 {print $0 " RSS(MB)"}; NR>1 {printf "%s %s %s %.2f\n", $1, $2, $3, $4/1024}''' | head -n 11)"'
```
Then reload: `source ~/.zshrc`

#### Fish (~/.config/fish/config.fish)
```bash
# Add to ~/.config/fish/config.fish
alias memreport="echo -e 'Memory Report:\n(free -h)\n\nTop 10 Memory Consuming Processes (%MEM and RSS in MB):\n(ps -eo pid,comm,%mem,rss --sort=-%mem | awk '\''NR==1 {print \$0 \" RSS(MB)\"}; NR>1 {printf \"%s %s %s %.2f\\n\", \$1, \$2, \$3, \$4/1024}''' | head -n 11)'"
```
Then reload: `source ~/.config/fish/config.fish`

### Tips for Creating Effective Aliases

1. **Choose memorable names**: Use short, intuitive names like `memreport`, `bigfiles`, `gitclean`
2. **Quote properly**: Use quotes around the alias value to prevent premature variable expansion
3. **Escape inner quotes**: When your command contains quotes, escape them appropriately for your shell
4. **Document your aliases**: Consider keeping a personal alias reference file
5. **Start with temporary aliases**: Test them before making them permanent

By using these oneliners as aliases, you can significantly improve your command-line efficiency and have powerful tools readily available at your fingertips.

---