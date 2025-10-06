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

## HLS Streaming (HTTP Live Streaming)

HLS is the recommended option for browser-based streaming and tools that need HTTP URLs.

### Accessing HLS Streams

**Format:** `http://YOUR-IP:8888/camera-name/`

**Examples:**
```
http://192.168.1.100:8888/front_door/
http://192.168.1.100:8888/garage_camera/
http://192.168.1.100:8888/back_yard/
```

### Using HLS Streams

#### In Web Browsers
Simply open the URL in your browser. The stream will play using the browser's built-in HLS player.

#### In HTML Pages
```html
<video controls width="640">
  <source src="http://192.168.1.100:8888/front_door/stream.m3u8" type="application/x-mpegURL">
</video>
```

#### With Video.js (Recommended)
```html
<link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
<script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>

<video id="my-camera" class="video-js" controls preload="auto" width="640" height="480">
  <source src="http://192.168.1.100:8888/front_door/stream.m3u8" type="application/x-mpegURL">
</video>

<script>
  var player = videojs('my-camera');
</script>
```

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

## Troubleshooting

### HLS Stream Not Loading

1. **Check the URL is accessible:**
   ```bash
   curl http://YOUR-IP:8888/camera-name/
   ```
   
2. **Verify port 8888 is exposed:**
   - Check docker-compose.yml includes: `- 8888:8888`

3. **Check bridge logs:**
   ```bash
   docker logs wyze-bridge
   ```

4. **Test with VLC:**
   - Open VLC → Media → Open Network Stream
   - Enter: `http://YOUR-IP:8888/camera-name/stream.m3u8`

### Snapshots Not Updating

1. **Verify snapshot URL:**
   - Open in browser: `http://YOUR-IP:5000/snapshot/camera-name.jpg`
   - Should see a camera image

2. **Check camera name:**
   - Camera names use underscores instead of spaces
   - "Front Door" becomes "front_door"
   - Check Web UI at `http://YOUR-IP:5000` for correct names

3. **Check port 5000 is exposed:**
   - docker-compose.yml should have: `- 5000:5000`

### CORS Issues

If you're embedding streams in another website and get CORS errors:

1. The bridge allows CORS by default for HLS streams
2. If issues persist, check your reverse proxy configuration
3. For development, you may need to disable browser CORS checks

## Port Reference

| Port | Service | Description |
|------|---------|-------------|
| 5000 | Web UI | Camera management, snapshots |
| 8554 | RTSP | Traditional RTSP streams (not browser compatible) |
| 8888 | HLS | HTTP Live Streaming (browser compatible) |
| 8889 | WebRTC | Low-latency WebRTC (browser compatible) |
| 8189 | WebRTC/ICE | WebRTC ICE protocol (UDP) |

## Security Considerations

When exposing HTTP streams:

1. **Use authentication:**
   ```yaml
   environment:
     - WB_AUTH=true
     - WB_PASSWORD=your-password
   ```

2. **Don't expose to the internet** without proper security:
   - Use a VPN for remote access
   - Or use a reverse proxy with authentication
   - Never forward ports directly to the internet

3. **Use local network only:**
   - Keep streams on your local network (192.168.x.x or 10.0.x.x)
   - Access remotely via VPN

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
- Use WebRTC via the Web UI

**For traditional NVRs and Home Assistant:**
- Use RTSP: `rtsp://ip:8554/camera-name`

---

For more information:
- [Quick Start Guide](QUICK_START.md)
- [RTSP Setup Guide](RTSP-SETUP.md)
- [Complete Setup Guide](SETUP_GUIDE.md)
