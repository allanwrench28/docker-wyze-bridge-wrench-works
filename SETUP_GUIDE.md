# 🎬 Wyze Bridge Complete Setup Guide

Welcome to the complete setup guide for Wyze Bridge! This guide will walk you through the entire process from start to finish, making it simple to get your Wyze cameras streaming via RTSP.

## 📋 Table of Contents

1. [Understanding Your Command Line](#understanding-your-command-line)
2. [Prerequisites](#prerequisites)
3. [Getting Your API Credentials](#getting-your-api-credentials)
4. [Installation Methods](#installation-methods)
5. [Configuration](#configuration)
6. [Accessing Your Streams](#accessing-your-streams)
7. [Home Assistant Integration](#home-assistant-integration)
8. [Testing Your Streams](#testing-your-streams)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Features](#advanced-features)

---

## 💻 Understanding Your Command Line

**Important:** This guide includes commands that you need to type and run. Here's where to run them:

### Windows Users

**Use one of these:**
- ✅ **Command Prompt** (cmd.exe)
  - How to open: Press `Win+R`, type `cmd`, press Enter
  - Or: Start menu → Search "Command Prompt"
  
- ✅ **PowerShell**
  - How to open: Press `Win+R`, type `powershell`, press Enter
  - Or: Right-click Start menu → "Windows PowerShell"

- ✅ **Git Bash** (for .sh scripts only, after installing Git)
  - How to open: Right-click in folder → "Git Bash Here"

**Do NOT use:**
- ❌ Python IDLE
- ❌ Python (command line)
- ❌ Regular text editors

**What goes where on Windows:**
- **Docker commands** (`docker`, `docker-compose`) → Command Prompt or PowerShell
- **Python scripts** (`python app/wyzebridge/setup_wizard.py`) → Command Prompt or PowerShell
- **Bash scripts** (`./scripts/check-upstream.sh`) → Git Bash only
- **Editing .env file** → Notepad, VS Code, or any text editor

### Mac Users

**Use:**
- ✅ **Terminal** (built-in)
  - How to open: Applications → Utilities → Terminal
  - Or: Spotlight (`Cmd+Space`) → type "Terminal"

**What to run:**
- All commands (Docker, Python, bash scripts) → Terminal
- Editing .env file → TextEdit, VS Code, or any text editor

### Linux Users

**Use:**
- ✅ **Terminal Emulator** (varies by distribution)
  - Common shortcut: `Ctrl+Alt+T`
  - Or: Applications menu → Terminal

**What to run:**
- All commands (Docker, Python, bash scripts) → Terminal
- Editing .env file → nano, vim, gedit, or any text editor

### Quick Reference

|Task|Windows|Mac|Linux|
|------|---------|-----|-------|
|Run Docker|Command Prompt / PowerShell|Terminal|Terminal|
|Run Python script|Command Prompt / PowerShell|Terminal|Terminal|
|Run bash script|Git Bash|Terminal|Terminal|
|Edit .env|Notepad / VS Code|TextEdit / VS Code|nano / vim / gedit|

---

## 🎯 Prerequisites

Before you begin, you'll need:

### Required Software

#### Docker and Docker Compose (REQUIRED)

Docker runs the bridge application in a container.

**Check if installed:**
```bash
docker --version
docker-compose --version
```

**If not installed, download from:**
- **Windows:** [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- **Mac:** [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
- **Linux:** [Docker Engine for Linux](https://docs.docker.com/engine/install/)

**Verify installation:**
```bash
docker run hello-world
```

**Where to run Docker commands:**
- **Windows:** Command Prompt (cmd.exe) or PowerShell - NOT Python terminal
- **Mac:** Terminal app (Applications > Utilities > Terminal)
- **Linux:** Any terminal emulator

#### Python 3 (Optional - only for setup wizard)

**Check if installed:**
```bash
python3 --version  # Linux/Mac
python --version   # Windows
```

**If not installed and you want to use the setup wizard:**
- **Windows:** [python.org/downloads](https://www.python.org/downloads/windows/) (Check "Add Python to PATH"!)
- **Mac:** [python.org/downloads](https://www.python.org/downloads/macos/) or `brew install python3`
- **Linux:** `sudo apt-get install python3` (Ubuntu/Debian) or `sudo dnf install python3` (Fedora)

**Note:** You can skip Python if you configure manually!

#### Git (Optional - for cloning repository)

**Check if installed:**
```bash
git --version
```

**If not installed:**
- **Windows:** [git-scm.com/download/win](https://git-scm.com/download/win)
- **Mac:** [git-scm.com/download/mac](https://git-scm.com/download/mac) or `brew install git`
- **Linux:** `sudo apt-get install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora)

**Alternative:** Download as ZIP from [GitHub](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works) instead of cloning.

### Required Information

- **Wyze account** with cameras registered
- **Network access** to your cameras (same local network)
- **Basic network information** (your computer's IP address)

---

## 🔑 Getting Your API Credentials

This is the most important step! You need 4 pieces of information:

### Step 1: Visit the Wyze Developer Portal

Go to: **https://developer-api-console.wyze.com/#/apikey/view**

### Step 2: Sign In or Create an Account

- Use your existing Wyze account credentials, OR
- Create a new developer account (recommended to use the same email as your Wyze app)

### Step 3: Generate API Keys

1. Click the **"Create API Key"** button
2. Give your key a name (e.g., "Home Bridge")
3. You'll receive two values:
   - **API ID**: A 36-character UUID (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)
   - **API Key**: A 60-character alphanumeric string

### Step 4: Save Your Credentials

⚠️ **IMPORTANT**: Save these immediately! You won't be able to see the API Key again.

Copy these values:
- ✉️ Your Wyze account email
- 🔐 Your Wyze account password
- 🔑 API ID (36 characters)
- 🗝️ API Key (60 characters)

---

## 🚀 Installation Methods

### Method 1: Interactive Setup Wizard (Recommended for Beginners)

**Prerequisites:** Python 3 installed (see Prerequisites section above)

The easiest way to get started:

**Where to run these commands:**
- **Windows:** Open "Command Prompt" (Start → type "cmd") or "PowerShell"
  - ⚠️ Do NOT use Python IDLE or Python terminal
  - ⚠️ Use regular Windows Command Prompt or PowerShell
- **Mac:** Open "Terminal" (Applications → Utilities → Terminal)
- **Linux:** Open your terminal emulator (Ctrl+Alt+T on most distributions)

**Step-by-step commands:**

```bash
# Step 1: Clone the repository (or download ZIP from GitHub)
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git

# Step 2: Navigate into the directory
cd docker-wyze-bridge-wrench-works

# Step 3: Run the setup wizard (Python script)
# On Linux/Mac:
python3 app/wyzebridge/setup_wizard.py

# On Windows:
python app/wyzebridge/setup_wizard.py
```

**What the wizard does:**
- ✅ Guides you through entering your credentials step-by-step
- ✅ Validates the format of your API keys automatically
- ✅ Saves everything to your `.env` file (no manual editing needed)
- ✅ Shows you the next steps to start the bridge

**After the wizard completes:**
The wizard will create a `.env` file with your credentials. You can then proceed to start the bridge with Docker.

### Method 2: Manual Configuration

**Prerequisites:** A text editor (any will work: Notepad, VS Code, nano, vim, etc.)

If you prefer to configure manually without Python:

**Where to run commands:**
- **Windows:** Command Prompt or PowerShell
- **Mac:** Terminal app
- **Linux:** Terminal emulator

**Step 1: Get the repository**
```bash
# Clone the repository
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works
```

**Alternative without Git:**
- Download ZIP from [GitHub repository](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works)
- Extract to a folder
- Open Command Prompt/Terminal and navigate to that folder

**Step 2: Copy the template**
```bash
# On Linux/Mac:
cp .env.template .env

# On Windows Command Prompt:
copy .env.template .env

# On Windows PowerShell:
Copy-Item .env.template .env
```

**Step 3: Edit the configuration file**

Open `.env` in a text editor:
- **Windows:** Right-click `.env` → "Open with" → Choose Notepad or VS Code
- **Mac:** Double-click `.env` and open with TextEdit, or run `open -e .env` in Terminal
- **Linux:** Run `nano .env` in terminal, or use your preferred text editor

**Which application to use:**
- ✅ Use any TEXT EDITOR (Notepad, TextEdit, VS Code, Sublime, nano, vim)
- ❌ Do NOT use Word, Excel, or other document processors
- ❌ Do NOT try to open in Python IDLE or Python terminal

---

## ⚙️ Configuration

### Minimal Configuration (Just 4 Fields!)

Edit your `.env` file with these 4 required fields:

```bash
# === REQUIRED: Your Wyze Credentials ===
WYZE_EMAIL=your-email@example.com
WYZE_PASSWORD=your-password
API_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
API_KEY=your-60-character-api-key-here
```

### Find Your Network IP

You need your computer's local IP address:

**Windows:**
```cmd
ipconfig
```
Look for "IPv4 Address" (usually starts with 192.168.x.x or 10.0.x.x)

**Linux/Mac:**
```bash
ip addr show
# or
ifconfig
```
Look for "inet" address on your main network interface

**Example:** `192.168.1.100`

### Add Your IP to Configuration

Add this line to your `.env` file:

```bash
WB_IP=192.168.1.100  # Use YOUR IP address here
```

### Optional: Improve Connection Stability

If you experience timeout issues, add these settings:

```bash
# Connection timeout fixes
CONNECT_TIMEOUT=60
RESEND=0
NET_MODE=any
```

### Complete Minimal .env Example

```bash
# Wyze Credentials (REQUIRED)
WYZE_EMAIL=john@example.com
WYZE_PASSWORD=mySecurePassword123
API_ID=12345678-abcd-1234-efgh-123456789abc
API_KEY=abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTU

# Network Configuration
WB_IP=192.168.1.100

# Connection Settings (Optional but recommended)
CONNECT_TIMEOUT=60
RESEND=0
```

---

## 🎥 Accessing Your Streams

### Step 1: Start the Bridge

```bash
docker-compose up -d
```

### Step 2: Access the Web UI

Open your browser and go to:
```
http://YOUR-IP:5000
```

Example: `http://192.168.1.100:5000`

You'll see:
- ✅ All discovered cameras
- ✅ Real-time stream status
- ✅ RTSP URLs for each camera
- ✅ Stream controls and settings

### Step 3: Find Your RTSP URLs

Your streams are automatically available at:

```
rtsp://YOUR-IP:8554/camera-name
```

**Camera names:**
- Spaces are replaced with underscores
- Special characters are removed
- Example: "Front Door" → `front_door`

**Check the Web UI** to see the exact camera names!

### Quick Reference: All Stream Types

Each camera is available in multiple formats:

| Format | URL Pattern | Port | Best For |
|--------|-------------|------|----------|
| **RTSP** | `rtsp://YOUR-IP:8554/camera-name` | 8554 | VLC, Home Assistant, NVR |
| **HLS** | `http://YOUR-IP:8888/camera-name/` | 8888 | Web browsers |
| **RTMP** | `rtmp://YOUR-IP:1935/camera-name` | 1935 | OBS, streaming software |
| **WebRTC** | `http://YOUR-IP:8889/camera-name/` | 8889 | Low-latency web viewing |

---

## 🏠 Home Assistant Integration

### Method 1: As a Home Assistant Add-on

1. **Add Custom Repository:**
   - Go to **Supervisor** → **Add-on Store** → **⋮** (menu) → **Repositories**
   - Add: `https://github.com/allanwrench28/docker-wyze-bridge-wrench-works`

2. **Install the Add-on:**
   - Find "Docker Wyze Bridge" in the add-on store
   - Click **Install**

3. **Configure:**
   - Go to the **Configuration** tab
   - Enter your 4 credentials:
     - Wyze Email
     - Wyze Password
     - API ID
     - API Key
   - Click **Save**

4. **Start:**
   - Click **Start**
   - Check the **Log** tab for confirmation

### Method 2: Standalone Docker with Home Assistant Integration

Add to your `configuration.yaml`:

```yaml
# Camera configurations
camera:
  # Front Door Camera
  - platform: generic
    name: "Front Door"
    stream_source: rtsp://192.168.1.100:8554/front_door
    still_image_url: http://192.168.1.100:5000/snapshot/front_door.jpg
    verify_ssl: false
    
  # Living Room Camera
  - platform: generic
    name: "Living Room"
    stream_source: rtsp://192.168.1.100:8554/living_room
    still_image_url: http://192.168.1.100:5000/snapshot/living_room.jpg
    verify_ssl: false
```

**Then restart Home Assistant:**
```bash
# From Home Assistant UI
# Developer Tools → YAML → Restart
```

### Auto-Generate Home Assistant Config

Use the Web UI to automatically generate your configuration:

1. Go to `http://YOUR-IP:5000`
2. Click on any camera
3. Look for the **"Home Assistant Config"** button
4. Copy the generated YAML
5. Paste into your `configuration.yaml`

---

## 🧪 Testing Your Streams

### Test with VLC Media Player

**VLC** is the easiest way to test your streams.

1. **Download VLC** (if you don't have it):
   - https://www.videolan.org/vlc/

2. **Open Network Stream:**
   - Open VLC
   - Go to **Media** → **Open Network Stream** (or press `Ctrl+N`)

3. **Enter Your RTSP URL:**
   ```
   rtsp://192.168.1.100:8554/front_door
   ```
   (Replace with your IP and camera name)

4. **Click Play**
   - You should see your camera stream within a few seconds!

### Test with FFplay (Command Line)

```bash
# Basic playback
ffplay rtsp://192.168.1.100:8554/front_door

# With low latency settings
ffplay -fflags nobuffer -flags low_delay -framedrop rtsp://192.168.1.100:8554/front_door
```

### Test with MPV Player

```bash
mpv rtsp://192.168.1.100:8554/front_door
```

### Test Stream Health

Use the Web UI at `http://YOUR-IP:5000` to:
- ✅ View real-time connection status
- ✅ Check stream health
- ✅ See bandwidth usage
- ✅ Monitor for errors

---

## 🔧 Troubleshooting

### Common Setup Issues

#### Issue: "command not found" Errors

**Problem: `docker: command not found` or `docker-compose: command not found`**

**Cause:** Docker is not installed or not in your system PATH.

**Solution:**
1. Install Docker following the [Prerequisites](#prerequisites) section
2. After installation:
   - **Windows:** Restart Command Prompt/PowerShell
   - **Linux:** Log out and back in, or run:
     ```bash
     sudo usermod -aG docker $USER
     ```
3. Verify installation:
   ```bash
   docker --version
   ```

**Problem: `python: command not found` or `python3: command not found`**

**Cause:** Python is not installed or not in your system PATH.

**Solution:**
1. Install Python following the [Prerequisites](#prerequisites) section
2. On Windows, make sure you checked "Add Python to PATH" during installation
3. Restart your terminal/command prompt
4. **Alternative:** Skip the setup wizard and use manual configuration instead

**Problem: `git: command not found`**

**Cause:** Git is not installed.

**Solution:**
1. Install Git following the [Prerequisites](#prerequisites) section
2. Restart your terminal/command prompt
3. **Alternative:** Download the repository as ZIP file from GitHub instead of cloning

#### Issue: "Cannot run .sh script on Windows"

**Problem:** Trying to run bash scripts (`.sh` files) in Windows Command Prompt or PowerShell

**Cause:** Bash scripts require a bash shell environment.

**Solution:**
- **Option 1:** Install [Git for Windows](https://git-scm.com/download/win) which includes Git Bash
  - Right-click in folder → "Git Bash Here"
  - Run: `./scripts/check-upstream.sh`
- **Option 2:** Use [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- **Option 3:** Most users don't need to run these scripts - they're for maintainers

#### Issue: "Permission denied" When Running Docker (Linux)

**Problem:** Docker commands fail with "permission denied" error

**Cause:** Your user is not in the `docker` group.

**Solution:**
```bash
# Add your user to the docker group
sudo usermod -aG docker $USER

# Log out and back in for changes to take effect
# Or run this in current session:
newgrp docker

# Verify it works:
docker run hello-world
```

#### Issue: Opening Files in Wrong Application

**Problem:** Trying to edit `.env` file or run scripts in the wrong application

**What to use:**
- ✅ `.env` files → Use TEXT EDITOR (Notepad, VS Code, nano, vim)
- ✅ `.py` Python scripts → Run from COMMAND LINE/TERMINAL (not Python IDLE)
- ✅ `.sh` Bash scripts → Run from BASH SHELL (Terminal on Mac/Linux, Git Bash on Windows)
- ✅ Docker commands → Run from COMMAND LINE/TERMINAL

**What NOT to use:**
- ❌ Don't open `.env` in Python IDLE
- ❌ Don't open `.env` in Word or Excel
- ❌ Don't try to double-click `.py` files (run them from command line)
- ❌ Don't try to run `.sh` scripts in Windows Command Prompt
- ❌ Don't try to run Docker commands in Python IDLE

### Connection and Stream Issues

#### Issue: "Connection Timeout" or "IOTC_ER_TIMEOUT"

**Solution 1: Increase Timeout**
```bash
# In your .env file:
CONNECT_TIMEOUT=90  # or even 120
```

**Solution 2: Check Network Mode**
```bash
# Try forcing LAN mode:
NET_MODE=LAN
```

**Solution 3: Restart Everything**
```bash
# Restart the bridge
docker-compose restart

# Or full clean restart
docker-compose down
docker-compose up -d
```

### Issue: "Cannot Find Cameras"

**Check:**
1. ✅ Are credentials correct? (Check Web UI login)
2. ✅ Are cameras online in Wyze app?
3. ✅ Are cameras on the same network?

**Try:**
```bash
# Clear cache and restart
docker-compose down
rm -rf app/tokens/*
docker-compose up -d
```

### Issue: "Stream Not Playing in VLC"

**Check:**
1. ✅ Can you access the Web UI? (`http://YOUR-IP:5000`)
2. ✅ Is the camera showing as "connected" in Web UI?
3. ✅ Try the HLS stream instead: `http://YOUR-IP:8888/camera-name/`

**Debug:**
```bash
# Check logs
docker-compose logs -f wyze-bridge

# Look for errors related to your camera
docker-compose logs wyze-bridge | grep "camera-name"
```

### Issue: "Authentication Failed"

**Verify:**
1. ✅ API ID is exactly 36 characters
2. ✅ API Key is exactly 60 characters
3. ✅ No extra spaces in credentials
4. ✅ Email and password are correct

**Fix:**
```bash
# Run the setup wizard again
python3 app/wyzebridge/setup_wizard.py
```

### Issue: "Port Already in Use"

**Check what's using the port:**
```bash
# Linux/Mac
sudo lsof -i :8554

# Windows
netstat -ano | findstr :8554
```

**Solution: Change ports in docker-compose.yml:**
```yaml
ports:
  - "8555:8554"  # Change external port
```

Then use: `rtsp://YOUR-IP:8555/camera-name`

### Issue: Cameras Disconnect Frequently

**Solution:**
```bash
# In .env:
CONNECT_TIMEOUT=120
RESEND=0
NET_MODE=LAN
IGNORE_OFFLINE=false
```

### Getting Help

**Check Logs:**
```bash
# Live logs
docker-compose logs -f

# Save logs to file
docker-compose logs > wyze-bridge-logs.txt
```

**Enable Debug Logging:**
```bash
# In .env:
LOG_LEVEL=DEBUG
```

---

## 🚀 Advanced Features

### Export RTSP URLs

The bridge can automatically export all your camera URLs:

```bash
# Get plain text list
curl http://YOUR-IP:5000/api/rtsp/export?format=text

# Get JSON
curl http://YOUR-IP:5000/api/rtsp/export?format=json

# Get YAML
curl http://YOUR-IP:5000/api/rtsp/export?format=yaml

# Get Home Assistant config
curl http://YOUR-IP:5000/api/rtsp/export?format=homeassistant

# Get VLC playlist
curl http://YOUR-IP:5000/api/rtsp/export?format=vlc > cameras.m3u
```

### Stream Quality Settings

Control stream quality per camera:

```bash
# Global quality (in .env)
QUALITY=HD120  # Options: SD, HD, HD120, FHD (if supported)

# Per-camera quality
FRONT_DOOR_QUALITY=FHD
BACK_YARD_QUALITY=SD
```

### Enable Audio

```bash
# Global audio setting
AUDIO=true

# Per-camera audio
FRONT_DOOR_AUDIO=true
```

### Recording

Enable automatic recording:

```bash
# Enable recording for all cameras
RECORD_ALL=true
RECORD_PATH=/recordings
RECORD_LENGTH=60  # seconds per file

# Per-camera recording
FRONT_DOOR_RECORD=true
```

### Substreams

Get lower resolution substreams:

```bash
# Enable substreams
SUBSTREAM=true

# Access substream
rtsp://YOUR-IP:8554/camera-name-sub
```

### Motion Detection

Enable motion detection webhooks:

```bash
MOTION_API=true
MOTION_WEBHOOKS=http://your-server/motion-webhook
```

---

## 📚 Additional Resources

- **Project Repository**: https://github.com/allanwrench28/docker-wyze-bridge-wrench-works
- **Command Reference**: [COMMAND_REFERENCE.md](COMMAND_REFERENCE.md) - Quick reference for running commands
- **Quick Start Guide**: [QUICK_START.md](QUICK_START.md) - 5-minute setup
- **RTSP Setup Guide**: [RTSP-SETUP.md](RTSP-SETUP.md) - RTSP-specific configuration
- **Wyze Developer Portal**: https://developer-api-console.wyze.com/
- **Issue Tracker**: [GitHub Issues](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works/issues)
- **VLC Media Player**: https://www.videolan.org/vlc/

---

## 🎉 Success!

If you've followed this guide, you should now have:

✅ Working RTSP streams from all your Wyze cameras  
✅ Access through the Web UI  
✅ Integration with Home Assistant (if desired)  
✅ Ability to view streams in VLC or other players  

**Enjoy your streams!** 📹✨

---

## 💡 Quick Start Checklist

Print this or keep it handy:

- [ ] Get API credentials from https://developer-api-console.wyze.com/
- [ ] Clone repository
- [ ] Run setup wizard OR edit .env manually
- [ ] Find your network IP address
- [ ] Add IP to .env as `WB_IP`
- [ ] Run `docker-compose up -d`
- [ ] Access Web UI at `http://YOUR-IP:5000`
- [ ] Test stream in VLC: `rtsp://YOUR-IP:8554/camera-name`
- [ ] (Optional) Add to Home Assistant
- [ ] Celebrate! 🎉
