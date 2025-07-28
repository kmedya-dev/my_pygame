#!/bin/bash

echo "Running build script..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Run the Flask application
python3 ./main.py