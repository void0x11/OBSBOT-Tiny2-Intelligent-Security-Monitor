"""
OBSBOT Tiny2 - Windows PyInstaller Build Script (Python Only)
No batch files needed - just Python
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

print("\n" + "=" * 60)
print("OBSBOT Tiny2 Intelligent Security Monitor")
print("PyInstaller Windows Build")
print("=" * 60 + "\n")

# Check required files
required_files = [
    "main.py",
    "icon.ico",
    "cache_model.py",
    "requirements.txt"
]

print("[CHECK] Verifying required files...")
for file in required_files:
    if not Path(file).exists():
        print(f"  ❌ Missing: {file}")
        sys.exit(1)
    print(f"  ✓ Found: {file}")

print("\n[1/5] Checking PyInstaller installation...")
try:
    result = subprocess.run(["pyinstaller", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ PyInstaller installed: {result.stdout.strip()}")
    else:
        raise Exception("PyInstaller not found")
except Exception as e:
    print(f"  ❌ Error: PyInstaller not installed")
    print("  Run: pip install pyinstaller")
    sys.exit(1)

print("\n[2/5] Cleaning previous builds...")
try:
    if Path("build").exists():
        shutil.rmtree("build")
        print("  ✓ Removed build/ folder")
    if Path("dist").exists():
        shutil.rmtree("dist")
        print("  ✓ Removed dist/ folder")
    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"  ✓ Removed {spec_file.name}")
except Exception as e:
    print(f"  ⚠ Warning: {e}")

print("\n[3/5] Caching YOLOv8 model...")
try:
    print("  (This may take 2-3 minutes on first run)")
    result = subprocess.run([sys.executable, "cache_model.py"], capture_output=True, text=True)
    if result.returncode == 0:
        print("  ✓ Model cached successfully")
    else:
        print("  ⚠ Warning: Model cache incomplete (will download on first run)")
except Exception as e:
    print(f"  ⚠ Warning: {e}")

print("\n[4/5] Building PyInstaller EXE...")
print("  (This may take 10-15 minutes, please wait...)\n")

build_command = [
    "pyinstaller",
    "--onefile",
    "--windowed",
    "--icon=icon.ico",
    "--name=OBSBOT Tiny2 Intelligent Security Monitor",
    "--add-data=icon.ico:.",
    "--hidden-import=ultralytics",
    "--hidden-import=cv2",
    "--hidden-import=numpy",
    "--collect-all=ultralytics",
    "--noupx",
    "main.py"
]

try:
    result = subprocess.run(build_command, capture_output=False, text=True)
    if result.returncode != 0:
        print("\n  ❌ Build failed!")
        print("  Check the error messages above")
        sys.exit(1)
    print("\n  ✓ Build completed successfully")
except Exception as e:
    print(f"\n  ❌ Build error: {e}")
    sys.exit(1)

print("\n[5/5] Cleaning up temporary files...")
try:
    if Path("build").exists():
        shutil.rmtree("build")
        print("  ✓ Cleaned build/ folder")
    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"  ✓ Removed {spec_file.name}")
except Exception as e:
    print(f"  ⚠ Warning: {e}")

print("\n" + "=" * 60)
print("✅ BUILD SUCCESSFUL!")
print("=" * 60)
print("\nYour EXE is ready:")
exe_path = Path("dist") / "OBSBOT Tiny2 Intelligent Security Monitor.exe"
print(f"  📁 {exe_path}")

if exe_path.exists():
    file_size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"  📊 Size: {file_size_mb:.1f} MB")

print("\n✨ Features:")
print("  ✓ Icon in File Explorer")
print("  ✓ Icon in Taskbar")
print("  ✓ Icon in Window Title")
print("  ✓ Fast startup (5-10 seconds)")

print("\n📝 Notes:")
print("  - First run: 10-20 seconds (model loads)")
print("  - After first run: 5-10 seconds")
print("  - Double-click to run the app")

print("\n" + "=" * 60)
print("Ready to distribute! 🚀")
print("=" * 60 + "\n")

input("Press Enter to exit...")
