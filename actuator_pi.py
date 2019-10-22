import RPi.GPIO as GPIO
from time import sleep   # Imports sleep (aka wait or pause) into the program

GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout
GPIO.setup(8, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.setup(40,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)

throttle = GPIO.PWM(8, 50)  # Sets up pin 11 as a PWM pin
steer = GPIO.PWM(40, 50)
cur_speed = 0
angle = 0

def init(default_speed=12):
    throttle.start(15)
    steer.start(9)
def set_speed(speed):
    cur_speed = speed
    throttle.ChangeDutyCycle(speed)

def get_speed():
    return cur_speed


def get_angle():
    return angle

def stop():
    throttle.ChangeDutyCycle(15)


# steering
def center():
    steer.ChangeDutyCycle(5)


def set_angle(a):
    angle = a
    steer.ChangeDutyCycle(a)


# exit
def turn_off():
    throttle.stop()
    steer.stop()
    GPIO.cleanup()