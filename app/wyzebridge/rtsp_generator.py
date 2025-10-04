"""
RTSP URL Generator for Wyze Bridge.

This module provides functionality to automatically generate RTSP URLs for all discovered cameras
and export them in various formats (YAML, JSON, plain text).
"""

import json
from typing import Dict, List, Optional
from pathlib import Path

import yaml
from wyzebridge.bridge_utils import env_bool
from wyzebridge.logging import logger


class RTSPURLGenerator:
    """Generator for RTSP URLs and camera configurations."""

    def __init__(self, hostname: str = "localhost", rtsp_port: int = 8554):
        """
        Initialize the RTSP URL Generator.

        Args:
            hostname: Bridge hostname or IP address
            rtsp_port: RTSP streaming port (default: 8554)
        """
        self.hostname = hostname
        self.rtsp_port = rtsp_port
        self.cameras: Dict[str, Dict] = {}

    def add_camera(self, name: str, nickname: str, model: str = "", 
                   mac: str = "", ip: str = "", enabled: bool = True) -> None:
        """
        Add a camera to the generator.

        Args:
            name: Camera URI name (sanitized)
            nickname: Camera display name
            model: Camera model
            mac: Camera MAC address
            ip: Camera IP address
            enabled: Whether camera is enabled
        """
        rtsp_url = f"rtsp://{self.hostname}:{self.rtsp_port}/{name}"
        rtmp_url = f"rtmp://{self.hostname}:1935/{name}"
        hls_url = f"http://{self.hostname}:8888/{name}/"
        webrtc_url = f"http://{self.hostname}:8889/{name}/"
        snapshot_url = f"http://{self.hostname}:5000/snapshot/{name}.jpg"
        
        self.cameras[name] = {
            "nickname": nickname,
            "model": model,
            "mac": mac,
            "ip": ip,
            "enabled": enabled,
            "rtsp_url": rtsp_url,
            "rtmp_url": rtmp_url,
            "hls_url": hls_url,
            "webrtc_url": webrtc_url,
            "snapshot_url": snapshot_url,
        }

    def get_rtsp_url(self, camera_name: str) -> Optional[str]:
        """Get RTSP URL for a specific camera."""
        if camera := self.cameras.get(camera_name):
            return camera.get("rtsp_url")
        return None

    def get_all_rtsp_urls(self) -> Dict[str, str]:
        """Get all RTSP URLs as a dictionary."""
        return {name: cam["rtsp_url"] for name, cam in self.cameras.items()}

    def export_text(self, filepath: Optional[Path] = None) -> str:
        """
        Export RTSP URLs as plain text.

        Args:
            filepath: Optional file path to save the output

        Returns:
            Plain text representation of RTSP URLs
        """
        lines = ["# Wyze Bridge RTSP URLs\n"]
        lines.append(f"# Generated for {self.hostname}:{self.rtsp_port}\n")
        lines.append("#\n")
        
        for name, cam in self.cameras.items():
            lines.append(f"# {cam['nickname']} ({cam['model']})\n")
            lines.append(f"{cam['rtsp_url']}\n")
            lines.append("\n")
        
        output = "".join(lines)
        
        if filepath:
            filepath.write_text(output)
            logger.info(f"[RTSP] Exported text to {filepath}")
        
        return output

    def export_json(self, filepath: Optional[Path] = None) -> str:
        """
        Export camera information as JSON.

        Args:
            filepath: Optional file path to save the output

        Returns:
            JSON representation of camera data
        """
        output = json.dumps({
            "hostname": self.hostname,
            "rtsp_port": self.rtsp_port,
            "cameras": self.cameras
        }, indent=2)
        
        if filepath:
            filepath.write_text(output)
            logger.info(f"[RTSP] Exported JSON to {filepath}")
        
        return output

    def export_yaml(self, filepath: Optional[Path] = None) -> str:
        """
        Export camera information as YAML.

        Args:
            filepath: Optional file path to save the output

        Returns:
            YAML representation of camera data
        """
        data = {
            "hostname": self.hostname,
            "rtsp_port": self.rtsp_port,
            "cameras": self.cameras
        }
        
        output = yaml.dump(data, default_flow_style=False, sort_keys=False)
        
        if filepath:
            filepath.write_text(output)
            logger.info(f"[RTSP] Exported YAML to {filepath}")
        
        return output

    def export_home_assistant_config(self, filepath: Optional[Path] = None) -> str:
        """
        Export Home Assistant camera configuration.

        Args:
            filepath: Optional file path to save the output

        Returns:
            Home Assistant YAML configuration
        """
        cameras_config = []
        
        for name, cam in self.cameras.items():
            if not cam["enabled"]:
                continue
                
            camera_config = {
                "platform": "generic",
                "name": cam["nickname"],
                "stream_source": cam["rtsp_url"],
                "still_image_url": cam["snapshot_url"],
                "verify_ssl": False,
            }
            cameras_config.append(camera_config)
        
        output = yaml.dump({"camera": cameras_config}, 
                          default_flow_style=False, 
                          sort_keys=False)
        
        if filepath:
            filepath.write_text(output)
            logger.info(f"[RTSP] Exported Home Assistant config to {filepath}")
        
        return output

    def generate_vlc_playlist(self, filepath: Optional[Path] = None) -> str:
        """
        Generate an M3U playlist for VLC.

        Args:
            filepath: Optional file path to save the output

        Returns:
            M3U playlist content
        """
        lines = ["#EXTM3U\n"]
        
        for name, cam in self.cameras.items():
            if not cam["enabled"]:
                continue
            
            lines.append(f"#EXTINF:-1,{cam['nickname']}\n")
            lines.append(f"{cam['rtsp_url']}\n")
        
        output = "".join(lines)
        
        if filepath:
            filepath.write_text(output)
            logger.info(f"[RTSP] Exported VLC playlist to {filepath}")
        
        return output

    def get_camera_count(self) -> int:
        """Get total number of cameras."""
        return len(self.cameras)

    def get_enabled_camera_count(self) -> int:
        """Get number of enabled cameras."""
        return sum(1 for cam in self.cameras.values() if cam["enabled"])

    def get_summary(self) -> Dict[str, any]:
        """Get summary of generated URLs."""
        return {
            "hostname": self.hostname,
            "rtsp_port": self.rtsp_port,
            "total_cameras": self.get_camera_count(),
            "enabled_cameras": self.get_enabled_camera_count(),
            "cameras": list(self.cameras.keys())
        }


def create_generator_from_streams(streams, hostname: str = None) -> RTSPURLGenerator:
    """
    Create an RTSPURLGenerator from a StreamManager.

    Args:
        streams: StreamManager instance
        hostname: Override hostname (defaults to WB_IP or localhost)

    Returns:
        RTSPURLGenerator instance
    """
    if hostname is None:
        hostname = env_bool("WB_IP", env_bool("DOMAIN", "localhost"))
    
    generator = RTSPURLGenerator(hostname=hostname)
    
    # Get all camera info from streams
    for cam_uri, cam_info in streams.get_all_cam_info().items():
        generator.add_camera(
            name=cam_uri,
            nickname=cam_info.get("nickname", cam_uri),
            model=cam_info.get("model", ""),
            mac=cam_info.get("mac", ""),
            ip=cam_info.get("ip", ""),
            enabled=cam_info.get("enabled", False)
        )
    
    return generator
