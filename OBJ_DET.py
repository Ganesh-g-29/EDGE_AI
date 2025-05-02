import serial
import time
import pyttsx3

# Setup TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Connect to Arduino
ArduinoSerial = serial.Serial('/dev/cu.usbserial-10', 9600)
time.sleep(2)

def speak(audio):
    print(f"Speaking: {audio}")
    engine.say(audio)
    engine.runAndWait()

def read_distance():
    while ArduinoSerial.in_waiting:
        ArduinoSerial.readline()  # flush old data
    time.sleep(0.6)
    try:
        line = ArduinoSerial.readline().decode().strip()
        distance = float(line)
        print(f"Distance: {distance} cm")
        return distance
    except:
        return -1

# Distance state tracking
last_spoken = None

if __name__ == "__main__":
    while True:
        distance = read_distance()

        # Check for change only if valid
        if distance != -1:
            if distance < 20 and last_spoken != "close":
                speak("Stop! Close object in front.")
                last_spoken = "close"
            elif 20 <= distance < 40 and last_spoken != "near":
                speak("Object is near.")
                last_spoken = "near"
            elif 40 <= distance < 100 and last_spoken != "mid":
                speak("Object is one meter away.")
                last_spoken = "mid"
            elif distance >= 100 and last_spoken != "far":
                speak("Object is far away.")
                last_spoken = "far"
        
        time.sleep(1)  # avoid spamming speech
