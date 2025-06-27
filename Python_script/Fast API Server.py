from fastapi import FastAPI, Body
from datetime import datetime
import json
import os
from Python_script.Servo import Servo  
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_FILE = "feeding_log.json"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        json.dump([], f)

def read_log():
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def write_log(log_data):
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

@app.post("/feed")
async def feed_pet(amount: int = Body(...)):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    servo = Servo(17)

    # Rotate to 90 degrees
    servo.rotate_to(170)
    time.sleep(2)

    # Rotate back to 0 degrees
    servo.rotate_to(0)

    # Cleanup GPIO when done
    servo.cleanup()
    new_entry = {
        "amount": amount,
        "timestamp": timestamp
    }
    
    log = read_log()
    log.append(new_entry)
    write_log(log)

    return {
        "message": f"Successfully fed {amount} grams of food.",
        "fed_amount": amount,
        "time": timestamp,
        "time_feed_completed": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/feeding-history")
def get_history():
    return read_log()


#ngrok http --domain=just-earwig-blatantly.ngrok-free.app 8000

#uvicorn server:app --host 0.0.0.0 --port 8000