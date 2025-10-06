# Wyze Bridge HTTP/Browser Streaming Setup Guide

## 🔧 Prerequisites

Before starting, make sure you have:
- **Docker and Docker Compose** installed - [Get Docker](https://docs.docker.com/get-docker/)
- **A text editor** (Notepad, VS Code, nano, etc.)
- **Wyze Bridge already running**  
  If you haven't set up Wyze Bridge yet, follow these basic steps:
  1. **Pull the Wyze Bridge Docker image:**
     ```bash
     docker pull mrlt8/wyze-bridge
     ```
  2. **Create a `docker-compose.yml` file** with at least the following content:
     ```yaml
     version: "3"
     services:
       wyze-bridge:
         image: mrlt8/wyze-bridge
         restart: unless-stopped
         ports:
           - 5000:5000
           - 8554:8554
           - 8888:8888
     ```
  3. **Start the bridge:**
     ```bash
     docker-compose up -d
     ```

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

### 1. Verify Bridge is Running

First, make sure the Wyze Bridge is running:

```bash
docker-compose ps
```

You should see the `wyze-bridge` container running.

### 2. Configure Ports for HTTP Streaming

Edit your `docker-compose.yml` file to ensure these ports are exposed:

```yaml
ports:
  - 5000:5000      # Web UI and snapshots
  - 8554:8554      # RTSP (for reference)
  - 8888:8888      # HLS streaming
  - 8889:8889      # WebRTC (optional)
  - 8189:8189/udp  # WebRTC/ICE (optional)
```

**For WebRTC** (optional low-latency streaming), also add your server IP to the environment:

```yaml
environment:
  - WB_IP=your-ip  # Replace with your actual IP
```

### 3. Restart the Bridge

If you made changes to `docker-compose.yml`:

```bash
docker-compose down
docker-compose up -d
```

### 4. Find Your Network IP

**Where to run these commands:** Command Prompt/Terminal (NOT Python IDLE)

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

### 5. Access Your Streams

**Web UI:** http://your-ip:5000

**Stream types available:**
- **HLS:** `http://your-ip:8888/camera-name/`
- **Snapshots:** `http://your-ip:5000/snapshot/camera-name.jpg`
- **WebRTC:** Access via Web UI at `http://your-ip:5000`

Replace `your-ip` with your actual IP address and `camera-name` with your camera name.

## Stream Types Overview
# HTTP/Browser-Compatible Streaming Guide

This guide explains how to use HTTP-based streaming options that work with browsers and tools that don't support RTSP (like OctoPrint, web dashboards, etc.).

## Overview

While RTSP is excellent for local network streaming, many applications and browsers don't support RTSP natively. This bridge provides several HTTP-based alternatives:

- **HLS (HTTP Live Streaming)** - Works in most modern browsers
- **WebRTC** - Low-latency browser streaming
- **HTTP Snapshots** - Static images via HTTP
- **MJPEG Streams** - Motion JPEG over HTTP (via Web UI)

## Stream Types Comparison

| Protocol | Port | URL Format | Best For | Browser Support |
|----------|------|------------|----------|-----------------|
| **RTSP** | 8554 | `rtsp://ip:8554/camera-name` | VLC, Home Assistant, NVRs | ❌ No |
| **HLS** | 8888 | `http://ip:8888/camera-name/` | Web browsers, dashboards | ✅ Yes |
| **WebRTC** | 8889 | Via Web UI | Low-latency browser viewing | ✅ Yes |
| **Snapshots** | 5000 | `http://ip:5000/snapshot/camera-name.jpg` | Static images, OctoPrint | ✅ Yes |

## Testing Your HTTP Streams

### Testing HLS Streams

#### Method 1: In Your Web Browser

**Simplest method:**
1. Open your web browser (Chrome, Firefox, Safari, Edge)
2. Enter the URL: `http://your-ip:8888/camera-name/`
   - Example: `http://your-ip:8888/front_door/`
3. The stream should play automatically

**Note:** Replace `your-ip` with your actual IP address and `camera-name` with your camera name from the Web UI.

#### Method 2: VLC Media Player

**Download VLC if you don't have it:**
- Get from: https://www.videolan.org/vlc/

**Test your HLS stream:**
1. Open VLC Media Player
2. Go to **Media** → **Open Network Stream** (or press `Ctrl+N`)
3. Enter your HLS URL: `http://your-ip:8888/camera-name/stream.m3u8`
   - Example: `http://your-ip:8888/front_door/stream.m3u8`
4. Click **Play**

#### Method 3: Using HTML (For Web Developers)

**Basic HTML5 video tag:**
```html
<video controls width="640">
  <source src="http://your-ip:8888/front_door/stream.m3u8" type="application/x-mpegURL">
</video>
```

**Using Video.js (Recommended for better browser compatibility):**
```html
<link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
<script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>

<video id="my-camera" class="video-js" controls preload="auto" width="640" height="480">
  <source src="http://your-ip:8888/front_door/stream.m3u8" type="application/x-mpegURL">
  <source src="http://192.168.1.100:8888/front_door/stream.m3u8" type="application/x-mpegURL">
</video>

<script>
  var player = videojs('my-camera');
</script>
```

### Testing Snapshots

#### In Your Web Browser

1. Open your browser
2. Enter the snapshot URL: `http://your-ip:5000/snapshot/camera-name.jpg`
   - Example: `http://your-ip:5000/snapshot/front_door.jpg`
3. You should see a still image from your camera

The snapshot updates automatically. To force a refresh, add a timestamp:
```
http://your-ip:5000/snapshot/camera-name.jpg?t=timestamp
```

### Testing WebRTC (Lowest Latency)

**Access via Web UI:**
1. Open the Web UI: `http://your-ip:5000`
2. Click on any camera
3. The stream will automatically use WebRTC for the lowest latency

**Requirements:**
- Port 8889 (TCP) must be open
- Port 8189 (UDP) must be open
- `WB_IP` environment variable must be set to your server IP

## Common Use Cases

### OctoPrint Integration

**Method 1: Using Snapshots (Recommended - Simpler)**

1. In OctoPrint, go to **Settings** → **Webcam & Timelapse**
2. Set these values:
   - **Stream URL:** `http://your-ip:5000/snapshot/camera-name.jpg`
   - **Snapshot URL:** `http://your-ip:5000/snapshot/camera-name.jpg`
3. Click **Test** to verify
4. Adjust frame rate if needed (1-15 fps recommended for snapshots)

**Method 2: Using HLS Stream (Video)**

1. Install an OctoPrint plugin that supports custom URLs:
   - Go to **Settings** → **Plugin Manager**
   - Search for "WebcamTab" or similar plugins
2. Configure the stream:
   - **Stream URL:** `http://your-ip:8888/camera-name/`
3. Enable "Embed stream" if available

### Home Assistant Integration

**Using Snapshots:**
```yaml
camera:
  - platform: generic
    name: "Front Door Camera"
    still_image_url: http://your-ip:5000/snapshot/front_door.jpg
```

**Using RTSP (Recommended for recording):**
```yaml
camera:
  - platform: generic
    name: "Front Door Camera"
    stream_source: rtsp://your-ip:8554/front_door
    still_image_url: http://your-ip:5000/snapshot/front_door.jpg
```

**What to do:**
1. Open `configuration.yaml` in a text editor
2. Add the camera configuration above
3. Replace `your-ip` with your actual IP address
4. Replace `front_door` with your actual camera name
5. Save the file
6. Restart Home Assistant:
   - **Web UI:** Developer Tools → YAML → Restart
   - **Command Line:** `ha core restart` (Home Assistant OS)

**Easier method:** Use the Web UI export feature at `http://your-ip:5000` to auto-generate the camera config!

### Web Dashboard/Iframe Integration

**For custom dashboards (Grafana, etc.):**

```html
<!-- HLS Stream -->
<iframe src="http://your-ip:8888/camera-name/" width="640" height="480"></iframe>

<!-- Snapshot -->
<img src="http://your-ip:5000/snapshot/camera-name.jpg" width="640" height="480" />
```

## Troubleshooting

### HLS Stream Not Loading

**Check 1: Verify the URL is accessible**

**Where to run:** Command Prompt/Terminal

```bash
curl http://your-ip:8888/camera-name/
```

You should see HTML or M3U8 playlist content.

**Check 2: Verify port 8888 is exposed**

Check your `docker-compose.yml` includes:
```yaml
ports:
  - 8888:8888
```

**Check 3: Check bridge logs**

**Where to run:** Command Prompt/Terminal

```bash
docker-compose logs wyze-bridge
```

**Check 4: Test with VLC**

- Open VLC → Media → Open Network Stream
- Enter: `http://your-ip:8888/camera-name/stream.m3u8`
- Click Play

### Snapshots Not Updating

**Check 1: Verify snapshot URL**

Open in your browser:
```
http://your-ip:5000/snapshot/camera-name.jpg
```

You should see a camera image.

**Check 2: Verify camera name**

- Camera names use underscores instead of spaces
- "Front Door" becomes "front_door"
- Check the Web UI at `http://your-ip:5000` for correct names

**Check 3: Verify port 5000 is exposed**

Check your `docker-compose.yml` includes:
```yaml
ports:
  - 5000:5000
```

### WebRTC Not Working

**Check 1: Verify WB_IP is set**

Check your `docker-compose.yml` or `.env` file has:
```yaml
environment:
  - WB_IP=your-ip  # Your actual server IP
```

**Check 2: Verify WebRTC ports are open**

```yaml
ports:
  - 8889:8889      # WebRTC
  - 8189:8189/udp  # WebRTC/ICE
```

**Check 3: Restart the bridge**

```bash
docker-compose restart
```

### CORS Issues (Cross-Origin Errors)
#### In OctoPrint
1. Install the "OctoPrint-Dashboard" or "OctoPrint-WebcamTab" plugin
2. Use the HLS URL format: `http://YOUR-IP:8888/camera-name/`
3. Or use the snapshot URL (see below) for a simpler setup

### HLS Stream Files

The HLS stream provides these files:
- **Main playlist:** `http://ip:8888/camera-name/stream.m3u8`
- **Direct stream:** `http://ip:8888/camera-name/`

Both URLs work, but the directory URL (`/camera-name/`) is simpler and automatically serves the playlist.

## HTTP Snapshots

For applications that only need still images (like OctoPrint), use the snapshot endpoint.

### Snapshot URLs

**Format:** `http://YOUR-IP:5000/snapshot/camera-name.jpg`

**Examples:**
```
http://192.168.1.100:5000/snapshot/front_door.jpg
http://192.168.1.100:5000/snapshot/3d_printer.jpg
```

### Using Snapshots

#### In OctoPrint
1. Go to Settings → Webcam & Timelapse
2. Set "Stream URL" to: `http://YOUR-IP:5000/snapshot/camera-name.jpg`
3. Set "Snapshot URL" to the same URL
4. Click "Test" to verify

#### In Home Assistant
```yaml
camera:
  - platform: generic
    name: "Camera Name"
    still_image_url: http://192.168.1.100:5000/snapshot/camera-name.jpg
```

#### Refresh Rate
The snapshot updates automatically. To force a refresh, add a timestamp parameter:
```
http://192.168.1.100:5000/snapshot/camera-name.jpg?t=timestamp
```

## WebRTC Streaming

For the lowest latency browser streaming, use WebRTC through the Web UI.

### Accessing WebRTC

1. Open the Web UI: `http://YOUR-IP:5000`
2. Click on any camera
3. The stream will automatically use WebRTC for the lowest latency

### WebRTC Configuration

Add these to your docker-compose.yml:
```yaml
ports:
  - 8889:8889      # WebRTC
  - 8189:8189/udp  # WebRTC/ICE
environment:
  - WB_IP=192.168.1.100  # Your server IP
```

## Web UI Integration

The Web UI (port 5000) provides a complete interface with:
- Live camera previews
- One-click stream access
- Copy RTSP/HLS URLs to clipboard
- Test streams directly in VLC
- Export all stream URLs

Access at: `http://YOUR-IP:5000`

## OctoPrint Setup (Detailed)

### Method 1: Using HLS Stream (Video)

1. Install OctoPrint plugin (if needed):
   - Go to Settings → Plugin Manager
   - Search for "WebcamTab" or similar plugins that support custom URLs

2. Configure the stream:
   - Settings → Webcam & Timelapse
   - Stream URL: `http://YOUR-IP:8888/camera-name/`
   - Enable "Embed stream" if available

### Method 2: Using Snapshots (Simpler, Recommended)

1. Configure OctoPrint:
   - Settings → Webcam & Timelapse
   - Stream URL: `http://YOUR-IP:5000/snapshot/camera-name.jpg`
   - Snapshot URL: (same as above)
   - Optional: Increase refresh rate if needed

2. Test the configuration:
   - Click "Test" button in OctoPrint settings
   - Should see your camera feed

3. Adjust settings:
   - Set appropriate frame rate (1-15 fps recommended for snapshots)
   - Adjust resolution if needed

## Browser Compatibility

### HLS Support

| Browser | HLS Support | Notes |
|---------|-------------|-------|
| Safari | ✅ Native | Works out of the box |
| Chrome | ✅ Via library | Requires video.js or hls.js |
| Firefox | ✅ Via library | Requires video.js or hls.js |
| Edge | ✅ Via library | Requires video.js or hls.js |
| Mobile Safari | ✅ Native | Works out of the box |
| Chrome Android | ✅ Via library | Requires video.js or hls.js |

### Using hls.js for Better Browser Support

```html
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<video id="video" controls width="640"></video>
<script>
  var video = document.getElementById('video');
  var videoSrc = 'http://192.168.1.100:8888/front_door/stream.m3u8';
  
  if (video.canPlayType('application/vnd.apple.mpegurl')) {
    // Native HLS support (Safari)
    video.src = videoSrc;
  } else if (Hls.isSupported()) {
    // Use hls.js for other browsers
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
  }
</script>
```

## Camera Names and URLs

Your camera streams will be available at:
- **HLS:** `http://your-ip:8888/camera-name/`
- **Snapshots:** `http://your-ip:5000/snapshot/camera-name.jpg`
- Replace spaces in camera names with underscores
- Example: "Front Door" becomes "front_door"

Check the Web UI at http://your-ip:5000 to see all available camera names and their URLs.

## Port Reference

| Port | Service | Description |
|------|---------|-------------|
| **5000** | Web UI | Camera management, snapshots, export features |
| **8554** | RTSP | Traditional RTSP streams (for VLC, NVRs) |
| **8888** | HLS | HTTP Live Streaming (browser compatible) |
| **8889** | WebRTC | Low-latency WebRTC (browser compatible) |
| **8189** | WebRTC/ICE | WebRTC ICE protocol (UDP, for WebRTC) |

## Security Considerations

When using HTTP streams:

**1. Enable authentication:**
```yaml
environment:
  - WB_AUTH=true
  - WB_PASSWORD=your-secure-password
```

**2. Keep streams on local network:**
- Use local network IPs only (192.168.x.x or 10.0.x.x)
- Don't expose ports directly to the internet
- Use a VPN for remote access

**3. Use a reverse proxy for remote access:**
- Set up nginx or similar with authentication
- Use HTTPS for encrypted connections
- Never forward ports directly to the internet without security

## Logs and Debugging

**Where to run:** Command Prompt, PowerShell, or Terminal

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

## Advanced: Custom Integration

### Embedding in Dashboards

For custom dashboards (Home Assistant, Grafana, etc.):

```html
<!-- HLS Stream -->
<iframe src="http://YOUR-IP:8888/camera-name/" width="640" height="480"></iframe>

<!-- Snapshot -->
<img src="http://YOUR-IP:5000/snapshot/camera-name.jpg" width="640" height="480" />
```

### Using with Home Assistant

See [RTSP-SETUP.md](RTSP-SETUP.md#home-assistant) for complete Home Assistant integration, or use:

```yaml
camera:
  - platform: generic
    name: "Front Door"
    stream_source: rtsp://YOUR-IP:8554/front_door  # For recording
    still_image_url: http://YOUR-IP:5000/snapshot/front_door.jpg
```

### API Access

The Web UI also provides API endpoints:

- **All cameras:** `http://YOUR-IP:5000/api/cameras`
- **RTSP URLs:** `http://YOUR-IP:5000/api/rtsp/urls`
- **Export streams:** `http://YOUR-IP:5000/api/rtsp/export?format=json`

## Summary

**For OctoPrint and similar tools:**
- Use snapshots: `http://ip:5000/snapshot/camera-name.jpg`

**For web browsers:**
- Use HLS: `http://ip:8888/camera-name/`
- Or use the Web UI: `http://ip:5000`

**For lowest latency:**
- Use WebRTC via the Web UI at `http://ip:5000`

**For traditional NVRs and Home Assistant:**
- Use RTSP: `rtsp://ip:8554/camera-name` (see [RTSP-SETUP.md](RTSP-SETUP.md))

---

For more information, see [RTSP Setup Guide](RTSP-SETUP.md).
