# 📝 Command Reference Guide

Quick reference for running commands and scripts in this project.

> **💡 Quick Tip:** If you see a command in documentation and don't know where to run it, this guide will help you!

## 🎯 Most Common Questions

**Q: Where do I run `docker-compose up`?**
A: In your Command Prompt (Windows) or Terminal (Mac/Linux) - NOT in Python!

**Q: Where do I run `python3 app/wyzebridge/setup_wizard.py`?**
A: In your Command Prompt (Windows) or Terminal (Mac/Linux) - NOT in Python IDLE!

**Q: Where do I edit the `.env` file?**
A: In any text editor like Notepad, VS Code, nano, or vim - NOT in Command Prompt!

**Q: How do I run `.sh` scripts on Windows?**
A: Use Git Bash (comes with Git for Windows) - regular Command Prompt won't work!

## 🖥️ Where Do I Run Commands?

### Quick Answer

| Your OS | What to Use | How to Open |
|---------|-------------|-------------|
| **Windows** | Command Prompt or PowerShell | Press `Win+R`, type `cmd` or `powershell` |
| **Mac** | Terminal | Applications → Utilities → Terminal |
| **Linux** | Terminal | Usually `Ctrl+Alt+T` |

### What NOT to Use

❌ **Python IDLE** - This is for writing Python code, not running system commands
❌ **Python (command line)** - The Python interpreter is for Python code only
❌ **Text editors** - Notepad, Word, VS Code are for editing files, not running commands
❌ **Web browser** - Commands don't run in browsers

## 📦 Prerequisites Checklist

Before starting, make sure you have these installed:

### Required Tools

