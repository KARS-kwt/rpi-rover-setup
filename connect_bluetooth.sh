#!/bin/bash

# Replace XX:XX:XX:XX:XX:XX with your Bluetooth device MAC address
DEVICE_MAC="E3:23:B0:B1:7F:4A"
# DEVICE_MAC="EB:F3:9A:25:FB:22"

# Start bluetoothctl, then connect to the device
echo -e "power on\nagent on\ndefault-agent\nscan on\nconnect $DEVICE_MAC\nscan off\nexit" | bluetoothctl
