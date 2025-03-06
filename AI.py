import speech_recognition as sr
import serial
import time

# Initialize serial connection to Arduino
# Change 'COM3' to your Arduino's port (e.g., '/dev/ttyUSB0' for Linux)
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Wait for serial connection to establish
    print("Connected to Arduino on COM3")
except:
    print("Failed to connect to Arduino. Check port and connection.")
    exit()

# Initialize speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_and_recognize():
    with mic as source:
        print("\nAdjusting for ambient noise... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening for command... (say 'light on', 'light off', etc.)")
        
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Timeout: No command heard")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def send_command_to_arduino(command):
    # Define your command mappings
    command_map = {
        "light on": "a1",
        "light off": "a0",
        "fan on": "b1",
        "fan off": "b0",
        "door open": "c1",
        "door close": "c0"
    }
    
    if command in command_map:
        serial_command = command_map[command]
        arduino.write(serial_command.encode())
        print(serial_command)
        print(f"Sent {serial_command} to Arduino")
    else:
        print("Command not recognized. Available commands:")
        for cmd in command_map.keys():
            print(f"- {cmd}")

def main():
    print("Home Automation Voice Control System")
    print("Say a command like 'light on' or 'fan off'")
    print("Press Ctrl+C to exit")
    
    while True:
        command = listen_and_recognize()
        if command:
            send_command_to_arduino(command)
        time.sleep(0.5)  # Small delay between commands

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        arduino.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        arduino.close()