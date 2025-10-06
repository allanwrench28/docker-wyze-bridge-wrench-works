# Maintenance Scripts

This directory contains helper scripts for maintaining the fork.

## 🔧 Prerequisites for Running Scripts

### Required Software

**Bash Shell (for .sh scripts)**

These scripts are bash shell scripts and must be run in a bash-compatible environment.

**Where to run these scripts:**

- **Linux:** Any terminal (bash is usually the default shell)
  - Open terminal and run: `./scripts/check-upstream.sh`

- **Mac:** Terminal app (bash or zsh both work)
  - Open Terminal (Applications → Utilities → Terminal)
  - Run: `./scripts/check-upstream.sh`

- **Windows:** 
  - ❌ **Cannot run in Command Prompt** - cmd.exe doesn't support bash scripts
  - ❌ **Cannot run in PowerShell** - different scripting language
  - ✅ **Option 1:** Use Git Bash (installed with [Git for Windows](https://git-scm.com/download/win))
    - After installing Git for Windows, right-click in the folder → "Git Bash Here"
    - Run: `./scripts/check-upstream.sh`
  - ✅ **Option 2:** Use Windows Subsystem for Linux (WSL)
    - Install from [Microsoft Store](https://learn.microsoft.com/en-us/windows/wsl/install)
    - Run: `./scripts/check-upstream.sh`

**Required Tools:**
- `git` - [Install Git](https://git-scm.com/downloads)

**Check if you have the required tools:**
```bash
git --version
```

## Available Scripts

### check-upstream.sh

Checks for updates from the upstream repository.

**Prerequisites:** Git installed

**Where to run:** Bash shell (see above for platform-specific instructions)

**Usage:**
```bash
# Navigate to the repository root first
cd /path/to/docker-wyze-bridge-wrench-works

# Run the script
./scripts/check-upstream.sh
```

**What it does:**
- Fetches latest upstream changes
- Compares current fork version with upstream
- Shows number of commits behind
- Provides helpful commands for syncing

**Example output:**
```
🔍 Checking for upstream updates...

📦 Current fork version: v2.10.3
📦 Latest upstream tag: v2.10.4
📊 Commits behind upstream: 5

⚠️  Updates available!

To view changes:
  git log HEAD..upstream/main --oneline
...
```

## For Maintainers

These scripts are designed to help with the tasks outlined in [MAINTENANCE.md](../MAINTENANCE.md).

### Adding New Scripts

When adding new maintenance scripts:
1. Make them executable: `chmod +x scripts/your-script.sh`
2. Add proper error handling (`set -e`)
3. Include helpful comments
4. Document them in this README
5. Keep them simple and focused

### Script Guidelines

- Use bash for portability
- Include usage instructions
- Provide clear output
- Handle errors gracefully
- Document dependencies

## Automation

Some maintenance tasks are automated via GitHub Actions:
- `.github/workflows/upstream-check.yml` - Weekly upstream checks
- `.github/workflows/stale.yml` - Stale issue management

See [MAINTENANCE.md](../MAINTENANCE.md) for more information.
