# Detection-Triggered Recorder (Void-DTR)

An intelligent, event-driven surveillance system that automatically captures video and screenshots when humans are detected in real-time using **AI vision processing**.

## Working Example



## Overview

**Detection-Triggered Recorder** is a sophisticated security monitoring application designed for **research** and **autonomous surveillance**. It continuously monitors a USB-connected camera feed, performs real-time human detection using **YOLOv8**, and automatically initiates recording only when humans are detected. This event-driven approach drastically reduces storage requirements compared to traditional 24/7 recording, while still ensuring comprehensive event documentation.

## Key Features

### 🎯 Core Functionality
- **Real-Time Human Detection**: YOLOv8 neural network processes video frames at 30 FPS for instantaneous human detection.
- **Automatic Recording**: Initiates recording only when a person is detected, saving storage space.
- **Smart Cooldown Logic**: A 5-second cooldown after the last detection prevents fragmented video clips.
- **Automatic Snapshots**: Captures timestamped screenshots every 2 seconds during detection events.
- **Continuous Monitoring**: Operates in standby mode, consuming minimal CPU resources while remaining responsive to human presence.

### 🎬 Recording Features
- **High-Quality Video**: Captures video at 1920×1080 resolution and 30 FPS in MP4 format with H.264 encoding.
- **Automatic Timestamping**: All recordings are automatically timestamped in filenames (`YYYYMMDD_HHMMSS` format).
- **Smart Storage**: Videos are stored in the `recordings/` directory.
- **Efficient Compression**: H.264 compression balances video quality and file size.

### 📸 Screenshot Features
- **Event Detection Snapshots**: Automatic image capture when a person is detected.
- **Timestamp Overlay**: Each image contains a timestamp for reference.
- **Organized Storage**: Screenshots are saved in the `snapshots/` directory, with millisecond precision naming.
- **Smart Snapshot Frequency**: Takes snapshots every 2 seconds during continuous detection to avoid duplicates.
- **Data Recovery**: If the camera disconnects mid-recording, screenshots can serve as backup evidence.

### 🖥️ User Interface
- **Clean PyQt5 GUI**: A professional and intuitive desktop application interface.
- **Live Video Display**: Real-time camera feed with detection bounding boxes.
- **Status Indicators**:
  - **Detection Status**: Shows detection state (Not Detected / DETECTED).
  - **Recording Status**: Indicates whether the system is recording (Standby / RECORDING / COOLDOWN).
  - **System Health**: Indicates overall system status (Monitoring / Stopped / Error).
- **Color-Coded States**: Green (normal), Red (active), Orange (transition).
- **Camera Selection**: Dropdown to select from available USB or built-in cameras.
- **Resizable Window**: User-friendly interface that adapts to different screen sizes.

### 🎥 Camera Support
- **USB Camera Compatible**: Works with OBSBOT Tiny 2, standard USB webcams, and most V4L2-compliant cameras.
- **Automatic Detection**: Scans system for connected cameras and identifies available devices.
- **1920×1080 Capture**: Supports high-resolution capture at 30 FPS.
- **Multi-Camera Ready**: System can be adapted for multiple simultaneous camera feeds in future updates.

## System Architecture

### Threading Model
- **CameraThread**: Continuously captures frames from the USB camera at 30 FPS.
- **DetectionThread**: Runs YOLOv8 inference on captured frames to detect human presence.
- **RecordingManager**: Manages recording state transitions (Standby → Detected → Cooldown).
- **ScreenshotManager**: Captures event-triggered screenshots with timestamp annotation.
- **Main UI Thread**: Handles PyQt5 GUI rendering and user interactions.

