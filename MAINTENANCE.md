# Maintenance Guide

This document outlines the maintenance procedures for keeping this fork of docker-wyze-bridge active and useful.

## Maintenance Philosophy

This fork aims to:
1. **Stay Current**: Regularly sync with upstream releases
2. **Be Responsive**: Address issues and PRs promptly
3. **Document Well**: Keep documentation accurate and helpful
4. **Test Thoroughly**: Validate changes before release
5. **Communicate Clearly**: Keep users informed of changes

## Regular Maintenance Tasks

### Weekly Tasks

- [ ] Check for new upstream releases
- [ ] Review and respond to new issues
- [ ] Monitor discussion activity
- [ ] Check Docker Hub for image pull statistics

### Monthly Tasks

- [ ] Review and update documentation
- [ ] Check for security vulnerabilities in dependencies
- [ ] Test with latest camera firmware versions
- [ ] Review and merge community PRs
- [ ] Update supported camera list if needed

### Quarterly Tasks

- [ ] Perform comprehensive testing across camera models
- [ ] Review and optimize Docker image size
- [ ] Update Home Assistant addon if needed
- [ ] Audit and update dependencies
- [ ] Review analytics and user feedback

## Syncing with Upstream

### Checking for Updates

```bash
# Add upstream if not already added
git remote add upstream https://github.com/mrlt8/docker-wyze-bridge.git

# Fetch upstream changes
git fetch upstream

# Check what's new
git log HEAD..upstream/main --oneline

# View detailed changes
git log HEAD..upstream/main --graph --decorate
```

### Merging Upstream Changes

```bash
# Ensure you're on main branch
git checkout main

# Merge upstream changes
git merge upstream/main

# If conflicts occur, resolve them carefully
# Test thoroughly after merging

# Push to origin
git push origin main
```

### After Syncing

1. **Update version references** in documentation if upstream version changed
2. **Test Docker builds** to ensure no breaking changes
3. **Review changelog** and update CHANGELOG.md with fork-specific notes
4. **Test with real cameras** if possible
5. **Update README.md** if new features or cameras are supported
6. **Create a release** if significant changes were merged

## Release Process

### Version Numbering

- Follow upstream version numbers for synced releases
- Use `-wrench.X` suffix for fork-specific releases
  - Example: `v2.10.3-wrench.1` for first fork-specific patch on v2.10.3

### Creating a Release

1. **Ensure all tests pass**
   ```bash
   # Build Docker image
   docker build -t wyze-bridge:test -f docker/Dockerfile .
   
   # Test with your cameras
   # Verify WebUI loads
   # Check streams work
   ```

2. **Update documentation**
   - Update version numbers in README.md
   - Update CHANGELOG.md with release notes
   - Update app/.env if version changed

3. **Create git tag**
   ```bash
   git tag -a v2.10.3 -m "Release v2.10.3 - Synced with upstream"
   git push origin v2.10.3
   ```

4. **Create GitHub release**
   - Go to GitHub Releases
   - Create release from tag
   - Copy changelog content
   - Highlight fork-specific changes if any

5. **Monitor for issues**
   - Watch for issues after release
   - Be ready to hotfix critical bugs
   - Communicate with users about any problems

## Issue Management

### Triaging Issues

1. **Determine if upstream issue**: Check if issue exists upstream
   - If yes, link to upstream issue and monitor it
   - If fixed upstream, sync the fix

2. **Categorize issues**:
   - `bug`: Something isn't working
   - `enhancement`: Feature request
   - `documentation`: Documentation improvements
   - `question`: Support questions
   - `upstream`: Waiting on upstream fix
   - `help-wanted`: Good for community contributions

3. **Set priority**:
   - `critical`: Security issues, data loss, major breakage
   - `high`: Significant functionality broken
   - `medium`: Important but workarounds exist
   - `low`: Minor issues, enhancements

4. **Initial response time goal**: Within 48 hours

### Closing Issues

