# 🚀 Wyze Bridge Quick Start

Get your Wyze cameras streaming in **5 minutes**!

## 🔧 Prerequisites

Before you begin, make sure you have these tools installed:

### Docker and Docker Compose (REQUIRED)

Docker is the platform that runs the bridge application.

**Check if you have Docker:**
```bash
docker --version
docker-compose --version
```

**If you see version numbers, Docker is properly installed. If not, install Docker:**

- **Windows:** Download [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- **Mac:** Download [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
- **Linux:** Follow instructions for your distribution:
  - [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  - [Debian](https://docs.docker.com/engine/install/debian/)
  - [Fedora](https://docs.docker.com/engine/install/fedora/)
  - [Other Linux](https://docs.docker.com/engine/install/)

**After installing Docker, verify it works:**
```bash
docker run hello-world
```

### Python 3 (Optional - only needed for setup wizard)

Python is only needed if you want to use the interactive setup wizard.

**Check if you have Python:**
```bash
python3 --version
```
or on Windows:
```cmd
python --version
```

**If you don't have Python and want to use the setup wizard, install it:**

- **Windows:** Download from [python.org](https://www.python.org/downloads/windows/)
  - ⚠️ Check "Add Python to PATH" during installation!
- **Mac:** Download from [python.org](https://www.python.org/downloads/macos/) or use Homebrew: `brew install python3`
- **Linux:** Usually pre-installed, or install with:
  ```bash
  sudo apt-get install python3  # Ubuntu/Debian
  sudo dnf install python3      # Fedora
  ```

**Note:** You can skip Python installation if you use Method 3 (Manual Config) or the Web Wizard!

### Git (Optional - only needed for cloning the repository)

Git is needed to download the repository code.

**Check if you have Git:**
```bash
git --version
```

**If you don't have Git, install it:**

- **Windows:** Download from [git-scm.com](https://git-scm.com/download/win)
- **Mac:** Download from [git-scm.com](https://git-scm.com/download/mac) or use Homebrew: `brew install git`
- **Linux:** Install with your package manager:
  ```bash
  sudo apt-get install git  # Ubuntu/Debian
  sudo dnf install git      # Fedora
  ```

**Alternative:** Instead of using Git, you can download the repository as a ZIP file from GitHub:
- Go to: https://github.com/allanwrench28/docker-wyze-bridge-wrench-works
- Click the green "Code" button
- Select "Download ZIP"
- Extract the ZIP file to a folder on your computer

---

## 📝 What You Need

Just **4 pieces of information**:
1. ✉️ **Wyze Email** - Your Wyze account email
2. 🔐 **Wyze Password** - Your Wyze account password  
3. 🔑 **API ID** - 36-character UUID from Wyze
4. 🗝️ **API Key** - 60-character key from Wyze

---

## ⚡ Super Quick Setup

### Get Your API Credentials (3 minutes)

1. **Visit:** https://developer-api-console.wyze.com/#/apikey/view
2. **Sign in** with your Wyze account
3. **Click "Create API Key"**
4. **Copy both values:**
   - API ID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
   - API Key: `abcdef1234567890...` (60 characters)

### Setup Method 1: Interactive Wizard (Easiest!)

**Prerequisites:** Python 3 installed (see above)

**Where to run these commands:**
- **Windows:** Open "Command Prompt" (cmd.exe) or "PowerShell" - NOT the Python terminal
- **Mac:** Open "Terminal" app (Applications > Utilities > Terminal)
- **Linux:** Open your terminal emulator

**Commands to run:**
```bash
# Clone the repo (or download and extract ZIP if you don't have Git)
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Run the setup wizard (this is a Python script)
# On Linux/Mac:
python3 app/wyzebridge/setup_wizard.py
# On Windows, use:
python app/wyzebridge/setup_wizard.py

# Follow the on-screen prompts to enter your credentials

# Start the bridge
docker-compose up -d

# Open Web UI in your web browser
# Go to: http://YOUR-IP:5000
```

**What the wizard does:**
- ✅ Guides you step-by-step through entering credentials
- ✅ Validates your API ID and Key formats
- ✅ Saves everything to `.env` file automatically
- ✅ Shows you the next steps

### Setup Method 2: Web Wizard

```bash
# Start the bridge first
docker-compose up -d

# Open your browser
# Go to: http://YOUR-IP:5000/setup

# Follow the on-screen wizard
```

### Setup Method 3: Manual Config

**Prerequisites:** A text editor (Notepad, VS Code, nano, vim, etc.)

**Where to run commands:**
- **Windows:** Open "Command Prompt" (cmd.exe) or "PowerShell"
- **Mac:** Open "Terminal" app
- **Linux:** Open your terminal emulator

**Step 1: Get the repository**
```bash
# Clone the repository (or download ZIP from GitHub)
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works
```

**Step 2: Create your configuration file**
```bash
# Copy the template file
# On Linux/Mac:
cp .env.template .env
# On Windows Command Prompt:
copy .env.template .env
# On Windows PowerShell:
Copy-Item .env.template .env
```

**Step 3: Edit the configuration file**

Open `.env` file in a text editor:
- **Windows:** Right-click `.env` → Open with → Notepad (or VS Code)
- **Mac:** Open with TextEdit or run `nano .env` in Terminal
- **Linux:** Run `nano .env` or use your preferred editor

Add these 4 lines (replace with YOUR actual credentials):
```bash
WYZE_EMAIL=your-email@example.com
WYZE_PASSWORD=your-password
API_ID=your-api-id-here
API_KEY=your-api-key-here
```

**Step 4: Find your computer's IP address**

Run this command in your terminal/command prompt:
```bash
# Linux/Mac:
ip addr show
# or
ifconfig

# Windows Command Prompt:
ipconfig

# Windows PowerShell:
Get-NetIPAddress
```

Look for your local IP address (usually starts with 192.168.x.x or 10.0.x.x)

**Step 5: Add your IP to the .env file**

Add this line to `.env` (replace with YOUR IP):
```bash
WB_IP=192.168.1.100  # Use YOUR actual IP address
```

**Step 6: Start the bridge**
```bash
docker-compose up -d
```

---

## 🎥 Access Your Cameras

Once running, your cameras are available at:

### Web UI
```
http://YOUR-IP:5000
```

### RTSP Streams
```
rtsp://YOUR-IP:8554/camera-name
```

Example: `rtsp://192.168.1.100:8554/front_door`

---

## 🧪 Test Your Stream

### Option 1: VLC Media Player
1. Download VLC: https://www.videolan.org/vlc/
2. Open VLC → Media → Open Network Stream
3. Enter: `rtsp://YOUR-IP:8554/camera-name`
4. Click Play

### Option 2: Web UI
1. Go to `http://YOUR-IP:5000`
2. Click on any camera
3. Click "Streams" → "Copy RTSP URL"
4. Click "Test in VLC"

---

## 📥 Export Features

### Get All Camera URLs

Visit the Web UI and click **Export** in the navbar:

- **Text File** - Simple list of URLs
- **JSON** - Structured data for APIs
- **YAML** - Configuration format
- **VLC Playlist** - Open all cameras in VLC
- **Home Assistant Config** - Ready-to-use YAML

Or use the API directly:
```bash
# Get JSON of all cameras
curl http://YOUR-IP:5000/api/rtsp/urls

# Download Home Assistant config
curl http://YOUR-IP:5000/api/rtsp/export?format=homeassistant > cameras.yaml

# Download VLC playlist
curl http://YOUR-IP:5000/api/rtsp/export?format=vlc > cameras.m3u
```

---

## 🏠 Home Assistant Integration

### Quick Integration

1. In the Web UI, click **Export** → **Camera Config (YAML)**
2. Download the file
3. Open your Home Assistant `configuration.yaml`
4. Add the downloaded content
5. Restart Home Assistant

### Example Generated Config

```yaml
camera:
  - platform: generic
    name: "Front Door"
    stream_source: rtsp://192.168.1.100:8554/front_door
    still_image_url: http://192.168.1.100:5000/snapshot/front_door.jpg
    verify_ssl: false
```

---

## 🔧 Troubleshooting

### Problem: "docker: command not found" or "docker-compose: command not found"

**This means Docker is not installed or not in your PATH.**

**Solution:**
1. Install Docker following the [Prerequisites](#prerequisites) section above
2. On Windows, restart your terminal/command prompt after installing Docker
3. On Linux, you may need to add your user to the docker group:
   ```bash
   sudo usermod -aG docker $USER
   ```
   Then log out and back in

### Problem: "python: command not found" or "python3: command not found"

**This means Python is not installed or not in your PATH.**

**Solution:**
- Install Python following the [Prerequisites](#prerequisites) section above
- On Windows, make sure you checked "Add Python to PATH" during installation
- Alternatively, use Method 2 (Web Wizard) or Method 3 (Manual Config) which don't require Python

### Problem: "git: command not found"

**This means Git is not installed.**

**Solution:**
- Install Git following the [Prerequisites](#prerequisites) section above
- Alternatively, download the repository as a ZIP file from GitHub (see Prerequisites section)

### Problem: Can't connect to cameras

**Solution:**
```bash
# In your .env file, add:
CONNECT_TIMEOUT=90
NET_MODE=LAN
```

### Problem: Port already in use

**Solution:**
```yaml
# In docker-compose.yml, change:
ports:
  - "8555:8554"  # Changed from 8554:8554
```

Then use: `rtsp://YOUR-IP:8555/camera-name`

### Problem: Credentials not working

**Solution:**
Run the setup wizard again:
```bash
# On Linux/Mac:
python3 app/wyzebridge/setup_wizard.py
# On Windows:
python app/wyzebridge/setup_wizard.py
```

### Problem: "Permission denied" when running Docker commands (Linux)

**Solution:**
Add your user to the docker group:
```bash
sudo usermod -aG docker $USER
```
Then log out and log back in for the changes to take effect.

### Check Logs

```bash
docker-compose logs -f wyze-bridge
```

---

## 📚 Need More Help?

- **Full Setup Guide:** [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **RTSP Setup Guide:** [RTSP-SETUP.md](RTSP-SETUP.md)
- **Command Reference:** [COMMAND_REFERENCE.md](COMMAND_REFERENCE.md) - Where to run commands
- **GitHub Issues:** https://github.com/allanwrench28/docker-wyze-bridge-wrench-works/issues

---

## ✅ Quick Checklist

- [ ] Get API credentials from https://developer-api-console.wyze.com/
- [ ] Clone the repository
- [ ] Run setup wizard OR edit .env
- [ ] Find your IP address
- [ ] Add IP to .env as `WB_IP`
- [ ] Run `docker-compose up -d`
- [ ] Access Web UI at `http://YOUR-IP:5000`
- [ ] Test stream in VLC: `rtsp://YOUR-IP:8554/camera-name`
- [ ] Export URLs if needed
- [ ] Add to Home Assistant (optional)
- [ ] Enjoy! 🎉

---

**Total setup time:** 5-10 minutes  
**Difficulty:** Easy  
**Prerequisites:** Docker installed

---

## 🎯 Key Features

✅ **Simple 4-Field Setup** - Just email, password, API ID, and API Key  
✅ **Auto Discovery** - Finds all your cameras automatically  
✅ **Multiple Export Formats** - JSON, YAML, text, VLC playlists  
✅ **Home Assistant Ready** - Auto-generate camera configs  
✅ **Stream Testing** - Built-in VLC integration  
✅ **Copy to Clipboard** - One-click URL copying  
✅ **Interactive Wizard** - Step-by-step guidance  

---

**Made with ❤️ for the Wyze community**
