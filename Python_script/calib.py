import RPi.GPIO as GPIO
from hx711 import HX711
import time

GPIO.setwarnings(False)

# Initialize HX711 (adjust pins if needed)
hx = HX711(dout_pin=5, pd_sck_pin=6)

print("HX711 Calibration Program")
print("===========================")

try:
    print("Taring... Please ensure the scale is empty.")
    offset = 0
    for _ in range(20):
        readings = hx.get_raw_data(times=5)
        avg = sum(readings) / len(readings)
        offset += avg
    offset = offset / 20
    print(f"Tare Offset: {offset}\n")

    known_weight = float(input("Enter known weight placed on scale (in grams): "))
    print("Please place the known weight now and wait...")
    time.sleep(5)

    readings = hx.get_raw_data(times=10)
    avg = sum(readings) / len(readings)
    print(f"Measured Raw Value with Weight: {avg}")

    calibration_factor = (avg - offset) / known_weight
    print(f"\n? Calibration Factor (use this value in your main code): {calibration_factor}")

except KeyboardInterrupt:
    print("\nCalibration interrupted.")

finally:
    GPIO.cleanup()
    print("GPIO Cleaned up. Exiting...")
