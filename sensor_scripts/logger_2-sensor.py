#!/usr/bin/python

import Adafruit_DHT
import sqlite3
import os

sensor = Adafruit_DHT.DHT22
pin = 4
sensor2 = Adafruit_DHT.DHT22
pin2 = 10

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
print 'Temp: {0:0.1f} *C, Humidity: {1:0.1f}%'.format(temperature, humidity)

humidity2, temperature2 = Adafruit_DHT.read_retry(sensor2, pin2)
print 'Temp: {0:0.1f} *C, Humidity: {1:0.1f}%'.format(temperature2, humidity2)

dir_path = os.path.dirname(os.path.abspath(__file__))
# Running this script by cron messes up the relative path

try:
    db = sqlite3.connect(os.path.join(dir_path, '../raspi-weather.db'))
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS indoor(
        `id`            INTEGER PRIMARY KEY AUTOINCREMENT,
        `timestamp`     DATETIME,
        `temperature`   NUMERIC,
        `humidity`      NUMERIC,
        `temperature2`  NUMERIC,
        `humidity2`     NUMERIC)""")
    db.commit()

    args = ['now', round(temperature, 1), int(humidity), round(temperature2, 1), int(humidity2)]
    c.execute('INSERT INTO indoor (timestamp, temperature, humidity, temperature2, humidity2) VALUES (datetime(?), ?, ?, ?, ?)', args)
    db.commit()
    db.close()
except sqlite3.Error as err:
    f = open(os.path.join(dir_path, 'sensor.log'), 'a')
    print(str(err))
    f.write(str(err))
    f.write('\n')
    f.close()
