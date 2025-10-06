# Wyze Bridge RTSP Setup Guide

## 🔧 Prerequisites

Before starting, make sure you have:
- **Docker and Docker Compose** installed - [Get Docker](https://docs.docker.com/get-docker/)
- **A text editor** (Notepad, VS Code, nano, etc.)

**Check if Docker is installed:**
```bash
docker --version
docker-compose --version
```

**Where to run commands:**
- **Windows:** Command Prompt (cmd.exe) or PowerShell - NOT Python terminal
- **Mac:** Terminal app (Applications → Utilities → Terminal)
- **Linux:** Terminal emulator

## Quick Setup Steps

### 1. Get Your Wyze API Credentials
1. Go to https://developer-api-console.wyze.com/
2. Create an account and generate API keys
3. Note down your `API_ID` and `API_KEY`

### 2. Configure Your Environment

**Step 1: Copy the template**
```bash
# On Linux/Mac:
cp .env.template .env

# On Windows Command Prompt:
copy .env.template .env

# On Windows PowerShell:
Copy-Item .env.template .env
```

**Step 2: Edit the .env file**

Open `.env` in a text editor:
- **Windows:** Right-click `.env` → Open with → Notepad
- **Mac:** Run `open -e .env` or use TextEdit
- **Linux:** Run `nano .env` or use your preferred editor

**What to edit:** Add your credentials and network settings

### 3. Find Your Network IP

**Where to run these commands:** Command Prompt/Terminal (NOT Python IDLE)

Run one of these commands to find your local IP:
```bash
# Windows (Command Prompt):
ipconfig

# Windows (PowerShell):
Get-NetIPAddress

# Mac:
ifconfig
# or
ipconfig getifaddr en0

# Linux:
ip addr show
# or
hostname -I
```

Look for your local IP address (usually starts with 192.168.x.x or 10.0.x.x)

Update `WB_IP` in your `.env` file with this IP address.

### 4. Start the Bridge

**Where to run:** Command Prompt/Terminal (same place you ran previous commands)

```bash
docker-compose up -d
```

**What this does:** Starts the bridge in the background

### 5. Access Your Streams

**Web UI:** http://your-ip:5000
**RTSP Stream:** rtsp://your-ip:8554/panv3

Replace `your-ip` with your actual IP address and `panv3` with your camera name.

## Troubleshooting Your Timeout Issues

The configuration includes these fixes for your `IOTC_ER_TIMEOUT` errors:
- `CONNECT_TIMEOUT=60` - Increased connection timeout to 60 seconds
- `RESEND=0` - Disabled packet retransmission
- Pan V3 specific settings for better compatibility

## Testing Your RTSP Stream

### VLC Media Player (Recommended)

**Download VLC if you don't have it:**
- Get from: https://www.videolan.org/vlc/

**Test your stream:**
1. Open VLC Media Player (NOT Python IDLE or terminal)
2. Go to **Media** → **Open Network Stream** (or press `Ctrl+N`)
3. Enter your RTSP URL: `rtsp://your-ip:8554/camera-name`
   - Example: `rtsp://192.168.1.100:8554/panv3`
4. Click **Play**

**Note:** Replace `your-ip` with your actual IP address and `camera-name` with your camera name from the Web UI.

### FFmpeg/FFplay Command Line

**Prerequisites:** FFmpeg must be installed
- Download from: https://ffmpeg.org/download.html

**Where to run:** Command Prompt, PowerShell, or Terminal (NOT Python terminal)

**Test command:**
```bash
ffplay rtsp://your-ip:8554/panv3
```

**With low latency options:**
```bash
ffplay -fflags nobuffer -flags low_delay -framedrop rtsp://your-ip:8554/panv3
```

### Home Assistant

**Where to find configuration.yaml:**
- Home Assistant OS: Use File Editor add-on or SSH
- Home Assistant Core: Usually in `/config/configuration.yaml`
- Docker: In your Home Assistant config directory

**What to do:**
1. Open `configuration.yaml` in a text editor (File Editor add-on in HA, or nano/vim if SSH)
2. Add this camera configuration:

```yaml
camera:
  - platform: generic
    name: "Pan V3 Camera"
    stream_source: rtsp://your-ip:8554/panv3
    still_image_url: http://your-ip:5000/img/panv3.jpg
```

3. Replace `your-ip` with your actual IP address
4. Replace `panv3` with your actual camera name
5. Save the file
6. Restart Home Assistant:
   - **Web UI:** Developer Tools → YAML → Restart
   - **Command Line:** `ha core restart` (Home Assistant OS)

**Easier method:** Use the Web UI export feature at `http://your-ip:5000` to auto-generate the camera config!

## Camera Names and URLs

Your camera streams will be available at:
- `rtsp://your-ip:8554/camera-name`
- Replace spaces in camera names with underscores
- Example: "Front Door" becomes "front_door"

Check the Web UI at http://your-ip:5000 to see all available camera names and their URLs.

## Port Reference

- **8554** - RTSP streaming (main port you need)
- **5000** - Web UI for management
- **8888** - HLS streams (browser-compatible)

## Logs and Debugging

**Where to run:** Command Prompt, PowerShell, or Terminal (where you ran docker-compose)

**Check live logs:**
```bash
docker-compose logs -f wyze-bridge
```

**What this does:** Shows real-time logs from the bridge
- Press `Ctrl+C` to stop viewing logs (container keeps running)

**Check recent logs:**
```bash
docker-compose logs --tail=100 wyze-bridge
```

**Save logs to a file:**
```bash
docker-compose logs wyze-bridge > bridge-logs.txt
```

**Common issues:**

If you see timeout errors, edit your `.env` file and increase `CONNECT_TIMEOUT`:
```bash
CONNECT_TIMEOUT=90  # or 120
```

Then restart the bridge:
```bash
docker-compose restart
```