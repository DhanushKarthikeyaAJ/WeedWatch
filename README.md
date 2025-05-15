
# 🌿 WeedWatch

**WeedWatch** is a hybrid AI + Arduino-based weed detection system designed for precision agriculture. It uses a machine learning model running on a PC to classify plant images as **weed** or **non-weed**, and then communicates the result to an Arduino Nano 33 BLE Sense for real-time physical feedback like LED alerts.

---

## 🚜 Project Overview

- 🧠 **Machine Learning (PC)**  
  Trained MobileNetV2 model classifies images into weed/non-weed using TensorFlow/Keras.

- 🔌 **Arduino (Microcontroller)**  
  Receives classification result via Serial and performs real-time actions — like turning on an LED for weeds.

- 🛠️ **Serial Communication (Bridge)**  
  Python sends the result to Arduino using keyboard emulation (`pyautogui`) to avoid COM port conflicts.

---

## 🧰 Technologies Used

| Component               | Purpose                                      |
|------------------------|----------------------------------------------|
| Python + Keras         | Train and run weed classifier                |
| TensorFlow Lite (opt.) | Convert model to lightweight format (if needed) |
| PyAutoGUI              | Emulate keyboard to send data to Arduino     |
| Arduino Nano 33 BLE Sense | Receive and act on predictions            |
| Arduino IDE            | Upload sketches and view Serial Monitor      |

---

## 🗂️ Folder Structure

```
WeedWatch/
├── Arduino/
│   └── weed_detector.ino          # Receives prediction & controls LED
├── Python/
│   └── classify_and_send.py       # Classifies and sends to Arduino
├── model/
│   ├── weed_classifier.h5         # Trained model file
│   └── image_data/                # Test images
├── docs/
│   └── circuit_diagram.png        # Optional: wiring reference
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/DhanushKarthikeyaAJ/WeedWatch.git
cd WeedWatch
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train or Load Model
- Train using your own image dataset (e.g., crops vs weeds)
- Or use the included `weed_classifier.h5` model

### 4. Upload Arduino Code
- Open `Arduino/weed_detector.ino` in Arduino IDE
- Select **Arduino Nano 33 BLE Sense** from Tools > Board
- Upload the sketch
- Open **Serial Monitor** at `9600` baud

### 5. Classify and Send from PC
```bash
cd Python
python classify_and_send.py
```

This script uses `pyautogui` to send `"WEED"` or `"NON_WEED"` to the Serial Monitor (emulating keyboard input).

---

## 💡 Features

- ✅ Lightweight MobileNetV2-based classifier
- ✅ LED control for classification feedback
- ✅ Works even when Serial Monitor is open (keyboard input workaround)
- ✅ Simple hardware setup
- 🧪 Easily extendable to real-time webcam input or Bluetooth comms

---


## 🧠 Credits

Built by [Dhanush Karthikeya A J](https://github.com/DhanushKarthikeyaAJ)  
Contributions welcome!

---

## 📜 License

MIT License
