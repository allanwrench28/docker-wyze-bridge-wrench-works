# Maintenance Scripts

This directory contains helper scripts for maintaining the fork.

## Available Scripts

### check-upstream.sh

Checks for updates from the upstream repository.

**Usage:**
```bash
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
