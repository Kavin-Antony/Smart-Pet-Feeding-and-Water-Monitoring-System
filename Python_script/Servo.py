import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin):
        self.servo_pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = angle / 18 + 2.5
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(0)

    def rotate_to(self, angle):
        try:
            self.set_angle(angle)
        except Exception as e:
            print("Error rotating servo:", e)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
