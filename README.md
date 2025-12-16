# 🖐️ Hand Tracking Mouse Controller (Python)

Control your **mouse pointer using your hand** through a webcam using **Computer Vision**.
This project turns hand gestures into **real OS-level mouse actions**, allowing you to play games and use applications **without touching a physical mouse**.

Built using **Python, OpenCV, MediaPipe, and PyAutoGUI**.

---

## ✨ Features

* 🖱️ **Mouse movement** using index finger
* 🤏 **Left click** using thumb + index pinch
* ✌️ **Right click** using index + middle finger pinch
* 🎯 **Calibrated timings** to prevent accidental clicks
* 🚫 Scroll intentionally removed for stability
* 🎮 Works with **any mouse-based application or game**
* 🪟 Runs on Windows using a normal webcam

---

## 🧠 How It Works (High Level)

1. Webcam captures video frames
2. MediaPipe detects **hand landmarks**
3. Distances between fingers are calculated
4. Gestures are mapped to mouse actions
5. PyAutoGUI sends events to the operating system

👉 The system acts as a **real mouse**, not a simulation.

---

## 🗂️ Project Structure

```
hand-tracking-mouse/
│
├── main.py              # Main controller loop
├── hand_tracker.py      # Hand landmark detection
├── mouse_controller.py # OS-level mouse control
├── gestures.py          # Gesture logic (clicks)
├── config.py            # Calibration & timing values
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements

* Python **3.10+**
* Webcam
* Windows OS

### Python Libraries

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/hand-tracking-mouse.git
cd hand-tracking-mouse
```

2. Run the controller:

```bash
python main.py
```

3. Allow camera access

4. Move your hand to control the mouse

Press **ESC** to exit.

---

## 🖐️ Gesture Controls

| Gesture               | Action                |
| --------------------- | --------------------- |
| Index finger movement | Mouse movement        |
| Thumb + Index pinch   | Left click            |
| Index + Middle pinch  | Right click           |
| No gesture            | Pointer movement only |

> Scroll is intentionally disabled for accuracy and usability.

---

## 🎮 Use Cases

* Play mouse-based games (Tic Tac Toe, Snake, etc.)
* Accessibility tool
* Human–Computer Interaction demos
* Computer Vision projects
* Interactive presentations

---

## 🧪 Calibration Notes

All gesture thresholds and timing delays are tuned for:

* Reduced jitter
* Intentional clicks
* Smooth pointer control

You can adjust values in:

```
config.py
gestures.py
```

---

## 🚀 Future Improvements

* Gesture-based pause / resume
* On-screen gesture indicator
* GUI for calibration
* Windows executable (.exe)
* Multi-hand support
* ML-based gesture classification

---

## 🧑‍💻 Author

**Daksh Mahera**

Built as a hands-on project to explore:

* Computer Vision
* Real-time systems
* Human–Computer Interaction
* Practical Python applications

---

## ⭐ Final Note

This project is designed as a **system**, not a demo.
Once running, it works with **any application that supports mouse input**.

If you find this useful, feel free to ⭐ the repository.
