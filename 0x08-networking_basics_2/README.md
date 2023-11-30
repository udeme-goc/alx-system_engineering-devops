# 0x08. Networking basics #1

## Description

This repository contains scripts and tools for basic networking tasks on Ubuntu 20.04 LTS. These scripts are designed to help with tasks related to IP configuration, host resolution, and port listening.

## Author

- Udeme Harrison
- GitHub: [udeme-goc](https://github.com/udeme-goc)

## Scripts

1. **Change Your Home IP (`0-change_your_home_IP`):**
   - This script modifies the `/etc/hosts` file to change the resolution of `localhost` and `facebook.com`.

2. **Show Attached IPs (`1-show_attached_IPs`):**
   - This script displays all active IPv4 IPs on the machine it's executed on.

3. **Port Listening on Localhost (`100-port_listening_on_localhost`):**
   - This script listens on port 98 on localhost, providing a tool for debugging and testing network connections.

## Usage

### Change Your Home IP
```bash
sudo ./0-change_your_home_IP
```

### Show Attached IPs
```bash
./1-show_attached_IPs
```

### Port Listening on Localhost
```bash
sudo ./100-port_listening_on_localhost
```

## Note
    - Use caution when running scripts that modify system configurations.
    - Ensure proper permissions and backup critical files before making changes.
