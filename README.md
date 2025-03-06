## Circuit design
![download](https://github.com/user-attachments/assets/429b4ed9-035e-45be-b563-0897ab82f13a)

Sure! Here's the updated README with your name included and a section about using Arduino code for the hardware part of the system:

---

# AI-Based Simple Home Automation System

## Overview
Welcome to the **AI-Based Simple Home Automation System**! This system leverages the power of AI to control various devices in your home with ease. Whether it's controlling lights, security systems, or other appliances, this system brings smart home features to your fingertips, all powered by advanced machine learning algorithms.

### Developed By: 
**Muhammad Hassnain**

## Features
- **Voice Control**: Manage your home devices using voice commands.
- **Automation**: Devices can be scheduled to turn on or off based on certain conditions (e.g., time of day, sensors, etc.).
- **AI Integration**: The system adapts over time based on your preferences and routines.
- **Security**: Automated monitoring and alerts for your home security.

## Requirements
Before you start, make sure you have the following tools and libraries installed:

- Python 3.x
- Pip (for Python package management)
- Arduino IDE (for uploading the Arduino code)

## Installation

To get started with the **AI-Based Simple Home Automation System**, follow these steps:

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/MH-Pro/AHAB.git
cd AHAB
```

### 2. Install Dependencies
Once you've cloned the repository, you'll need to install the required dependencies. To do this, run the following command:

```bash
pip3 install -r requirements.txt
```

This will install all the necessary libraries listed in the `requirements.txt` file, ensuring that your environment is ready to run the system.

### 3. Upload Arduino Code
To make sure the hardware (like lights, sensors, etc.) is controlled by the system, you'll need to upload the provided Arduino code to your Arduino board.

- Open the `arduino_code.ino` file in the **Arduino IDE**.
- Select your Arduino model and the appropriate port.
- Click the "Upload" button in the Arduino IDE to upload the code to your Arduino.

This will set up the connection between your Arduino and the Python-based home automation system.

### 4. Run the System
After installing the dependencies and uploading the Arduino code, you can start the system by running the Python file:

```bash
python3 AI.py
```

This will start the home automation system, and you can begin controlling your devices via the AI interface.

## Usage

Once the system is running, you can interact with it in various ways:

### Voice Commands
The system is designed to accept voice commands such as:
- "Turn on the lights."
- "Turn on the fan."
- "Turn on the TV."

### Manual Control
If you'd like, you can also manually control devices through the user interface or configuration files.

## Configuration

You can easily customize the system by editing the `config.json` file to set up devices, schedules, and preferences. Refer to the sample configuration below:

```Dictionary
command_map = {
        "light on": "a1",
        "light off": "a0",
        "fan on": "b1",
        "fan off": "b0",
        "tv on": "c1",
        "tv off": "c0"
    }
```

## Contributing

We welcome contributions! Feel free to fork the repository, create a branch, and submit a pull request. If you encounter any issues or have ideas for improvements, open an issue in the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Enjoy your Smart Home Experience! 🏠✨

---

This updated README now includes your name and specifies the need to upload Arduino code to the hardware. Let me know if you need further adjustments!
