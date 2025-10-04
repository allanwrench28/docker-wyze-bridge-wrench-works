# Changelog

All notable changes specific to this fork will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

For upstream changes, see the [upstream releases](https://github.com/mrlt8/docker-wyze-bridge/releases).

## [Unreleased]

### Fork Improvements
- Added CONTRIBUTING.md with contribution guidelines
- Added MAINTENANCE.md with maintainer procedures
- Added SECURITY.md with security best practices
- Added CHANGELOG.md for tracking fork changes
- Enhanced documentation for fork maintenance

## [2.10.3] - 2024-01-XX

### Synced with Upstream
- Synced with upstream v2.10.3 release
- Includes all upstream features and fixes from v2.10.3

### Upstream Features (v2.10.3)
- FIX: Increased `MTX_WRITEQUEUESIZE` to prevent issues with higher bitrates
- FIX: Restart RTMP livestream on fail (#1333)
- FIX: Restore user data on bridge restart (#1334)
- NEW: `SNAPSHOT_KEEP` Option to delete old snapshots
- NEW: `RESTREAMIO` option for livestreaming via restream.io

For complete upstream changelog, see: https://github.com/mrlt8/docker-wyze-bridge/releases/tag/v2.10.3

## Fork Information

### About This Fork

This fork (docker-wyze-bridge-wrench-works) is maintained to:
1. Stay synchronized with the excellent upstream project
2. Provide a maintained alternative with clear contribution paths
3. Document best practices for deployment and security
4. Support the community with responsive maintenance

### Versioning Strategy

- **Upstream Synced Releases**: Use upstream version number (e.g., v2.10.3)
- **Fork-Specific Patches**: Add `-wrench.X` suffix (e.g., v2.10.3-wrench.1)
- **Breaking Changes**: Documented in release notes

### How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting issues
- Suggesting features
- Submitting pull requests
- Development setup

### Maintenance Schedule

- **Weekly**: Check for upstream updates
- **Monthly**: Review issues and PRs
- **Quarterly**: Comprehensive testing and documentation review

See [MAINTENANCE.md](MAINTENANCE.md) for detailed maintenance procedures.

### Relationship with Upstream

This fork maintains close alignment with [mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge):
- Regular syncing with upstream releases
- Major contributions should go to upstream first
- Fork-specific features are clearly documented
- We avoid unnecessary divergence

### Support

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Security**: See [SECURITY.md](SECURITY.md) for security reporting
- **Documentation**: Check README.md and upstream wiki
- **Community**: Engage respectfully in discussions

## Previous Upstream Versions

### [2.10.2] - Upstream Release
- FIX: day/night FPS slowdown for V4 cameras (#1287)
- NEW: Update battery level in WebUI

### [2.10.0/2.10.1] - Upstream Release
- FIXED: Could not disable `WB_AUTH` if `WB_API` is set (#1304)
- NEW: WebUI Authentication improvements
- NEW: `STREAM_AUTH` option for multiple users and paths
- NEW: Recording via MediaMTX with option to delete older clips

For complete history, see [upstream releases](https://github.com/mrlt8/docker-wyze-bridge/releases).

---

## Legend

Types of changes:
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

Scopes:
- **Upstream**: Changes from upstream repository
- **Fork**: Changes specific to this fork
- **Docs**: Documentation changes
- **Build**: Build system changes
- **Tests**: Testing changes

---

**Note**: This fork aims to remain compatible with upstream. Most changes come from upstream, with this changelog highlighting fork-specific additions and maintenance activities.
