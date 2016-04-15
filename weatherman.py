import urllib
import json as m_json
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
    while(1):
        response = urllib.urlopen ('https://api.forecast.io/forecast/KEY/37.7782,-122.4122').read()
        json = m_json.loads(response)
        temp = json['currently']['temperature']
        if temp < 55:
            print temp
            GPIO.output(12, True)
            time.sleep(10)
        elif temp > 55 and temp < 67:
            print temp
            GPIO.output(16, True)
            time.sleep(10)
        elif temp >= 67:
            print temp
            GPIO.output(18, True)
            time.sleep(10)
        else:
            print temp
            time.sleep(10)

except KeyboardInterrupt:
    print "Interrupted :("

finally:
    GPIO.cleanup()
#
# n = n - 1 time.sleep(t)
#
#
#
# t = (0.8)
#
# while (t > 0.2):
#   GPIO.output(18, True)
#   time.sleep(t)
#   GPIO.output(18, False)
#   time.sleep(t)
#   t = t-0.1
# t = 0.1
# n = 8
# while (n > 0):
#  GPIO.output(18, True)
#  time.sleep(t)
#  GPIO.output(18, False)
