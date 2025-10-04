# 🚀 Wyze Bridge Quick Start

Get your Wyze cameras streaming in **5 minutes**!

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

```bash
# Clone the repo
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works

# Run the setup wizard
python3 app/wyzebridge/setup_wizard.py

# Start the bridge
docker-compose up -d

# Open Web UI
# Go to: http://YOUR-IP:5000
```

### Setup Method 2: Web Wizard

```bash
# Start the bridge first
docker-compose up -d

# Open your browser
# Go to: http://YOUR-IP:5000/setup

# Follow the on-screen wizard
```

### Setup Method 3: Manual Config

```bash
# Clone and setup
git clone https://github.com/allanwrench28/docker-wyze-bridge-wrench-works.git
cd docker-wyze-bridge-wrench-works
cp .env.template .env

# Edit .env with your favorite editor
nano .env

# Add these 4 lines:
WYZE_EMAIL=your-email@example.com
WYZE_PASSWORD=your-password
API_ID=your-api-id-here
API_KEY=your-api-key-here

# Find your IP address
ip addr show  # Linux/Mac
ipconfig      # Windows

# Add your IP to .env
WB_IP=192.168.1.100  # Use YOUR IP

# Start the bridge
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
python3 app/wyzebridge/setup_wizard.py
```

### Check Logs

```bash
docker-compose logs -f wyze-bridge
```

---

## 📚 Need More Help?

- **Full Setup Guide:** [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **RTSP Setup Guide:** [RTSP-SETUP.md](RTSP-SETUP.md)
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
