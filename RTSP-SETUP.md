# Wyze Bridge RTSP Setup Guide

## Quick Setup Steps

### 1. Get Your Wyze API Credentials
1. Go to https://developer-api-console.wyze.com/
2. Create an account and generate API keys
3. Note down your `API_ID` and `API_KEY`

### 2. Configure Your Environment
1. Copy `.env.template` to `.env`
2. Edit `.env` with your credentials and network settings:
   ```bash
   cp .env.template .env
   # Edit .env with your favorite text editor
   ```

### 3. Find Your Network IP
Run one of these commands to find your local IP:
- Windows: `ipconfig`
- Linux/Mac: `ip addr show` or `ifconfig`

Update `WB_IP` in your `.env` file with this IP address.

### 4. Start the Bridge
```bash
docker-compose up -d
```

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

### VLC Media Player
1. Open VLC
2. Go to Media > Open Network Stream
3. Enter: `rtsp://your-ip:8554/panv3`
4. Click Play

### FFmpeg Command Line
```bash
ffplay rtsp://your-ip:8554/panv3
```

### Home Assistant
Add to your `configuration.yaml`:
```yaml
camera:
  - platform: generic
    name: "Pan V3 Camera"
    stream_source: rtsp://your-ip:8554/panv3
    still_image_url: http://your-ip:5000/img/panv3.jpg
```

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

Check logs:
```bash
docker-compose logs -f wyze-bridge
```

If you still see timeout errors, try increasing `CONNECT_TIMEOUT` to 90 or 120 seconds in your `.env` file.