# Detection-Triggered Recorder

An **intelligent, event-driven surveillance system** that automatically captures video and screenshots upon detecting humans in real-time using AI-based vision processing.

---

## Overview

**Detection-Triggered Recorder** is a sophisticated **security monitoring** application, designed for **research** and **autonomous surveillance**. The system continuously monitors a USB-connected camera feed, performs real-time human detection with **YOLOv8**, and **initiates recording only when people are detected**. This event-driven approach significantly reduces storage requirements compared to traditional 24/7 recording while ensuring comprehensive event documentation.

---

## Key Features

### Core Functionality
- **Real-Time Human Detection**: YOLOv8 processes video frames at 30 FPS for immediate detection.
- **Automatic Recording**: Only records when humans are detected, optimizing storage.
- **Smart Cooldown Logic**: 5-second cooldown after detection to prevent fragmented clips.
- **Timestamped Snapshots**: Captures screenshots every 2 seconds during detection events.
- **Low CPU Usage**: Operates in standby mode, responding instantly to new detections.

### Recording Features
- **High-Quality Video**: 1920×1080 @ 30 FPS in MP4 format with H.264 encoding.
- **Automatic Timestamping**: Files are automatically timestamped in `YYYYMMDD_HHMMSS` format.
- **Efficient Storage**: Video files stored in a separate `recordings/` directory.
- **H.264 Compression**: Optimizes quality and file size.

### Screenshot Features
- **Event-Triggered Snapshots**: Images captured upon detection.
- **Timestamp Overlay**: Timestamps directly added to each image.
- **Organized Storage**: Saved in `snapshots/` directory with precise millisecond filenames.
- **Smart Snapshot Frequency**: Images taken every 2 seconds during detection to minimize duplicates.

### User Interface
- **Clean PyQt5 GUI**: Professional desktop interface with live video feed.
- **Status Indicators**: Displays detection status, recording status, and system health.
- **Camera Selection**: Easily select from available cameras with a dropdown menu.

---

## System Architecture

### Threading Model
- **CameraThread**: Captures frames from the camera at 30 FPS.
- **DetectionThread**: Runs YOLOv8 inference on captured frames.
- **RecordingManager**: Controls the recording lifecycle.
- **ScreenshotManager**: Handles screenshot capture during detection events.
- **Main UI Thread**: Manages the graphical interface.

### Data Flow
```text
USB Camera (1920×1080, 30 FPS)
    ↓
CameraThread (frame capture)
    ↓
DetectionThread (YOLOv8 inference)
    ↓ (detection_result signal)
    ├→ RecordingManager (start/stop recording)
    ├→ ScreenshotManager (captures snapshots)
    └→ Main UI (updates status)
    ↓
Video Output: recordings/*.mp4
Image Output: snapshots/*.jpg
```

---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- USB camera or built-in webcam

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/detection-triggered-recorder.git
cd detection-triggered-recorder
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python security_monitor.py
```

---

## Usage

### Starting the Application
1. Connect the USB camera.
2. Run `python security_monitor.py`.
3. The application will automatically detect available cameras.
4. Select the desired camera from the dropdown.
5. The system will enter monitoring mode.

### During Operation
- **Live Video Feed**: Shows real-time camera feed with detection bounding boxes.
- **Status Indicators**: Displays the current detection, recording, and system statuses.

### Output Files
After running the system:
```
project-root/
├── recordings/
│   ├── security_20251103_143500.mp4
│   ├── security_20251103_143530.mp4
└── snapshots/
    ├── snapshot_20251103_143502_045.jpg
    ├── snapshot_20251103_143505_123.jpg
```

---

## Configuration

### Adjustable Parameters

Edit `security_monitor.py` to customize the following:

#### Detection Sensitivity
```python
self.confidence_threshold = 0.5  # 0.0-1.0, higher = stricter detection
```

#### Recording Cooldown
```python
self.cooldown_seconds = 5  # Seconds after last detection before stopping recording
```

#### Screenshot Frequency
```python
self.screenshot_cooldown = 2  # Seconds between snapshots
```

---

## Performance Characteristics

- **CPU Usage**: ~15-25% in standby, ~30-40% during detection/recording.
- **Memory Usage**: ~200-300 MB base, ~400-500 MB with models loaded.
- **GPU Acceleration**: Optional, requires CUDA support.
- **Detection Latency**: ~30-50ms per frame.
- **Storage Efficiency**:
  - **Event-Driven Recording (24 hrs)**: ~5-15 GB.
  - **Snapshots (24 hrs)**: ~1-3 GB.

---

## Directory Structure

```
detection-triggered-recorder/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── security_monitor.py          # Main application script
├── recordings/                  # Video files (auto-generated)
├── snapshots/                   # Image files (auto-generated)
└── docs/
    ├── INSTALLATION.md
    ├── USAGE.md
    └── TROUBLESHOOTING.md
```

---

## Dependencies

```
PyQt5==5.15.9              # GUI framework
opencv-python==4.8.1.78    # Video capture
ultralytics==8.0.196       # YOLOv8 model
numpy==1.24.3              # Numerical computing
Pillow==10.0.1             # Image processing
torch==2.0.1               # Deep learning backend
```

---

## System Requirements

- **Minimum**: Python 3.8+, 4 GB RAM, 2 GB free disk space, USB camera (USB 2.0), Intel i5 processor.
- **Recommended**: Python 3.10+, 8 GB RAM, 20 GB free disk space, USB 3.0 camera, Intel i7 or better, NVIDIA GPU (optional).

---

## License

MIT License — see [LICENSE](./LICENSE) for details.

---

## Acknowledgements

- **YOLOv8** (Ultralytics) for advanced object detection.
- **PyQt5** for GUI framework.
- **OpenCV** for video capture and processing.

---
