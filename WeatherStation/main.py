import board
from adafruit_bme280 import basic as adafruit_bme280
from fastapi import FastAPI

app = FastAPI()
i2c = board.I2C()
bme280= adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)

print(bme280.temperature)
print(bme280.humidity)
print(bme280.pressure)