- Verify fix before closing
- Provide clear explanation
- Reference commits/PRs that fixed it
- Ask reporter to verify if possible

## Pull Request Management

### Review Checklist

- [ ] Code follows project style
- [ ] Changes are well-documented
- [ ] No sensitive data in commits
- [ ] Commits have clear messages
- [ ] PR description explains changes
- [ ] Testing has been done
- [ ] Documentation updated if needed
- [ ] No merge conflicts

### Merging PRs

1. **Test the changes** locally if possible
2. **Provide feedback** constructively
3. **Request changes** if needed
4. **Merge when ready** using squash or regular merge
5. **Thank the contributor**
6. **Close related issues** if PR fixes them

## Security

### Handling Security Issues

1. **Do not discuss publicly** until fixed
2. **Acknowledge receipt** within 24 hours
3. **Assess severity** and impact
4. **Develop fix** quickly for critical issues
5. **Test thoroughly** before release
6. **Release patch** as soon as ready
7. **Publish security advisory** after fix is available
8. **Credit reporter** (if they want credit)

### Dependency Updates

```bash
# Check for outdated dependencies
cd app
pip list --outdated

# Update requirements.txt carefully
# Test after updating
# Document any breaking changes
```

## Docker Image Maintenance

### Building Multi-Architecture Images

```bash
# Build for multiple architectures
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 \
  -t yourusername/wyze-bridge:latest \
  -f docker/Dockerfile .
```

### Testing Images

Test on different platforms:
- x86_64 (amd64)
- ARM64 (Raspberry Pi 4, Apple Silicon)
- ARM32v7 (Raspberry Pi 3)

## Documentation Maintenance

### Regular Reviews

- Check for broken links
- Update screenshots if UI changed
- Verify examples still work
- Update camera compatibility list
- Review and improve troubleshooting sections

### Documentation Standards

- Use clear, simple language
- Provide examples for complex topics
- Keep formatting consistent
- Update table of contents when adding sections
- Link to relevant wiki pages

## Community Engagement

### Communication Channels

- GitHub Issues: Primary support and bug reports
- GitHub Discussions: Community questions and feature ideas
- Pull Requests: Code contributions

### Responding to Community

- Be friendly and professional
- Acknowledge reports quickly
- Provide helpful information
- Ask for clarification when needed
- Thank contributors

## Monitoring

### What to Monitor

- Issue creation rate
- PR submission rate
- Docker image pulls
- Build status
- User feedback
- Upstream activity

### Tools

- GitHub notifications
- GitHub insights
- Docker Hub analytics
- GitHub Actions status

## Automation Opportunities

### GitHub Actions

Consider automating:
- Dependency updates (Dependabot)
- Docker image builds on release
- Upstream sync checking
- Stale issue management
- Testing on PR submission

### Scripts to Consider

- Upstream version checker
- Changelog generator
- Release automation
- Camera compatibility checker

## Maintainer Responsibilities

### Primary Maintainer

- Overall project direction
- Release decisions
- Major architecture changes
- Community management
- Security issues

### Contributors

- Issue triage and response
- PR review and merge
- Documentation updates
- Testing
- Community support

## Handling Maintainer Changes

### Offboarding

1. Document current state
2. Transfer knowledge
3. Update permissions
4. Announce changes
5. Ensure continuity

### Onboarding New Maintainers

1. Grant repository access
2. Share this document
3. Explain processes
4. Introduce to community
5. Start with supervised tasks

## Resources

- [Upstream Repository](https://github.com/mrlt8/docker-wyze-bridge)
- [Upstream Wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki)
- [Docker Hub](https://hub.docker.com/r/mrlt8/wyze-bridge)
- [Home Assistant Addon](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant)

## Conclusion

Maintaining this fork requires regular attention but doesn't need to be overwhelming. The key is consistency and communication. When in doubt, refer to upstream for guidance and maintain alignment with their approach.

Thank you for maintaining this project for the community! 🛠️
