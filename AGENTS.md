# GOLL Agent Instructions

This document provides comprehensive instructions for AI coding agents to create complete and validated GOLL (GULECD-UFPR Oneliner Library) entries that comply with all repository requirements.

## Overview

GOLL entries are structured JSON files that represent one-liner commands with detailed documentation. Each entry must:
1. Follow the JSON schema defined in `schema/goll.schema.json`
2. Include all required fields
3. Pass validation checks
4. Be placed in the correct directory structure

### Critical Command Design Rules

Every command **MUST** satisfy these two requirements simultaneously:

1. **Can be pasted directly on the terminal and executed** — the user copies the command string and runs it as-is
2. **Can be wrapped in a shell alias** — the same command string must work inside `alias name='...'`

To satisfy both requirements, follow these design patterns:

#### Parameters Must Come AFTER the Command

The user should NEVER need to edit or modify parameters embedded inside the command string. All variable inputs must be passed as arguments at the end. The expected invocation pattern is:

```
<command> <param1> <param2> <param3> ...
```

NOT:

```
<command> <param1> embedded-in-middle <param2>
```

**Good example** (parameters at end, using `bash -c` wrapper):
```bash
bash -c 'dir=$1; days=$2; shift 2; find "$dir" -type f -mtime +"$days" -delete "$@"' _ /var/log 30
```

**Good example** (simple positional args, tool natively supports trailing args):
```bash
psql -U "$1" -d "$2" -h "$3" -c "VACUUM (VERBOSE, ANALYZE);"
```

**Bad example** (user must edit path and days embedded in middle of command):
```bash
find /var/log -type f -mtime +30 -delete
```

#### Using `bash -c` for Complex Commands

The `bash -c` pattern is the most flexible way to handle commands with multiple arguments:

```bash
bash -c 'old=$1; new=$2; shift 2; find "$@" -type f -exec sed -i "s#$old#$new#g" {} +' _ 'search' 'replace' file.txt
```

This can be turned into an alias:
```bash
alias repl="bash -c 'old=\$1; new=\$2; shift 2; find \"\$@\" -type f -exec sed -i \"s#\$old#\$new#g\" {} +' _"
# Usage: repl 'old-text' 'new-text' *.txt
```

#### Using Shell Functions for Aliases

For more complex commands, consider documenting them as functions:

```bash
# Define the function
vacuum_pg() { PGPASSWORD="$2" psql -U "$1" -d "$3" -h "$4" -c "VACUUM (VERBOSE, ANALYZE);"; }

# Usage
vacuum_pg postgres secret123 mydb localhost
```

### Caution: JSON Escaping

The `command` field is a JSON string, so special characters MUST be properly escaped or the file will fail JSON validation:

| Character | JSON Escape Required |
|-----------|---------------------|
| Backslash `\` | `\\` → `\\\\` (double each backslash) |
| Double quote `"` | `\"` |
| Newline | `\n` |
| Tab | `\t` |

Always validate after writing:
```bash
python3 -m json.tool library/{language}/{id}.json
```

## Entry Creation Process

### 1. Understanding the Schema

Before creating any entry, familiarize yourself with the GOLL schema:
- **Required fields**: `id`, `title`, `language`, `category`, `command`, `description`, `tags`, `author`, `safety`
- **Safety levels**: `safe`, `caution`, or `dangerous`
- **Naming conventions**: Use kebab-case for `id` and `tags`

### 2. Directory Structure

Place entries in the appropriate language/tool directory:
```
library/
  bash/
  git/
  python/
  R/
  postgresql/
  # etc.
```

### 3. Entry Creation Steps

#### Step 1: Choose a Category and Language
Select an appropriate functional category from the schema examples:
- `filesystem`, `text-processing`, `system-administration`, `data-processing`, etc.
- Language should match the tool family (bash, git, python, etc.)

#### Step 2: Define the Command
Create a concise, functional one-liner that:
- Performs a single, well-defined operation
- Is reproducible across systems
- Follows best practices for its domain

#### Step 3: Set Safety Classification
Classify the command appropriately:
- `safe`: No side effects or system modifications
- `caution`: May modify system state
- `dangerous`: Can cause data loss or irreversible changes (requires warnings)

