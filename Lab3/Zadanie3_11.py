from gpiozero import AngularServo
from time import sleep

servo = AngularServo(24, min_angle=-90, max_angle=90)
predkosc = 0.05

while True:
    #ruch od -90 d0 90 stopni "range(-90,91) - zwiekszenie kata o 1 st"
    for kat in range(-90,91):
        servo.angle = kat
        sleep(predkosc)

    #ruch powrotny "range(90, -91, -1) - zmniejszenie kata o 1 st"

    for kat in range(90, -91, -1):
        servo.angle = kat
        sleep(predkosc)