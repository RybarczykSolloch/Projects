from gpiozero import LED, AngularServo
from time import sleep

led = LED(23)
servo = AngularServo(24, min_angle=-90, max_angle=90)

while True:

    #lewe polożenie - wolne miganie
    servo.angle =- 90

    for i in range (3):
        led.on()
        sleep(1)
        led.off()
        sleep(1)

    #prawe położenie - szybkie miganie
    servo.angle = 90

    for i in range (3):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)