#### Step 4: Write Required Fields
Ensure all required fields are present:
- `id`: Unique kebab-case identifier
- `title`: Clear, descriptive title
- `language`: Tool/language family
- `category`: Functional grouping
- `command`: The actual one-liner
- `description`: Brief explanation of what it does
- `tags`: Searchable keywords (kebab-case)
- `author`: Your identifier
- `safety`: Risk classification

#### Step 5: Add Optional Fields
Include relevant optional fields:
- `explanation`: Detailed operational description
- `arguments`: Parameter documentation
- `examples`: Usage examples
- `dependencies`: Required tools
- `platforms`: Supported operating systems
- `warnings`: Risk disclosures (required for dangerous commands)

### 4. Validation Requirements

#### JSON Schema Validation
Entries must pass validation against `schema/goll.schema.json`:
- All required fields present
- Field values match schema patterns
- String lengths within limits
- Enum values are valid

#### Content Validation
- `id` must be unique within the library
- `command` must be executable in target environments
- `dependencies` must be accurate
- `examples` must be functional

### 5. Best Practices

#### Command Design
- Keep commands concise and single-purpose
- Use standard tools available on FOSS systems
- Design for reproducibility
- Handle errors gracefully where possible

#### Documentation Quality
- Write clear, accurate descriptions
- Include relevant usage examples
- Document platform-specific behavior
- Disclose all risks appropriately

#### Cross-Platform Compatibility
- Test commands on target platforms
- Document platform-specific dependencies
- Use POSIX-compliant syntax when possible
- Specify supported environments explicitly

### 6. Common Patterns

#### File Processing
```bash
find . -type f -name "*.txt" -exec command {} \\;
```

#### Text Processing
```bash
command | awk '{print $1}' | sort | uniq -c
```

#### System Commands
```bash
sudo command && echo "Success" || echo "Failed"
```

### 7. Quality Assurance

#### Pre-Submission Checklist
- [ ] Entry passes JSON schema validation
- [ ] All required fields are present and valid
- [ ] Command executes successfully in test environment
- [ ] Examples are accurate and functional
- [ ] Safety classification is appropriate
- [ ] Dependencies are correctly listed
- [ ] Tags are relevant and in kebab-case
- [ ] ID is unique and descriptive

#### Post-Submission Verification
- [ ] Entry appears in validation reports
- [ ] Command functions as documented
- [ ] Examples produce expected results
- [ ] Cross-platform compatibility verified

### 8. Troubleshooting

#### Common Issues
1. **Validation failures**: Check schema compliance with `schema/goll.schema.json`
2. **Command errors**: Verify syntax and dependencies
3. **Platform issues**: Test on target systems
4. **ID conflicts**: Ensure unique identifier

#### Validation Commands
```bash
# Check JSON syntax
python3 -m json.tool entry.json

# Run repository validation
python3 bin/validate-entries.py
```

### 9. Repository Integration

#### File Placement
Place entries in the appropriate directory:
```
library/{language}/{id}.json
```

#### Git Workflow
1. Create feature branch
2. Add entry file
3. Validate with `bin/validate-entries.py`
4. Commit with descriptive message
5. Push and create pull request

### 10. Example Entry Structure

Refer to `docs/full-validated-example.json` for a complete example:
```json
{
  "id": "find-large-files-recursive",
  "title": "Find files larger than 100 MB recursively",
  "language": "find",
  "category": "filesystem",
  "command": "find . -type f -size +100M",
  "description": "Recursively finds all regular files larger than 100 MB under the current directory.",
  "tags": ["find", "filesystem", "disk-usage", "large-files"],
  "author": "author-name",
  "safety": "safe"
}
```

### 11. Agent-Specific Guidelines

#### Consistency
- Follow existing naming conventions
- Match documentation style of other entries
- Use consistent terminology

#### Completeness
- Document all edge cases
- Include platform-specific notes
- Provide comprehensive examples

#### Accuracy
- Verify all technical details
- Test commands before submission
- Cross-reference dependencies

### 12. Final Validation

Before submitting any entry:
1. Validate JSON syntax
2. Check schema compliance
3. Test command functionality
4. Verify all examples
5. Confirm platform support
6. Ensure unique ID
7. Review safety classification
8. Validate all links and references

This comprehensive guide ensures all AI agents can create high-quality, validated GOLL entries that contribute meaningfully to the library while maintaining consistency and quality standards.