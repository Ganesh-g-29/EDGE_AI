# EDGE_AI 🎯  
**On-Device Object Recognition and Proximity Feedback for Blind Navigation Aids**

---

## 🔍 Project Motivation

Navigating independently is a challenge for visually impaired individuals, especially in environments filled with static or dynamic obstacles. This project aims to build an assistive system that can detect nearby objects and provide real-time audio feedback about their proximity, enhancing mobility and awareness for the user. While our end goal is to embed this into wearable smart glasses, the current prototype focuses on proof-of-concept using Arduino and Python.

---

## 🛠 Tools and Components Used

### Hardware:
- Arduino Uno R3  
- HC-SR04 Ultrasonic Distance Sensor  
- USB Cable  
- Laptop (for Python voice feedback script)  
- Power Bank / USB Supply  

### Software:
- Arduino IDE  
- Python 3.10+  
- Libraries:
  - `pyttsx3` (Text-to-Speech)  
  - `pyserial` (Serial communication)

---

## 📂 Repository Structure

| File        | Description |
|-------------|-------------|
| `sketch.ino` | Arduino sketch to measure distance using HC-SR04 and send it via Serial |
| `OBJ_DET.py` | Python script to read distance from Uno and speak dynamic proximity alerts |
| `README.md` | Documentation and usage instructions for the project |

---

## 🚀 How to Run

### Step 1: Flash Arduino Code

1. Open `sketch.ino` in Arduino IDE  
2. Select the board: **Arduino Uno**  
3. Upload the code to the Uno  
4. Ensure the sensor is connected:  
   - `Trig → D2`  
   - `Echo → D3`  
   - `VCC → 5V`  
   - `GND → GND`

### Step 2: Run Python Voice Feedback

1. Make sure your Uno is connected via USB  
2. Install Python libraries (once):
   ```bash
   pip install pyttsx3 pyserial
  
