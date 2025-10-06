[![Docker](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works/actions/workflows/docker-image.yml/badge.svg)](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works/actions/workflows/docker-image.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mrlt8/docker-wyze-bridge?logo=github&label=upstream%20release)](https://github.com/mrlt8/docker-wyze-bridge/releases/latest)
[![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/mrlt8/wyze-bridge?sort=semver&logo=docker&logoColor=white&label=upstream%20image)](https://hub.docker.com/r/mrlt8/wyze-bridge)
[![Docker Pulls](https://img.shields.io/docker/pulls/mrlt8/wyze-bridge?logo=docker&logoColor=white&label=upstream%20pulls)](https://hub.docker.com/r/mrlt8/wyze-bridge)

# WebRTC/RTSP/RTMP/HLS Bridge for Wyze Cam

> [!NOTE]
> ## About This Fork
> This is an actively maintained fork of [mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge). We stay synchronized with upstream releases and aim to provide:
> - 📦 Regular updates synced with upstream
> - 📚 Enhanced documentation and guides
> - 🤝 Responsive community support
> - 🔒 Security best practices
>
> **Current Version**: v2.10.3 (synced with upstream)
>
> **New to this project?** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute, [MAINTENANCE.md](MAINTENANCE.md) for maintenance procedures, and [SECURITY.md](SECURITY.md) for security guidelines.

![479shots_so](https://user-images.githubusercontent.com/67088095/224595527-05242f98-c4ab-4295-b9f5-07051ced1008.png)


Create a local WebRTC, RTSP, RTMP, or HLS/Low-Latency HLS stream for most of your Wyze cameras including the outdoor, doorbell, and 2K cams. 

No modifications, third-party, or special firmware required.

It just works!

Streams direct from camera without additional bandwidth or subscriptions.

Please consider ⭐️ starring this project if you found it useful, or [☕️ sponsor the original author](https://ko-fi.com/mrlt8) who created this excellent project!


> [!IMPORTANT]
> As of May 2024, you will need an API Key and API ID from: https://support.wyze.com/hc/en-us/articles/16129834216731.

> [!WARNING]
> Please double check your router/firewall and do NOT forward ports or enable DMZ access to the bridge unless you know what you are doing!


![Wyze Cam V1](https://img.shields.io/badge/wyze_v1-yes-success.svg)
![Wyze Cam V2](https://img.shields.io/badge/wyze_v2-yes-success.svg)
![Wyze Cam V3](https://img.shields.io/badge/wyze_v3-yes-success.svg)
![Wyze Cam V3 Pro](https://img.shields.io/badge/wyze_v3_pro-yes-success.svg)
![Wyze Cam V4](https://img.shields.io/badge/wyze_v4-yes-success.svg)
![Wyze Cam Floodlight](https://img.shields.io/badge/wyze_floodlight-yes-success.svg)
![Wyze Cam Floodlight V2](https://img.shields.io/badge/wyze_floodlight_v2-yes-success.svg)
![Wyze Cam Pan](https://img.shields.io/badge/wyze_pan-yes-success.svg)
![Wyze Cam Pan V2](https://img.shields.io/badge/wyze_pan_v2-yes-success.svg)
![Wyze Cam Pan V3](https://img.shields.io/badge/wyze_pan_v3-yes-success.svg)
![Wyze Cam Pan Pro](https://img.shields.io/badge/wyze_pan_pro-yes-success.svg)
![Wyze Cam Outdoor](https://img.shields.io/badge/wyze_outdoor-yes-success.svg)
![Wyze Cam Outdoor V2](https://img.shields.io/badge/wyze_outdoor_v2-yes-success.svg)
![Wyze Cam Doorbell](https://img.shields.io/badge/wyze_doorbell-yes-success.svg)
![Wyze Cam Doorbell V2](https://img.shields.io/badge/wyze_doorbell_v2-yes-success.svg)

See the [supported cameras](#supported-cameras) section for additional information.


## 🚀 Quick Start

**New to Wyze Bridge?** Check out our guides:

- 🔧 **[RTSP Setup Guide](RTSP-SETUP.md)** - Complete setup guide for RTSP streaming
- 🌐 **[HTTP/Browser Streaming Guide](HTTP-STREAMING.md)** - Setup guide for HLS, WebRTC, and browser-compatible streams
- 💻 **[Command Reference](COMMAND_REFERENCE.md)** - Quick reference for where to run commands
- 💻 **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to this project
- 📖 **[Quick Start Guide](QUICK_START.md)** - Get streaming in 5 minutes! (Includes prerequisite setup)
- 📚 **[Complete Setup Guide](SETUP_GUIDE.md)** - Comprehensive walkthrough with troubleshooting
- 🔧 **[RTSP Setup Guide](RTSP-SETUP.md)** - RTSP-specific configuration
- 🌐 **[HTTP/Browser Streaming Guide](HTTP-STREAMING.md)** - Browser-compatible streaming & OctoPrint integration
- 💻 **[Command Reference](COMMAND_REFERENCE.md)** - Quick reference for where to run commands

### 🤔 Which Guide Should I Use?

**Choose based on your situation:**

| If you... | Use this guide |
|-----------|---------------|
| 🆕 Are brand new to this project | → [Quick Start Guide](QUICK_START.md) |
| ❓ Don't know where to run commands | → [Command Reference](COMMAND_REFERENCE.md) |
| 🔧 Need detailed step-by-step help | → [Complete Setup Guide](SETUP_GUIDE.md) |
| 📺 Just want RTSP streaming quickly | → [RTSP Setup Guide](RTSP-SETUP.md) |
| 🌐 Need browser/HTTP streaming or OctoPrint | → [HTTP Streaming Guide](HTTP-STREAMING.md) |
| 💻 Want to contribute code | → [Contributing Guide](CONTRIBUTING.md) |
| ❌ Getting "command not found" errors | → [Command Reference](COMMAND_REFERENCE.md) |

> **📝 Note:** All commands in this guide should be run in your terminal/command prompt:
> - **Windows:** Command Prompt or PowerShell (NOT Python terminal)
> - **Mac/Linux:** Terminal application
> - **Not sure?** See the [Command Reference Guide](COMMAND_REFERENCE.md)

### Simple Setup (3 Steps)

**Prerequisites:** [Docker](https://docs.docker.com/get-docker/) and [Python 3](https://www.python.org/downloads/) installed

1. **Get API Credentials** from https://developer-api-console.wyze.com/
2. **Run Setup Wizard** (in Command Prompt/Terminal): 
   ```bash
   python3 app/wyzebridge/setup_wizard.py
   ```
3. **Start Bridge**:
   ```bash
   docker-compose up -d
   ```

Or follow the original quick start:

Install [docker](https://docs.docker.com/get-docker/) and run in your terminal/command prompt:

```bash
docker run -p 8554:8554 -p 8888:8888 -p 5050:5000 -e WB_AUTH=false mrlt8/wyze-bridge
```

You can then use the web interface at `http://localhost:5050` where `localhost` is the hostname or ip of the machine running the bridge.

See [basic usage](#basic-usage) for additional information or visit the [wiki page](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant) for additional information on using the bridge as a Home Assistant Add-on.

## What's Changed in v2.10.3

- FIX: Increased `MTX_WRITEQUEUESIZE` to prevent issues with higher bitrates.
- FIX: Restart RTMP livestream on fail (#1333)
- FIX: Restore user data on bridge restart (#1334)
- NEW: `SNAPSHOT_KEEP` Option to delete old snapshots when saving snapshots with a timelapse-like custom format with `SNAPSHOT_FORMAT`. (#1330)
  - Example for 3 min: `SNAPSHOT_KEEP=180`, `SNAPSHOT_KEEP=180s`, `SNAPSHOT_KEEP=3m`
  - Example for 3 days: `SNAPSHOT_KEEP=72h`, `SNAPSHOT_KEEP=3d`
  - Example for 3 weeks: `SNAPSHOT_KEEP=21d`, `SNAPSHOT_KEEP=3w`
- NEW: `RESTREAMIO` option for livestreaming via [restream.io](https://restream.io). (#1333)
  - Example `RESTREAMIO_FRONT_DOOR=re_My_Custom_Key123`

## What's Changed in v2.10.2

- FIX: day/night FPS slowdown for V4 cameras (#1287) Thanks @cdoolin and @Answer-1!
- NEW: Update battery level in WebUI

## What's Changed in v2.10.0/v2.10.1

FIXED: Could not disable `WB_AUTH` if `WB_API` is set. (#1304)

### WebUI Authentication

Simplify default credentials for the WebUI:

  - This will not affect users who are setting their own `WB_PASSWORD` and `WB_API`.
  - Default `WB_PASSWORD` will now be derived from the username part of the Wyze email address instead of using a randomly generated password.
    - Example: For the email address `john123@doe.com`, the `WB_PASSWORD` will be `john123`.
  - Default `WB_API` will be based on the wyze account for persistance.

### Stream Authentication

NEW: `STREAM_AUTH` option to specify multiple users and paths:

  - Username and password should be separated by a `:` 
  - An additional `:` can be used to specify the allowed IP address for the user. 
    - **This does NOT work with docker desktop**
    - Specify multiple IPs using a comma
  - Use the `@` to specify paths accessible to the user. 
    - Paths are optional for each user.  
    - Multiple paths can be specified by using a comma. If none are provided, the user will have access to all paths/streams 
  - Multiple users can be specified by using  `|` as a separator 

  **EXAMPLE**:

  ```
  STREAM_AUTH=user:pass@cam-1,other-cam|second-user:password@just-one-cam|user3:pass
  ```

  - `user:pass`  has access to `cam-1` and `other-cam`
  - `second-user:password` has access to `just-one-cam`
  - `user3:pass` has access to **all** paths/cameras

  See [Wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki/Authentication#custom-stream-auth) for more information and examples.

### Recording via MediaMTX

Recoding streams has been updated to use MediaMTX with the option to delete older clips. 

Use `RECORD_ALL` or `RECORD_CAM_NAME` to enable recording.

- `RECORD_PATH` Available variables are `%path` or `{cam_name}`, `%Y` `%m` `%d` `%H` `%M` `%S` `%f` `%s` (time in strftime format).
- `RECORD_LENGTH` Length of each clip. Use `s` for seconds , `h` for hours. Defaults to `60s`
- `RECORD_KEEP` Delete older clips. Use `s` for seconds , `h` for hours. Set to 0s to disable automatic deletion. Defaults to `0s`

[View previous changes](https://github.com/mrlt8/docker-wyze-bridge/releases)

## FAQ

* How does this work?
  * It uses the same SDK as the app to communicate directly with the cameras. See [kroo/wyzecam](https://github.com/kroo/wyzecam) for details.
* Does it use internet bandwidth when streaming?
  * Not in most cases. The bridge will attempt to stream locally if possible but will fallback to streaming over the internet if you're trying to stream from a different location or from a shared camera. See the [wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki/Network-Connection-Modes) for more details.
* Can I use this with OctoPrint or in a web browser?
  * Yes! RTSP doesn't work in browsers, but the bridge provides HLS (HTTP) streams on port 8888 and HTTP snapshots on port 5000 that work with browsers and OctoPrint. See the [HTTP Streaming Guide](HTTP-STREAMING.md) for details.
* Can this work offline/can I block all wyze services?
  * No. Streaming should continue to work without an active internet connection, but will probably stop working after some time as the cameras were not designed to be used without the cloud. Some camera commands also depend on the cloud and may not function without an active connection. See [wz_mini_hacks](https://github.com/gtxaspec/wz_mini_hacks/wiki/Configuration-File#self-hosted--isolated-mode) for firmware level modification to run the camera offline.
* Why aren't all wyze cams supported yet (OG/Doorbell Pro)?
  * These cameras are using a different SDK and will require a different method to connect and stream. See the awesome [cryze](https://github.com/carTloyal123/cryze) project by @carTloyal123.

## Compatibility

![Supports arm32v7 Architecture](https://img.shields.io/badge/arm32v7-yes-success.svg)
![Supports arm64v8 Architecture](https://img.shields.io/badge/arm64v8-yes-success.svg)
![Supports amd64 Architecture](https://img.shields.io/badge/amd64-yes-success.svg)
![Supports Apple Silicon Architecture](https://img.shields.io/badge/apple_silicon-yes-success.svg)

[![Home Assistant Add-on](https://img.shields.io/badge/home_assistant-add--on-blue.svg?logo=homeassistant&logoColor=white)](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant)
[![Homebridge](https://img.shields.io/badge/homebridge-camera--ffmpeg-blue.svg?logo=homebridge&logoColor=white)](https://sunoo.github.io/homebridge-camera-ffmpeg/configs/WyzeCam.html)
[![Portainer stack](https://img.shields.io/badge/portainer-stack-blue.svg?logo=portainer&logoColor=white)](https://github.com/mrlt8/docker-wyze-bridge/wiki/Portainer)
[![Unraid Community App](https://img.shields.io/badge/unraid-community--app-blue.svg?logo=unraid&logoColor=white)](https://github.com/mrlt8/docker-wyze-bridge/issues/236)

Should work on most x64 systems as well as on most modern arm-based systems like the Raspberry Pi 3/4/5 or Apple Silicon M1/M2/M3.

The container can be run on its own, in [Portainer](https://github.com/mrlt8/docker-wyze-bridge/wiki/Portainer), [Unraid](https://github.com/mrlt8/docker-wyze-bridge/issues/236), as a [Home Assistant Add-on](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant), locally or remotely in the cloud.



### Ubiquiti Unifi 

> [!NOTE]  
> Some network adjustments may be needed - see [this discussion](https://github.com/mrlt8/docker-wyze-bridge/discussions/891) for more information.

## Supported Cameras

> [!IMPORTANT]
> Some newer camera firmware versions may cause issues with remote access via P2P. Local "LAN" access seems unaffected at this time. A temporary solution is to use a VPN. See the [OpenVPN example](https://github.com/mrlt8/docker-wyze-bridge/blob/main/docker-compose.ovpn.yml).

| Camera                        | Model          | Tutk Support                                                 | Latest FW |
| ----------------------------- | -------------- | ------------------------------------------------------------ | --------- |
| Wyze Cam v1 [HD only]         | WYZEC1         | ✅                                                            | 3.9.4.x   |
| Wyze Cam V2                   | WYZEC1-JZ      | ✅                                                            | 4.9.9.x   |
| Wyze Cam V3                   | WYZE_CAKP2JFUS | ✅                                                            | 4.36.11.x |
| Wyze Cam V4 [2K]              | HL_CAM4        | ✅                                                            | 4.52.3.x  |
| Wyze Cam Floodlight           | WYZE_CAKP2JFUS | ✅                                                            | 4.36.11.x |
| Wyze Cam Floodlight V2 [2k]   | HL_CFL2        | ✅                                                            | 4.53.2.x  |
| Wyze Cam V3 Pro [2K]          | HL_CAM3P       | ✅                                                            | 4.58.11.x |
| Wyze Cam Pan                  | WYZECP1_JEF    | ✅                                                            | 4.10.9.x  |
| Wyze Cam Pan v2               | HL_PAN2        | ✅                                                            | 4.49.11.x |
| Wyze Cam Pan v3               | HL_PAN3        | ✅                                                            | 4.50.4.x  |
| Wyze Cam Pan Pro [2K]         | HL_PANP        | ✅                                                            | -         |
| Wyze Cam Outdoor              | WVOD1          | ✅                                                            | 4.17.4.x  |
| Wyze Cam Outdoor v2           | HL_WCO2        | ✅                                                            | 4.48.4.x  |
| Wyze Cam Doorbell             | WYZEDB3        | ✅                                                            | 4.25.1.x  |
| Wyze Cam Doorbell v2 [2K]     | HL_DB2         | ✅                                                            | 4.51.1.x  |
| Wyze Cam Doorbell Pro 2       | AN_RDB1        | ❓                                                            | -         |
| Wyze Battery Cam Pro          | AN_RSCW        | [⚠️](https://github.com/mrlt8/docker-wyze-bridge/issues/1011) | -         |
| Wyze Cam Flood Light Pro [2K] | LD_CFP         | [⚠️](https://github.com/mrlt8/docker-wyze-bridge/issues/822)  | -         |
| Wyze Cam Doorbell Pro         | GW_BE1         | [⚠️](https://github.com/mrlt8/docker-wyze-bridge/issues/276)  | -         |
| Wyze Cam OG                   | GW_GC1         | [⚠️](https://github.com/mrlt8/docker-wyze-bridge/issues/677)  | -         |
| Wyze Cam OG Telephoto 3x      | GW_GC2         | [⚠️](https://github.com/mrlt8/docker-wyze-bridge/issues/677)  | -         |

## Basic Usage

### docker-compose (recommended)

This is similar to the docker run command, but will save all your options in a yaml file.

**Prerequisites:** [Docker and Docker Compose](https://docs.docker.com/get-docker/) installed

**Where to run commands:** Terminal/Command Prompt (NOT Python terminal)

1. **Install Docker Compose** - [Installation Guide](https://docs.docker.com/compose/install/)
   - Check if installed: `docker-compose --version`

2. **Create your configuration:**
   - Download the [sample docker-compose.yml](https://raw.githubusercontent.com/mrlt8/docker-wyze-bridge/main/docker-compose.sample.yml)
   - Or use the provided `docker-compose.sample.yml` in this repository
   - Edit with a text editor (Notepad, VS Code, etc.) to add your Wyze credentials

3. **Start the bridge:**
   ```bash
   docker-compose up
   ```

Once you're happy with your config you can use `docker-compose up -d` to run it in detached mode (background).

> [!CAUTION]
> If your credentials contain a `$` character, you need to escape it with another `$` sign (e.g., `pa$$word` > `pa$$$$word`) or leave your credentials blank and use the webUI to login.

> [!NOTE] 
> You may need to [update the WebUI links](https://github.com/mrlt8/docker-wyze-bridge/wiki/WebUI#custom-ports) if you're changing the ports or using a reverse proxy.


#### Updating your container

**Where to run:** Terminal/Command Prompt (same place you ran docker-compose)

To update your container, navigate to the directory where your `docker-compose.yml` is located and run:

```bash
# Navigate to your project directory first
cd /path/to/docker-wyze-bridge-wrench-works

# Pull latest image
docker-compose pull

# Restart container in background
docker-compose up -d

# Clean up old images (optional)
docker image prune
```

### 🏠 Home Assistant

Visit the [wiki page](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant) for additional information on Home Assistant.

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fmrlt8%2Fdocker-wyze-bridge)


## Additional Info

* [Camera Commands (MQTT/REST API)](https://github.com/mrlt8/docker-wyze-bridge/wiki/Camera-Commands)
* [Two-Factor Authentication (2FA/MFA)](https://github.com/mrlt8/docker-wyze-bridge/wiki/Two-Factor-Authentication)
* [ARM/Apple Silicon/Raspberry Pi](https://github.com/mrlt8/docker-wyze-bridge/wiki/Raspberry-Pi-and-Apple-Silicon-(arm-arm64-m1-m2-m3))
* [Network Connection Modes](https://github.com/mrlt8/docker-wyze-bridge/wiki/Network-Connection-Modes)
* [Portainer](https://github.com/mrlt8/docker-wyze-bridge/wiki/Portainer)
* [Unraid](https://github.com/mrlt8/docker-wyze-bridge/issues/236)
* [Home Assistant](https://github.com/mrlt8/docker-wyze-bridge/wiki/Home-Assistant)
* [Homebridge Camera FFmpeg](https://sunoo.github.io/homebridge-camera-ffmpeg/configs/WyzeCam.html)
* [HomeKit Secure Video](https://github.com/mrlt8/docker-wyze-bridge/wiki/HomeKit-Secure-Video)
* [WebUI API](https://github.com/mrlt8/docker-wyze-bridge/wiki/WebUI-API)


## Web-UI

The bridge features a basic Web-UI which can display a preview of all your cameras as well as direct links to all the video streams.

The web-ui can be accessed on the default port `5000`:

```text
http://localhost:5000/
```

See also: 
* [WebUI page](https://github.com/mrlt8/docker-wyze-bridge/wiki/WebUI)
* [WebUI API page](https://github.com/mrlt8/docker-wyze-bridge/wiki/WebUI-API)


## WebRTC

WebRTC should work automatically in Home Assistant mode, however, some additional configuration is required to get WebRTC working in the standard docker mode.

- WebRTC requires two additional ports to be configured in docker:
  ```yaml
    ports:
      ...
      - 8889:8889 #WebRTC
      - 8189:8189/udp # WebRTC/ICE
    ```

- In addition, the `WB_IP` env needs to be set with the IP address of the server running the bridge.
  ```yaml
    environment:
      - WB_IP=192.168.1.116
  ```
- See [documentation](https://github.com/aler9/rtsp-simple-server#usage-inside-a-container-or-behind-a-nat) for additional information/options.

## Advanced Options

All environment variables are optional.

* [Audio](https://github.com/mrlt8/docker-wyze-bridge/wiki/Camera-Audio)
* [Bitrate and Resolution](https://github.com/mrlt8/docker-wyze-bridge/wiki/Camera-Bitrate-and-Resolution)
* [Camera Substreams](https://github.com/mrlt8/docker-wyze-bridge/wiki/Camera-Substreams)
* [MQTT Configuration](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#mqtt-config)
* [Filtering Cameras](https://github.com/mrlt8/docker-wyze-bridge/wiki/Camera-Filtering)
* [Doorbell/Camera Rotation](https://github.com/mrlt8/docker-wyze-bridge/wiki/Doorbell-and-Camera-Rotation)
* [Custom FFmpeg Commands](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#custom-ffmpeg-commands)
* [Interval Snapshots](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#snapshotstill-images)
* [Stream Recording and Livestreaming](https://github.com/mrlt8/docker-wyze-bridge/wiki/Stream-Recording-and-Livestreaming)
* [rtsp-simple-server/MediaMTX Config](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#mediamtx)
* [Offline/IFTTT Webhook](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#offline-camera-ifttt-webhook)
* [Proxy Stream from RTSP Firmware](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#proxy-stream-from-rtsp-firmware)
* [BOA HTTP Server/Motion Alerts](https://github.com/mrlt8/docker-wyze-bridge/wiki/Boa-HTTP-Server)
* [Debugging Options](https://github.com/mrlt8/docker-wyze-bridge/wiki/Advanced-Option#debugging-options)

## Other Wyze Projects

Honorable Mentions:

* [@noelhibbard's script](https://gist.github.com/noelhibbard/03703f551298c6460f2fd0bfdbc328bd#file-readme-md) - Original script that the bridge is bassd on.
* [kroo/wyzecam](https://github.com/kroo/wyzecam) - Original library that the bridge is based on.

Video Streaming:

* [gtxaspec/wz_mini_hacks](https://github.com/gtxaspec/wz_mini_hacks) - Firmware level modification for Ingenic based cameras with an RTSP server and [self-hosted mode](https://github.com/gtxaspec/wz_mini_hacks/wiki/Configuration-File#self-hosted--isolated-mode) to use the cameras without the wyze services.
* [thingino](https://github.com/themactep/thingino-firmware) - Advanced custom firmware for some Ingenic-based wyze cameras.
* [carTloyal123/cryze](https://github.com/carTloyal123/cryze) - Stream video from wyze cameras (Gwell cameras) that use the Iotvideo SDK from Tencent Cloud. 
* [xerootg/cryze_v2](https://github.com/xerootg/cryze_v2) - Stream video from wyze cameras (Gwell cameras) that use the Iotvideo SDK from Tencent Cloud. 
* [mnakada/atomcam_tools](https://github.com/mnakada/atomcam_tools) - Video streaming for Wyze v3.

General Wyze:

* [shauntarves/wyze-sdk](https://github.com/shauntarves/wyze-sdk) - python library to interact with wyze devices over the cloud.

---

## Fork-Specific Resources

### Documentation

This fork provides additional documentation to help maintain and contribute to the project:

- **[RTSP-SETUP.md](RTSP-SETUP.md)** - RTSP streaming setup guide
  - Prerequisites with installation instructions
  - Step-by-step RTSP configuration
  - Testing with VLC and FFmpeg
  - Home Assistant integration
  - Troubleshooting

- **[HTTP-STREAMING.md](HTTP-STREAMING.md)** - HTTP/Browser streaming setup guide
  - HLS streaming for web browsers
  - WebRTC for low-latency viewing
  - HTTP snapshots for OctoPrint
  - Testing and integration examples
  - Browser compatibility guide

- **[COMMAND_REFERENCE.md](COMMAND_REFERENCE.md)** - Command reference guide
  - Where to run different types of commands
  - Prerequisites checklist
  - Common tasks step-by-step
  - Troubleshooting "command not found" errors

- **[RTSP-SETUP.md](RTSP-SETUP.md)** - RTSP-specific setup
  - Quick RTSP configuration
  - Testing with VLC and FFmpeg
  - Home Assistant integration

- **[HTTP-STREAMING.md](HTTP-STREAMING.md)** - HTTP/Browser streaming guide
  - HLS streaming for web browsers
  - HTTP snapshots for OctoPrint
  - WebRTC low-latency streaming
  - Browser compatibility guide

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributing to this fork
  - How to report issues effectively
  - Development setup with prerequisites
  - Code style and PR guidelines
  - Relationship with upstream

- **[MAINTENANCE.md](MAINTENANCE.md)** - Maintainer procedures and schedules
  - Regular maintenance tasks (weekly, monthly, quarterly)
  - Syncing with upstream
  - Release process
  - Issue and PR management

- **[SECURITY.md](SECURITY.md)** - Security best practices and reporting
  - Network security recommendations
  - Authentication best practices
  - Secure configuration examples
  - Vulnerability reporting process

- **[CHANGELOG.md](CHANGELOG.md)** - Fork-specific changes and updates
  - Track fork maintenance activities
  - Document sync points with upstream
  - Version history

### Community & Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/allanwrench28/docker-wyze-bridge-wrench-works/issues)
- **Discussions**: For questions and community support
- **Upstream**: Check [mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge) for the original project

### Quick Troubleshooting Guide

#### Common Issues and Solutions

**Camera not connecting:**
1. Verify camera is online in Wyze app
2. Check `WYZE_EMAIL` and `WYZE_PASSWORD` are correct
3. Ensure API Key and API ID are set (required as of May 2024)
4. Review logs: `docker logs wyze-bridge`
5. Try restarting the container

**Stream not accessible:**
1. Check port mappings in docker-compose.yml
2. Verify firewall rules allow connections
3. Test locally first: `http://localhost:5000`
4. Enable `STREAM_AUTH` if needed for remote access

**Authentication issues:**
1. Get API Key and ID from https://support.wyze.com/hc/en-us/articles/16129834216731
2. Set `API_ID` and `API_KEY` environment variables
3. Clear tokens directory and restart: `rm -rf tokens/*`
4. Check for Wyze account 2FA settings

**Poor performance or stuttering:**
1. Check camera WiFi signal strength in Wyze app
2. Adjust bitrate: Set `QUALITY=HD` or `QUALITY=SD`
3. Reduce FPS if needed
4. Check Docker host resources (CPU, memory, network)

**Home Assistant integration issues:**
1. Ensure bridge is accessible from Home Assistant
2. Use correct stream URLs: `rtsp://ip:8554/camera-name`
3. Check HA logs for connection errors
4. Verify camera names match (no spaces, use hyphens)

For more detailed troubleshooting, see the [upstream wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki).

### Fork Maintenance Status

This fork is actively maintained with:
- Weekly checks for upstream updates
- Monthly reviews of issues and pull requests  
- Quarterly comprehensive testing and documentation updates

Last sync with upstream: **v2.10.3** (Allow self-signed certificates)

### Contributing to This Fork

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report issues
- Suggesting enhancements
- Submitting pull requests
- Development setup

Major features should ideally be contributed to [upstream](https://github.com/mrlt8/docker-wyze-bridge) first to benefit the entire community.

---

**Thank you to [@mrlt8](https://github.com/mrlt8) and all upstream contributors for creating and maintaining this excellent project!** 🙏