### Data Flow
```
USB Camera (1920×1080, 30 FPS)
    ↓
CameraThread (frame capture)
    ↓
DetectionThread (YOLOv8 inference)
    ↓ (detection_result signal)
    ├→ RecordingManager (starts/stops recording)
    ├→ ScreenshotManager (captures snapshots)
    └→ Main UI (updates status indicators)
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
1. **Connect USB camera** to your computer.
2. Run the application:
   ```bash
   python security_monitor.py
   ```
3. The system will automatically detect available cameras.
4. **Select** your desired camera from the dropdown (USB camera is selected by default).
5. The system will begin monitoring and will start recording when a person is detected.

### During Operation
- **Live Video Feed**: Displays the real-time camera feed with bounding boxes indicating detected persons.
- **Status Updates**:
  - **Detection Status**: 🟢 Not Detected / 🔴 DETECTED.
  - **Recording Status**: 🟢 Standby / 🔴 RECORDING / 🟡 COOLDOWN.
  - **System Health**: 🟢 Monitoring / 🟡 Stopped / 🔴 Error.
- **No Manual Controls**: The system is fully automatic—no buttons required to start or stop recording.
- **Graceful Exit**: Press `EXIT` to properly stop all threads and close the application.

### Output Files
After running the system, output files will be saved as follows:
```
project-root/
├── recordings/
│   ├── security_20251103_143500.mp4
│   ├── security_20251103_143530.mp4
└── snapshots/
    ├── snapshot_20251103_143502_045.jpg  [with timestamp overlay]
    ├── snapshot_20251103_143505_123.jpg  [with timestamp overlay]
```

---

## Configuration

### Adjustable Parameters

Edit `security_monitor.py` to customize the following parameters:

#### Detection Sensitivity (Line ~73)
```python
self.confidence_threshold = 0.5  # Range: 0.0-1.0, higher values = stricter detection
```

#### Recording Cooldown (Line ~145)
```python
self.cooldown_seconds = 5  # Seconds after last detection before stopping recording
```

#### Screenshot Frequency (Line ~171)
```python
self.screenshot_cooldown = 2  # Seconds between snapshots during detection
```

---

## Performance Characteristics

### Resource Usage
- **CPU**: ~15-25% during monitoring (idle), ~30-40% during detection/recording
- **Memory**: ~200-300 MB base, ~400-500 MB with models loaded
- **GPU**: Optional GPU acceleration available (requires CUDA support in `ultralytics`)
- **Disk I/O**: Active only during recording events.

### Detection Accuracy
- **YOLOv8 nano model**: ~80% mAP on COCO dataset.
- **Detection Latency**: ~30-50ms per frame.

### Storage Efficiency
- **Continuous Recording** (24 hours): ~150-200 GB.
- **Event-Driven Recording** (24 hours, typical office): ~5-15 GB.
- **Snapshots** (24 hours, typical office): ~1-3 GB.

---

## Directory Structure

```
detection-triggered-recorder/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── security_monitor.py          # Main application script
├── recordings/                  # Video output directory (auto-created)
├── snapshots/                   # Screenshot output directory (auto-created)
└── docs/
    ├── INSTALLATION.md          # Detailed installation guide
    ├── USAGE.md                 # Advanced usage scenarios
    ├── TROUBLESHOOTING.md       # Common issues and solutions
    └── API.md                   # Code documentation
```

---

## Requirements

### `requirements.txt`
This file contains the list of Python dependencies needed to run the application. To install them, use:

```bash
pip install -r requirements.txt
```

#### Contents of `requirements.txt`
```txt
PyQt5==5.15.9              # GUI framework
opencv-python==4.8.1.78    # Video capture and processing
ultralytics==8.0.196       # YOLOv8 detection model
numpy==1.24.3              # Numerical computing
Pillow==10.0.1             # Image processing
torch==2.0.1               # Deep learning backend
```

---

## Common Issues & Troubleshooting

### Camera Not Detected
- Ensure that the camera is properly connected and recognized by your system.
- Check USB permissions (Linux: `chmod 666 /dev/video*`).
- Update camera drivers or try a different USB port.

### Detection Issues
- **Low Detection Accuracy**: Increase the `confidence_threshold` for stricter
