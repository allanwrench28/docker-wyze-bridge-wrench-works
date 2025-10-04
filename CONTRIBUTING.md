# Contributing to docker-wyze-bridge-wrench-works

Thank you for your interest in contributing to this fork of the Wyze Docker Bridge project! This document provides guidelines for contributing to the project.

## About This Fork

This is an actively maintained fork of [mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge). We aim to:

- Stay synchronized with upstream improvements
- Address community issues promptly
- Improve documentation and user experience
- Test and validate new camera models
- Provide additional features when beneficial

## How to Contribute

### Reporting Issues

Before creating an issue, please:

1. **Check upstream first**: Many issues may already be addressed in the [upstream repository](https://github.com/mrlt8/docker-wyze-bridge/issues)
2. **Search existing issues**: Check if your issue has already been reported
3. **Provide details**: Include your camera model, firmware version, Docker environment, and logs

When reporting an issue, include:
- Camera model and firmware version
- Docker/Home Assistant version
- Complete error messages and logs
- Steps to reproduce the problem
- Your configuration (sanitized of sensitive data)

### Suggesting Enhancements

We welcome suggestions for:
- Documentation improvements
- New camera model support
- Performance optimizations
- Security enhancements
- User experience improvements

Please open an issue to discuss major changes before implementing them.

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Keep changes focused**: One feature or fix per pull request
3. **Test your changes**: Ensure your changes work with various camera models
4. **Update documentation**: Reflect your changes in README.md or other docs
5. **Follow code style**: Match the existing code style in the project
6. **Write clear commit messages**: Explain what and why, not just what

#### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Add upstream remote
git remote add upstream https://github.com/mrlt8/docker-wyze-bridge.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Install dependencies
cd app
pip install -r requirements.txt
```

#### Testing Your Changes

1. **Build the Docker image** locally:
   ```bash
   docker build -t wyze-bridge:test -f docker/Dockerfile .
   ```

2. **Run with your cameras**:
   ```bash
   docker run --rm -p 5000:5000 -e WYZE_EMAIL=your@email.com -e WYZE_PASSWORD=yourpass wyze-bridge:test
   ```

3. **Verify streams** work for affected cameras

4. **Check logs** for any errors or warnings

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Comment complex logic
- Keep functions focused and concise

### Documentation

When updating documentation:
- Use clear, concise language
- Include examples where helpful
- Update table of contents if adding sections
- Test any code examples you provide

## Relationship with Upstream

This fork maintains close alignment with the upstream repository:

- We regularly sync with upstream releases
- Major features should ideally be contributed to upstream first
- Fork-specific features are clearly documented as such
- We avoid diverging from upstream architecture when possible

### Syncing with Upstream

Contributors can help keep the fork updated:

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream main into your branch
git merge upstream/main

# Resolve any conflicts
# Test thoroughly
# Submit PR
```

## Community

- Be respectful and constructive
- Help others when you can
- Share your knowledge and experiences
- Report security issues privately (see SECURITY.md)

## Recognition

Contributors will be recognized in:
- Git commit history
- Release notes for significant contributions
- README.md for major features

## Questions?

If you have questions about contributing:
1. Check existing documentation
2. Search closed issues for similar discussions
3. Open a new issue with the `question` label
4. Check the [upstream wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki) for general information

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

Thank you for helping make this project better for the Wyze camera community! 🚀
