#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

sensor2 = Adafruit_DHT.DHT11
pin2 = 24

try:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print '{0:0.1f}\n{1}'.format(temperature, int(humidity))
    humidity2, temperature2 = Adafruit_DHT.read_retry(sensor2, pin2)
    print '{0:0.1f}\n{1}'.format(temperature2, int(humidity2))
except RuntimeError as e:
    print 'error\n{0}'.format(e)
except:
    print 'error\nFailed to read sensor data'
