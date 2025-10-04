# 🎬 Wyze Bridge Complete Setup Guide

Welcome to the complete setup guide for Wyze Bridge! This guide will walk you through the entire process from start to finish, making it simple to get your Wyze cameras streaming via RTSP.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Your API Credentials](#getting-your-api-credentials)
3. [Installation Methods](#installation-methods)
4. [Configuration](#configuration)
5. [Accessing Your Streams](#accessing-your-streams)
6. [Home Assistant Integration](#home-assistant-integration)
7. [Testing Your Streams](#testing-your-streams)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Features](#advanced-features)

---

## 🎯 Prerequisites

Before you begin, you'll need:

- **Docker and Docker Compose** installed on your system
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

The easiest way to get started:

```bash
# Clone the repository
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Run the setup wizard
python3 app/wyzebridge/setup_wizard.py
```

The wizard will:
- ✅ Guide you through entering your credentials
- ✅ Validate the format of your API keys
- ✅ Save everything to your `.env` file
- ✅ Show you next steps

### Method 2: Manual Configuration

If you prefer to configure manually:

```bash
# Clone the repository
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Copy the template
cp .env.template .env

# Edit with your favorite editor
nano .env  # or vim, code, etc.
```

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

### Issue: "Connection Timeout" or "IOTC_ER_TIMEOUT"

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
