#!/bin/bash

echo "Running build script..."
python3 -m pip install --upgrade pip
# If your scripts had external dependencies, you would list them here, e.g.:
# pip install -r requirements.txt
python3 /root/DEVICE_BACKUP/main.py