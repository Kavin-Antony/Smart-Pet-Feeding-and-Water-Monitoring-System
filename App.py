from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import os
import time
import bcrypt
from flask_cors import CORS
# from Python_script.Servo import Servo  

app = Flask(__name__)
CORS(app)  # Allow CORS from any origin

LOG_FILE = "feeding_log.json"
USER_FILE = "login_details.json"

# Read the feeding log
def read_log():
    with open(LOG_FILE, "r") as f:
        return json.load(f)

# Write the feeding log
def write_log(log_data):
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

# Feed pet endpoint
# @app.route("/feed", methods=["POST"])
# def feed_pet():
#     data = request.get_json()
#     amount = data.get("amount")
    
#     if amount is None:
#         return jsonify({"error": "Amount is required"}), 400

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Operate the servo
#     servo = Servo(17)
#     servo.rotate_to(170)
#     time.sleep(2)
#     servo.rotate_to(0)
#     servo.cleanup()

#     # Log the feeding
#     new_entry = {
#         "amount": amount,
#         "timestamp": timestamp
#     }

#     log = read_log()
#     log.append(new_entry)
#     write_log(log)

#     return jsonify({
#         "message": f"Successfully fed {amount} grams of food.",
#         "fed_amount": amount,
#         "time": timestamp,
#         "time_feed_completed": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not email or not username or not password:
        return jsonify({"error": "Email, username, and password are required"}), 400

    # Read existing users
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

    if email in users:
        return jsonify({"error": "Email already registered"}), 409

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users[email] = {
        "username": username,
        "password": hashed_password.decode('utf-8')
    }

    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

    return jsonify({"success": True, "message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("username")   # frontend sends email in "username" field
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    else:
        return jsonify({"error": "No users found"}), 404

    if email not in users:
        return jsonify({"success": False, "error": "Invalid email or password"}), 401

    stored_hash = users[email]["password"].encode('utf-8')

    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return jsonify({
            "success": True,
            "message": "Login successful",
            "username": users[email]["username"]
        }), 200
    else:
        return jsonify({"success": False, "error": "Invalid email or password"}), 401

# Get feeding history
@app.route("/feeding-history", methods=["GET"])
def get_history():
    return jsonify(read_log())

@app.route("/login_page")
def login_page():
    return render_template("Login.html")

@app.route("/signup_page")
def signup_page():
    return render_template("Signup.html")

@app.route("/home_page")
def  home_page():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)