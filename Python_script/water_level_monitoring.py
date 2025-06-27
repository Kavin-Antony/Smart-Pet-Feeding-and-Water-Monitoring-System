import RPi.GPIO as GPIO
import time

# GPIO Pins
TRIG = 23
ECHO = 24
RED_LED = 16
GREEN_LED = 26

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout_start = time.time()
    while GPIO.input(ECHO) == 0:
        if time.time() - timeout_start > 0.05:
            return None
    pulse_start = time.time()

    timeout_start = time.time()
    while GPIO.input(ECHO) == 1:
        if time.time() - timeout_start > 0.05:
            return None
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2
    return round(distance, 2)

try:
    print("Ultrasonic Water Level Monitor with RGB LED\n")

    while True:
        dist = measure_distance()
        if dist is not None:
            print(f"Distance: {dist} cm")

            if dist > 12.5:
                # Water level low ? RED ON, GREEN OFF
                GPIO.output(RED_LED, GPIO.HIGH)
                GPIO.output(GREEN_LED, GPIO.LOW)
            else:
                # Water level OK ? GREEN ON, RED OFF
                GPIO.output(RED_LED, GPIO.LOW)
                GPIO.output(GREEN_LED, GPIO.HIGH)

        else:
            print("No Echo Detected - Retrying...")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()
