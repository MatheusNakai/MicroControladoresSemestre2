#!/usr/bin/env python
from adafruit_bme280 import basic as adafruit_bme280
from fastapi import FastAPI
import board
import sqlite3

con = sqlite3.connect("/home/pi/Desktop/WeatherStation/logs.db")

cur = con.cursor()
#cur.execute(f"CREATE TABLE logs (temperatura,humidade,pressao,alt)")
import json

app = FastAPI()

i2c = board.I2C()
bme280= adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)


@app.get('/')
async def home():
    cur = con.cursor()

    temp = bme280.temperature
    humid= bme280.relative_humidity
    press= bme280.pressure
    alit = bme280.altitude
    dicio = {
        "temperatura":temp,
        "humidade":humid,
        "pressao":press,
        "alt":alit
        }
    jsonOb = json.dumps(dicio)
    keys = ""
    values = ""
    for key, value in dicio.items():
        keys += f"'{key}',"
        values+= f"{value},"
    keys = keys[:-1]
    values = values[:-1]
    query = f"INSERT INTO logs ({keys}) VALUES ({values})"
    cur.execute(query)
    cur.close()

    return {
        "temperatura":f"{temp:.2f}",
        "humidade":f"{humid:.2f}",
        "pressao":f"{press:.2f}",
        "alt":f"{alit:.2f}"
        }