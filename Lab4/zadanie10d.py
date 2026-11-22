
from mpu6050 import mpu6050
import board
import adafruit_vl53l0x
import time
import math

# Inicjalizacja czujnika MPU6050
mpu = mpu6050(0x68)

# Inicjalizacja czujnika VL53L0X
i2c = board.I2C()
distance_sensor = adafruit_vl53l0x.VL53L0X(i2c)

# Próg wykrywania ruchu
movement_limit = 2.0

while True:
    # Odczyt danych z akcelerometru
    accel = mpu.get_accel_data()

    ax = accel['x']
    ay = accel['y']
    az = accel['z']

    # Obliczenie wartości przyspieszenia
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    # Wykrywanie ruchu z uwzględnieniem grawitacji
    movement = abs(magnitude - 9.81)

    # Odczyt odległości z VL53L0X
    distance = distance_sensor.range

    print("Ruch:", round(movement, 2), "m/s^2")
    print("Odleglosc:", distance, "mm")

    # Warunki alarmu
    if movement > movement_limit and distance < 300:
        print("!!! ALARM !!!")
    else:
        print("OK")

    print("----------------------")

    time.sleep(0.5)
