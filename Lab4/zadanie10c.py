
from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

# Maksymalne wartości dla osi X, Y, Z
max_gx = 0
max_gy = 0
max_gz = 0

print("Rozpoczynam pomiar przez 10 sekund...")

start_time = time.time()

while time.time() - start_time < 10:
    gyro = sensor.get_gyro_data()

    gx = abs(gyro['x'])
    gy = abs(gyro['y'])
    gz = abs(gyro['z'])

    # Aktualizacja maksymalnych wartości
    if gx > max_gx:
        max_gx = gx

    if gy > max_gy:
        max_gy = gy

    if gz > max_gz:
        max_gz = gz

    time.sleep(0.05)

print("\nMaksymalna predkosc obrotowa:")
print(f"X: {max_gx:.1f} deg/s")
print(f"Y: {max_gy:.1f} deg/s")
print(f"Z: {max_gz:.1f} deg/s")
