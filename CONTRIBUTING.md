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

**Prerequisites:**
- **Git** - [Download](https://git-scm.com/downloads)
- **Docker and Docker Compose** - [Download](https://docs.docker.com/get-docker/)
- **Python 3.7+** - [Download](https://www.python.org/downloads/)
- **pip** (Python package manager, usually included with Python)

**Check if you have the prerequisites:**
```bash
git --version
docker --version
docker-compose --version
python3 --version  # or 'python --version' on Windows
pip3 --version     # or 'pip --version' on Windows
```

**Where to run these commands:**
- **Windows:** Command Prompt, PowerShell, or Git Bash - NOT Python IDLE
- **Mac:** Terminal app
- **Linux:** Any terminal emulator

**Setup steps:**

```bash
# Step 1: Clone your fork
git clone https://github.com/yourusername/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Step 2: Add upstream remote
git remote add upstream https://github.com/mrlt8/docker-wyze-bridge.git

# Step 3: Create a feature branch
git checkout -b feature/your-feature-name

# Step 4: Install Python dependencies
cd app

# On Linux/Mac:
pip3 install -r requirements.txt

# On Windows:
pip install -r requirements.txt

# Step 5: Return to root directory
cd ..
```

**What each tool does:**
- **Git** - Version control, for downloading and managing code
- **Docker** - Container platform, for running the bridge application
- **Python** - Programming language, for running/developing the Python code
- **pip** - Python package installer, for installing dependencies

#### Testing Your Changes

**Where to run these commands:**
- **Windows:** Command Prompt, PowerShell, or Git Bash
- **Mac:** Terminal app
- **Linux:** Terminal emulator

**Testing steps:**

1. **Build the Docker image** locally:
   ```bash
   # Run from the repository root directory
   docker build -t wyze-bridge:test -f docker/Dockerfile .
   ```
   
   **What this does:** Builds a Docker container image with your changes

2. **Run with your cameras**:
   ```bash
   # Replace with your actual Wyze credentials
   docker run --rm -p 5000:5000 \
     -e WYZE_EMAIL=your@email.com \
     -e WYZE_PASSWORD=yourpass \
     -e API_ID=your-api-id \
     -e API_KEY=your-api-key \
     wyze-bridge:test
   ```
   
   **What this does:** Starts the bridge container with your changes
   
   **Access the Web UI:** Open `http://localhost:5000` in your web browser

3. **Verify streams** work for affected cameras:
   - Check the Web UI to see if cameras are discovered
   - Test RTSP stream in VLC: `rtsp://localhost:8554/camera-name`

4. **Check logs** for any errors or warnings:
   ```bash
   # Logs are shown in the terminal where you ran 'docker run'
   # Press Ctrl+C to stop the container
   ```

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

Contributors can help keep the fork updated.

**Where to run these commands:**
- **Windows:** Command Prompt, PowerShell, or Git Bash
- **Mac:** Terminal app
- **Linux:** Terminal emulator

**Sync steps:**

```bash
# Step 1: Fetch upstream changes
git fetch upstream

# Step 2: Merge upstream main into your branch
git merge upstream/main

# Step 3: If there are conflicts, Git will tell you which files
# Open the conflicted files in a text editor and resolve conflicts
# Look for lines with <<<<<<, ======, and >>>>>>
# After resolving, mark as resolved:
git add <resolved-file>

# Step 4: Complete the merge
git commit

# Step 5: Test thoroughly (see Testing Your Changes section)

# Step 6: Push to your fork
git push origin your-branch-name

# Step 7: Submit PR on GitHub
```

**Alternative:** Use the `check-upstream.sh` script in the `scripts/` directory:
```bash
# On Linux/Mac or Git Bash (Windows):
./scripts/check-upstream.sh
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