| Tool | Check Command | Install Link | Required For |
|------|--------------|--------------|--------------|
| **Docker** | `docker --version` | [Get Docker](https://docs.docker.com/get-docker/) | Running the bridge (REQUIRED) |
| **Docker Compose** | `docker-compose --version` | Included with Docker Desktop | Running the bridge (REQUIRED) |
| **Python 3** | `python3 --version` or `python --version` | [Get Python](https://www.python.org/downloads/) | Setup wizard only (OPTIONAL) |
| **Git** | `git --version` | [Get Git](https://git-scm.com/downloads) | Cloning repo (OPTIONAL) |

### Installation Tips

**Docker:**
- Windows/Mac: Install Docker Desktop (includes Docker Compose)
- Linux: Install Docker Engine, then install Docker Compose separately

**Python:**
- ⚠️ On Windows: Check "Add Python to PATH" during installation!
- Can be skipped if you use manual configuration

**Git:**
- Can be skipped - download ZIP from GitHub instead

## 🔍 Command Type Guide

### Docker Commands

**Where to run:** Command Prompt/Terminal

```bash
# Check Docker is installed
docker --version
docker-compose --version

# Test Docker works
docker run hello-world

# Start the bridge
docker-compose up -d

# Stop the bridge
docker-compose down

# View logs
docker-compose logs -f wyze-bridge

# Restart the bridge
docker-compose restart

# Update the bridge
docker-compose pull
docker-compose up -d

# Remove old images
docker image prune
```

### Python Scripts

**Where to run:** Command Prompt/Terminal (NOT Python IDLE)

```bash
# Run setup wizard (Linux/Mac)
python3 app/wyzebridge/setup_wizard.py

# Run setup wizard (Windows)
python app/wyzebridge/setup_wizard.py

# Check Python version
python3 --version  # Linux/Mac
python --version   # Windows
```

**Common mistake:** Don't try to open `.py` files by double-clicking. Always run from command line!

### Bash Scripts (.sh files)

**Where to run:**
- Linux/Mac: Terminal
- Windows: Git Bash (NOT Command Prompt or PowerShell)

```bash
# Run maintenance script
./scripts/check-upstream.sh

# Make script executable first (if needed)
chmod +x scripts/check-upstream.sh
```

**Windows users:** You need Git Bash or WSL to run `.sh` files!

### Git Commands

**Where to run:** Command Prompt/Terminal (or Git Bash on Windows)

```bash
# Clone repository
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git

# Navigate into directory
cd docker-wyze-bridge-wrench-works

# Check repository status
git status

# Pull latest changes
git pull

# Check Git version
git --version
```

### File Editing

**What to use:**
- **Windows:** Notepad, VS Code, Notepad++
- **Mac:** TextEdit, VS Code, nano
- **Linux:** nano, vim, gedit, VS Code

**Open .env file:**
```bash
# Windows (opens in Notepad)
notepad .env

# Mac (opens in TextEdit)
open -e .env

# Linux (opens in nano)
nano .env
```

## 📋 Common Tasks Step-by-Step

### Task 1: First Time Setup

1. **Open terminal/command prompt**
   - Windows: Press `Win+R`, type `cmd`, press Enter
   - Mac: Open Terminal app
   - Linux: Press `Ctrl+Alt+T`

2. **Clone repository** (or download ZIP)
   ```bash
   git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
   cd docker-wyze-bridge-wrench-works
   ```

3. **Run setup wizard**
   ```bash
   python3 app/wyzebridge/setup_wizard.py  # Linux/Mac
   python app/wyzebridge/setup_wizard.py   # Windows
   ```

4. **Start the bridge**
   ```bash
   docker-compose up -d
   ```

5. **Check it's running**
   - Open browser: http://localhost:5000

### Task 2: Update Configuration

1. **Open .env file in text editor**
   - Windows: Right-click `.env` → Open with → Notepad
   - Mac: Run `open -e .env`
   - Linux: Run `nano .env`

2. **Make your changes** (e.g., add credentials, change settings)

3. **Save the file**

4. **Restart the bridge** (in terminal/command prompt)
   ```bash
   docker-compose restart
   ```

### Task 3: View Logs

**In terminal/command prompt:**
```bash
# View live logs (Ctrl+C to exit)
docker-compose logs -f wyze-bridge

# View last 50 lines
docker-compose logs --tail=50 wyze-bridge

# Save logs to file
docker-compose logs wyze-bridge > logs.txt
```

### Task 4: Stop the Bridge

**In terminal/command prompt:**
```bash
# Stop but keep configuration
docker-compose stop

# Stop and remove containers
docker-compose down
```

### Task 5: Update the Bridge

**In terminal/command prompt:**
```bash
# Pull latest version
docker-compose pull

# Restart with new version
docker-compose up -d

# Clean up old images
docker image prune
```

## 🚨 Troubleshooting

### "Command not found" errors

**Problem:** System can't find the command you're trying to run

**Solutions:**

| Error | Solution |
|-------|----------|
| `docker: command not found` | Install Docker, then restart terminal |
| `python: command not found` | Install Python, or use manual config instead |
| `git: command not found` | Install Git, or download ZIP instead |
| `./script.sh: command not found` | On Windows, use Git Bash not Command Prompt |

### "Permission denied" errors (Linux)

**Problem:** Don't have permission to run Docker

**Solution:**
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker

# Test it works
docker run hello-world
```

### Running commands in wrong place

**Signs you're in the wrong place:**
- See `>>>` prompt (Python interpreter)
- Commands give syntax errors
- Nothing happens when you press Enter

**Solution:**
- Exit Python: Type `exit()` or press `Ctrl+Z` then Enter (Windows) or `Ctrl+D` (Mac/Linux)
- Open a new terminal/command prompt
- Make sure you're in bash/cmd/PowerShell, not Python

## 📚 Related Documentation

- **[Quick Start Guide](QUICK_START.md)** - Get up and running quickly
- **[Complete Setup Guide](SETUP_GUIDE.md)** - Detailed setup instructions
- **[RTSP Setup Guide](RTSP-SETUP.md)** - RTSP-specific configuration
- **[Contributing Guide](CONTRIBUTING.md)** - Development setup

## 💡 Pro Tips

1. **Use Tab completion** - Start typing a file/directory name and press Tab to auto-complete
2. **Copy-paste commands** - Right-click to paste in Command Prompt, `Ctrl+Shift+V` in most terminals
3. **Keep terminal open** - Don't close terminal while following a guide - you'll need it for multiple commands
4. **Navigate with `cd`** - Use `cd` to change directories, `cd ..` to go up one level
5. **Use `ls` or `dir`** - List files in current directory (`ls` on Mac/Linux, `dir` on Windows CMD)
6. **Check your location** - Use `pwd` (Mac/Linux) or `cd` (Windows) to see current directory

## ❓ Still Confused?

If you're still not sure where to run a command:

1. **Check for `$` or `>` in examples** - These indicate terminal/command prompt
   ```bash
   $ docker-compose up -d    # The $ means this is a terminal command
   ```

2. **Look for file extensions:**
   - `.sh` files → Run in bash (Terminal/Git Bash)
   - `.py` files → Run with `python` or `python3` command in terminal
   - `.env` files → Edit in text editor
   - `.yml` files → Edit in text editor

3. **When in doubt:**
   - Commands with `docker`, `git`, `python` → Terminal/Command Prompt
   - Commands with `cd`, `ls`, `cp`, `mv` → Terminal/Command Prompt
   - Editing files → Text editor (Notepad, VS Code, nano, etc.)

4. **Ask for help** - Open an issue on GitHub if you're stuck!
