# Security Policy

## Supported Versions

This fork follows the upstream release cycle. Only the latest version receives security updates.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Older   | :x:                |

We recommend always using the latest release to ensure you have all security patches.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability, please send an email to the repository maintainer with:

1. A description of the vulnerability
2. Steps to reproduce the issue
3. Potential impact assessment
4. Suggested fix (if you have one)

### What to Expect

- **Acknowledgment**: Within 24-48 hours
- **Initial Assessment**: Within 1 week
- **Status Updates**: Every 5-7 days until resolved
- **Resolution Timeline**: Depends on severity
  - Critical: 1-3 days
  - High: 1-2 weeks
  - Medium: 2-4 weeks
  - Low: Best effort

### Disclosure Policy

- Security issues will be kept confidential until a fix is released
- We will credit researchers who report vulnerabilities (unless they prefer to remain anonymous)
- A security advisory will be published after the fix is available
- Users will be notified through GitHub releases and repository announcements

## Security Best Practices

### Network Security

⚠️ **IMPORTANT**: Do NOT expose the bridge directly to the internet without proper security measures.

1. **Use behind a firewall**: Keep the bridge on your local network
2. **VPN Access**: Use VPN for remote access instead of port forwarding
3. **Reverse Proxy**: If exposing streams, use a reverse proxy with authentication
4. **Network Segmentation**: Consider isolating cameras on a separate VLAN

### Authentication

1. **Change default credentials**: Always set custom `WB_PASSWORD` and `WB_API`
2. **Use strong passwords**: Minimum 12 characters with mixed case, numbers, and symbols
3. **Enable STREAM_AUTH**: Protect streams with authentication
4. **Rotate credentials**: Change passwords periodically

### Docker Security

1. **Don't run as root**: Use user namespaces if possible
2. **Limit capabilities**: Only grant necessary capabilities
3. **Read-only filesystem**: Mount volumes as read-only when possible
4. **Resource limits**: Set memory and CPU limits
5. **Keep updated**: Regularly update Docker and the bridge image

### Credential Management

1. **Use environment files**: Store credentials in `.env` files (not in docker-compose.yml)
2. **Set proper permissions**: `chmod 600 .env` to restrict access
3. **Use secrets**: Consider Docker secrets for production deployments
4. **Don't commit secrets**: Add `.env` to `.gitignore`
5. **API Keys**: Keep Wyze API keys secure and don't share them

### Monitoring

1. **Check logs regularly**: Monitor for unusual activity
2. **Review access**: Check who's accessing your streams
3. **Network monitoring**: Watch for unexpected connections
4. **Update notifications**: Enable notifications for new releases

## Known Security Considerations

### Wyze Credentials

- The bridge requires your Wyze credentials to authenticate with cameras
- Credentials are used only to communicate with Wyze services and cameras
- We recommend using the Wyze API Key method (more secure than username/password)
- Consider creating a separate Wyze account for the bridge if you're concerned

### Camera Access

- Cameras connect using Wyze's TUTK P2P protocol
- Local LAN connections are preferred and more secure than P2P
- Some traffic may go through Wyze servers depending on connection mode
- See the [wiki](https://github.com/mrlt8/docker-wyze-bridge/wiki/Network-Connection-Modes) for connection details

### Stream Security

- Unencrypted streams (RTSP) can be intercepted on your network
- WebRTC offers encryption for streams
- Use `STREAM_AUTH` to require authentication for stream access
- Consider using RTSP over TLS if your client supports it

### WebUI Security

- The WebUI is HTTP by default (not HTTPS)
- Use a reverse proxy with HTTPS if exposing externally
- Enable authentication (`WB_PASSWORD` and optionally `WB_API`)
- Consider IP whitelisting through your reverse proxy

## Secure Configuration Examples

### Basic Secure Setup

```yaml
version: '3'
services:
  wyze-bridge:
    container_name: wyze-bridge
    image: mrlt8/wyze-bridge:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:8554:8554"  # RTSP - localhost only
      - "127.0.0.1:5000:5000"  # WebUI - localhost only
    environment:
      - WYZE_EMAIL=${WYZE_EMAIL}
      - WYZE_PASSWORD=${WYZE_PASSWORD}
      - WB_PASSWORD=${WB_PASSWORD}
      - STREAM_AUTH=user:strongpass
      - SNAPSHOT_TYPE=api
    env_file:
      - .env
    volumes:
      - ./tokens:/tokens
```

### Production Setup with Reverse Proxy

Use nginx or Traefik with:
- HTTPS/TLS certificates (Let's Encrypt)
- Strong authentication
- Rate limiting
- IP whitelisting
- Security headers

## Upstream Security

This fork inherits security considerations from the upstream project:
- [Upstream Security](https://github.com/mrlt8/docker-wyze-bridge/security)
- [Upstream Issues](https://github.com/mrlt8/docker-wyze-bridge/issues)

Please check upstream for any known security advisories.

## Dependency Security

We monitor dependencies for known vulnerabilities:
- Python packages in `requirements.txt`
- Base Docker images
- Third-party libraries

### Reporting Dependency Issues

If you discover a vulnerable dependency:
1. Check if it's already reported upstream
2. Report it through the security process above
3. If urgent, also create a private security advisory on GitHub

## Security Checklist

Before deploying in production:

- [ ] Changed default credentials
- [ ] Enabled authentication (WB_PASSWORD, STREAM_AUTH)
- [ ] Limited network exposure (localhost or VPN only)
- [ ] Using `.env` file for credentials (not in docker-compose.yml)
- [ ] Set proper file permissions (chmod 600 .env)
- [ ] Using latest bridge version
- [ ] Reviewed security logs
- [ ] Configured firewall rules
- [ ] Set up HTTPS if accessible remotely
- [ ] Documented access procedures
- [ ] Tested backup/recovery process

## Additional Resources

- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Upstream Wiki - Security](https://github.com/mrlt8/docker-wyze-bridge/wiki)

## Questions?

For non-security questions:
- Open a GitHub Issue
- Check the documentation
- Review closed issues

For security concerns, use the private reporting method described above.

Thank you for helping keep this project secure! 🔒
