# Fork Overview

## Quick Reference for Maintainers

This document provides a quick overview of this fork and its relationship with upstream.

## What is This Fork?

This is an actively maintained fork of [mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge), which provides WebRTC, RTSP, RTMP, and HLS streaming capabilities for Wyze cameras.

## Why This Fork Exists

- Provide an actively maintained alternative
- Offer enhanced documentation and community support
- Ensure regular upstream synchronization
- Maintain clear contribution pathways
- Document security best practices

## Key Documents

| Document | Purpose | Audience |
|----------|---------|----------|
| [README.md](../README.md) | Main project documentation | All users |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution guidelines | Contributors |
| [MAINTENANCE.md](../MAINTENANCE.md) | Maintenance procedures | Maintainers |
| [SECURITY.md](../SECURITY.md) | Security practices | Users & Maintainers |
| [CHANGELOG.md](../CHANGELOG.md) | Version history | All users |

## Fork vs Upstream

### Similarities
- ✅ Same core functionality
- ✅ Compatible with same cameras
- ✅ Same configuration options
- ✅ Regular synchronization

### Fork-Specific Additions
- 📚 Enhanced documentation
- 🤖 Automated maintenance workflows
- 🔒 Security guidelines
- 🤝 Structured contribution process
- 📋 Issue/PR templates

## Current Status

**Version:** v2.10.3 (synced with upstream)  
**Last Sync:** January 2024  
**Sync Status:** ✅ Up to date  
**Maintenance:** Active

## Quick Commands

### Check for Upstream Updates
```bash
./scripts/check-upstream.sh
```

### Sync with Upstream
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### View Documentation
```bash
# Contribution guidelines
cat CONTRIBUTING.md

# Maintenance procedures
cat MAINTENANCE.md

# Security best practices
cat SECURITY.md
```

## Automated Workflows

### Upstream Check Workflow
- **File:** `.github/workflows/upstream-check.yml`
- **Schedule:** Weekly (Mondays at 9 AM UTC)
- **Purpose:** Checks for upstream updates and creates issues

### Stale Management Workflow
- **File:** `.github/workflows/stale.yml`
- **Schedule:** Daily (1 AM UTC)
- **Purpose:** Marks and closes stale issues/PRs

### Docker Image Build
- **File:** `.github/workflows/docker-image.yml`
- **Trigger:** On release tags
- **Purpose:** Builds and publishes Docker images

## Maintenance Schedule

### Weekly
- Review new issues and PRs
- Check for upstream updates
- Respond to community questions

### Monthly
- Update documentation if needed
- Review open issues for staleness
- Check dependency security

### Quarterly
- Comprehensive testing with cameras
- Review and optimize workflows
- Update support documentation

## Directory Structure

```
.
├── .github/           # GitHub configuration
│   ├── ISSUE_TEMPLATE/  # Issue templates
│   └── workflows/       # GitHub Actions
├── app/               # Main application code
├── docker/            # Docker configurations
├── docs/              # Additional documentation
├── home_assistant/    # Home Assistant addon
├── scripts/           # Maintenance scripts
├── CONTRIBUTING.md    # Contribution guide
├── MAINTENANCE.md     # Maintainer guide
├── SECURITY.md        # Security policy
├── CHANGELOG.md       # Version history
└── README.md          # Main documentation
```

## Important Links

- **Upstream Repository:** https://github.com/mrlt8/docker-wyze-bridge
- **Upstream Wiki:** https://github.com/mrlt8/docker-wyze-bridge/wiki
- **Docker Hub:** https://hub.docker.com/r/mrlt8/wyze-bridge
- **This Fork:** https://github.com/allanwrench28/docker-wyze-bridge-wrench-works

## Common Maintenance Tasks

### Reviewing Issues

1. Check if it exists upstream
2. Determine severity and priority
3. Label appropriately
4. Respond within 48 hours
5. Link to relevant documentation

### Reviewing Pull Requests

1. Run tests locally if possible
2. Check for security concerns
3. Verify documentation updates
4. Ensure code style matches
5. Provide constructive feedback

### Syncing with Upstream

1. Run `./scripts/check-upstream.sh`
2. Review changes: `git log HEAD..upstream/main`
3. Test locally before merging
4. Update version in app/.env
5. Update CHANGELOG.md
6. Create release if needed

## Support Channels

- **Issues:** Bug reports and feature requests
- **Discussions:** Questions and community support
- **Security:** Private vulnerability reporting
- **Upstream:** General Wyze bridge questions

## Version Strategy

- **Upstream syncs:** Use upstream version (e.g., v2.10.3)
- **Fork patches:** Add suffix (e.g., v2.10.3-wrench.1)
- **Breaking changes:** Clearly document in CHANGELOG

## Testing Checklist

Before releasing:
- [ ] Docker build succeeds
- [ ] Image size is reasonable
- [ ] WebUI loads correctly
- [ ] Camera connections work
- [ ] Streams are accessible
- [ ] Documentation is accurate
- [ ] No sensitive data in commits

## Getting Help

If you need help with maintenance:

1. Check [MAINTENANCE.md](../MAINTENANCE.md)
2. Review closed issues for similar situations
3. Check upstream wiki and issues
4. Ask in discussions

## Philosophy

This fork aims to:
- **Stay Aligned:** Minimize divergence from upstream
- **Add Value:** Enhance through documentation and support
- **Be Responsive:** Address community needs promptly
- **Maintain Quality:** Keep high standards for code and docs
- **Give Credit:** Acknowledge all contributors

## Contributing to Upstream

Major features should ideally be contributed to upstream:

1. Check upstream contribution guidelines
2. Open issue to discuss feature
3. Submit PR to upstream
4. Sync to fork after upstream merge

This benefits the entire Wyze bridge community!

---

**Thank you for maintaining this fork and supporting the Wyze camera community!** 🚀
