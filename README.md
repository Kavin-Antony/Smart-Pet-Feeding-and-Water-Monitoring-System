# 🐾 Smart Pet Feeding & Water Monitoring System

An IoT-based automated pet feeding and water level monitoring system built using **Raspberry Pi**, enabling remote control through a web interface powered by Flask.

---

## 🚀 Features

✅ **Automated Pet Feeding**  
- Dispenses precise food amounts using a load cell (HX711) and servo motor.  
- Logs feeding events in `feeding_log.json`.

✅ **Water Level Monitoring**  
- Measures water levels via an ultrasonic sensor.  
- Displays alerts if water is low.

✅ **Web Interface**  
- User-friendly web pages for login, signup, and dashboard control.  
- Remote access secured via Ngrok tunnel.

✅ **User Authentication**  
- Handles login and signup via `login_details.json`.

---

## 🗂️ Project Structure
```
macos/
Python_script/
├── calib.py
├── Fast API Server.py
├── Servo.py
├── water_level_monitoring.py
Templates/
├── Home.html
├── Login.html
├── Signup.html
.gitignore
App.py
feeding_log.json
login_details.json
requirement.txt
```

---

## 🌐 Live Demo 

####  [🔹 Login Page](https://kavin-antony.github.io/Smart-Pet-Feeding-and-Water-Monitoring-System/Templates/Login.html)
####  [🔹 Signup Page](https://kavin-antony.github.io/Smart-Pet-Feeding-and-Water-Monitoring-System/Templates/Signup.html)
####  [🔹 Home Page](https://kavin-antony.github.io/Smart-Pet-Feeding-and-Water-Monitoring-System/Templates/Home.html)

### Key Files

| File / Folder                 | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `App.py`                      | Entry point for Flask web server.                           |
| `Python_script/calib.py`      | Calibration code for load cell (HX711).                       |
| `Python_script/Servo.py`      | Controls servo motor for food dispensing.                     |
| `Python_script/water_level_monitoring.py` | Reads ultrasonic sensor data for water levels. |
| `Python_script/Fast API Server.py` | Server-side logic for handling API calls.         |
| `Templates/`                  | HTML templates for web pages.                                 |
| `feeding_log.json`            | Stores logs of feeding times and quantities.                  |
| `login_details.json`          | Stores user credentials securely.                            |
| `requirement.txt`             | Python dependencies for the project.                         |

---

## 🛠️ Technologies Used

- **Programming Languages**: Python
- **Frameworks**: Flask 
- **Hardware**:
  - Raspberry Pi
  - Load Cell with HX711 Amplifier
  - Servo Motor
  - Ultrasonic Sensor (HC-SR04)
  - RGB LED
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: Ngrok, GPIO

---

## ✅ Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pet-feeding-system.git
    cd pet-feeding-system
    ```

2. Install dependencies:
    ```bash
    pip install -r requirement.txt
    ```

3. Run the Flask server:
    ```bash
    python App.py
    ```

4. Expose via WSGI Server:
    ```bash
    gunicorn -b 0.0.0.0:8000 App:app
    ```

5. Open the web interface and control your pet feeder remotely!

> **⚠️ Note:**  
> If you deploy this system on a different machine or server,  
> remember to update the system’s IP address or domain name  
> in all your `fetch()` and `request()` calls in the frontend code.  
> This ensures your web interface correctly communicates with the Flask server.
