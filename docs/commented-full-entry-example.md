# GULECD-UFPR Oneliner Library  
## Example Entry Documentation

This document provides a **fully annotated example** of a valid oneliner entry using a JSONC-style format (JSON with comments).

> IMPORTANT:  
> - This format is for documentation purposes only  
> - Actual submissions **must be strict JSON** (no comments)

---
### Required Fields
- `id`
- `title`
- `language`
- `category`
- `command`
- `description`
- `tags`
- `author`
- `safety`

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
- `warnings` (required if `safety` = `dangerous`)
- `see_also`
- `status`

### Contribution Notes
- Use lowercase kebab-case for `id` and `tags`
- Keep commands concise and reproducible
- Always classify safety correctly
- Prefer clarity over cleverness



---

## Example (JSONC)

```jsonc
{
  // REQUIRED
  // Unique machine-readable identifier (kebab-case, lowercase)
  "id": "find-large-files-recursive",

  // REQUIRED
  // Short descriptive title
  "title": "Find files larger than 100 MB recursively",

  // REQUIRED
  // Language, tool, or command family (free-form)
  "language": "find",

  // REQUIRED
  // Functional category (free-form, but follow recommended conventions)
  "category": "filesystem",

  // REQUIRED
  // The actual one-liner command
  "command": "find . -type f -size +100M",

  // REQUIRED
  // Short explanation of what the command does
  "description": "Recursively finds all regular files larger than 100 MB under the current directory.",

  // OPTIONAL
  // Detailed explanation of how the command works
  "explanation": "The command traverses directories recursively, filters regular files, and selects files larger than 100 MB.",

  // REQUIRED
  // Tags for search and filtering (kebab-case)
  "tags": [
    "find",
    "filesystem",
    "disk-usage",
    "large-files"
  ],

  // REQUIRED
  // Author or contributor name
  "author": "marcos",

  // OPTIONAL
  // Creation date (ISO format)
  "created_at": "2026-04-21",

  // OPTIONAL
  // Last update date (ISO format)
  "updated_at": "2026-04-21",

  // REQUIRED
  // Safety classification: safe | caution | dangerous
  "safety": "safe",

  // OPTIONAL
  // Shell/environment
  "shell": "posix",

  // OPTIONAL
  // Supported platforms (FOSS only)
  "platforms": [
    "linux",
    "gnu-linux",
    "freebsd"
  ],

  // OPTIONAL
  // Required external tools
  "dependencies": [
    "findutils"
  ],

  // OPTIONAL
  // Argument descriptions
  "arguments": [
    {
      "name": "PATH",
      "description": "Directory to search",
      "required": false,
      "default": "."
    }
  ],

  // OPTIONAL
  // Usage examples
  "examples": [
    {
      "command": "find /var -type f -size +500M",
      "description": "Find large files in /var"
    }
  ],

  // OPTIONAL
  // Example output
  "output": "./large-file.iso\n./backup.tar.gz",

  // OPTIONAL
  // Additional notes
  "notes": [
    "May be slow on large filesystems"
  ],

  // OPTIONAL (REQUIRED if safety = dangerous)
  "warnings": [
    "Performance may degrade on network filesystems"
  ],

  // OPTIONAL
  // Related entries
  "see_also": [
    "du-sort-largest-directories"
  ],

  // OPTIONAL
  // Editorial status
  "status": "reviewed"
}