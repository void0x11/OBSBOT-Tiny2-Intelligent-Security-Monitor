"""
Cache YOLOv8 Model Locally for Faster EXE Startup
Run this ONCE before building the PyInstaller EXE
"""

import os
from pathlib import Path
from ultralytics import YOLO

print("=" * 60)
print("YOLOv8 Model Caching for OBSBOT Monitor")
print("=" * 60)
print()

# Create models directory in project root
models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

print("[1/2] Downloading YOLOv8 Nano model...")
print("      This may take 2-3 minutes on first run")
print()

try:
    # Download and cache the model
    model = YOLO("yolov8n.pt")
    
    # Verify model loaded
    print("[2/2] Model cached successfully!")
    print()
    print("=" * 60)
    print("SUCCESS! Model is now cached locally")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Build PyInstaller: build_windows.bat")
    print("2. First startup will be FAST (model already cached)")
    print()
    
except Exception as e:
    print(f"ERROR: {e}")
    print()
    print("Make sure you have internet connection to download the model")
