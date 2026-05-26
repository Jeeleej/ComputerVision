# 🚗 Vehicle Detection & Counting System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white"/>
</p>

<p align="center">
  A real-time vehicle detection, tracking, and counting system built with <strong>YOLOv8n</strong> and <strong>SORT</strong> algorithm. Uses a mask image to focus detection on a specific region of interest and counts vehicles as they cross a virtual counting line.
</p>

---

## 📸 Sample Output

| Detection Frame |
|:---:|
| <img width="1919" height="1137" alt="Image" src="https://github.com/user-attachments/assets/94eed888-cff1-4347-8b74-4a1be6886eea" /> |

- 🟣 **Magenta bounding box** — detected vehicle with unique ID
- 🔴 **Red counting line** — flashes 🟡 **yellow** when a vehicle crosses
- 🟡 **Count: XX** — total vehicles that have passed the line

---

## 🎬 Demo

[▶ Watch Demo](https://raw.githubusercontent.com/Jeeleej/ComputerVision/main/Result_CV.mp4)

---

## ✨ Features

- ✅ **YOLOv8n** — fast, lightweight object detection model
- ✅ **SORT Tracker** — unique ID assigned to each vehicle across frames
- ✅ **Mask-based ROI** — uses `mask.png` to restrict detection to the road area only
- ✅ **Virtual counting line** — green line turns yellow on vehicle crossing
- ✅ **Live vehicle count** — total count displayed on screen in real time
- ✅ Works on any road/traffic video

---

## 📁 Project Structure

```
├── main.py              # Main script — detection, tracking & counting
├── sort.py              # SORT tracking algorithm
├── mask.png             # Region of interest mask image
├── car_video.mp4        # Input traffic video
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ How It Works

```
Input Video
    │
    ▼
Apply Mask (mask.png)        ← Focuses detection on road region only
    │
    ▼
YOLOv8n Detection            ← Detects vehicles in each frame
    │
    ▼
SORT Tracker                 ← Assigns unique ID to each vehicle
    │
    ▼
Counting Line Check          ← Line is GREEN; turns YELLOW on crossing
    │
    ▼
Count Incremented & Displayed on Screen
```

1. Each frame is masked using `mask.png` to ignore irrelevant areas.
2. YOLOv8n runs detection on the masked frame.
3. SORT tracker maintains consistent IDs across frames.
4. A horizontal counting line is drawn across the frame.
5. When a vehicle's center point crosses the line → count increments and line flashes yellow.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Jeeleej/ComputerVision.git
cd YOUR_REPO

# 2. Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

> Make sure `car_video.mp4` and `mask.png` are in the same directory as `main.py`.

---

## 📦 Requirements

```
ultralytics
opencv-python
numpy
cvzone
```

> Install all at once:
> ```bash
> pip install -r requirements.txt
> ```

---

## 🎭 Mask Image

The `mask.png` is a black-and-white image the same size as the video frame:

- **White region** → area where detection is active (e.g., the road)
- **Black region** → area ignored by the detector

This ensures vehicles on pavements, side areas, or sky are not counted.

---

## 🔢 Counting Line Logic

| State | Color | Meaning |
|-------|-------|---------|
| Default | 🟢 Green | No vehicle crossing |
| Triggered | 🟡 Yellow | Vehicle just crossed the line |

The line position can be adjusted in `main.py` by modifying the `count_line` variable.

---

## 🛠️ Configuration

Inside `main.py`, you can tweak:

| Variable | Description |
|----------|-------------|
| `count_line` | Y-coordinate of the counting line |
| `conf` | YOLO detection confidence threshold |
| `label` | Vehicle label to detect (car, truck, bus, etc.) |
| `mask` | Path to your custom mask image |

---

## 📊 Model Info

| Property | Value |
|----------|-------|
| Model | YOLOv8n (nano) |
| Framework | Ultralytics |
| Tracker | SORT |
| Input | Video file / Webcam |
| Classes Used | Car, Truck, Bus, Motorbike |

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [SORT — Simple Online and Realtime Tracking](https://github.com/abewley/sort)
- [OpenCV](https://opencv.org/)

---

<p align="center">Made with ❤️ | Computer Vision Project</p>
