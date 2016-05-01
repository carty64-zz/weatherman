import urllib
import json
import time
# -*- coding: UTF-8 -*-

response = urllib.urlopen ('https://api.forecast.io/forecast/API_KEY/37.7782,-122.4122').read()
json = json.loads(response)

#file = open('weatherjson.json', 'r')
#data = file.read()
#json = json.loads(data, encoding="utf-8")

forecast = []
temps = []

summary = json['hourly']['summary']
summary = summary.lower()
t0 = int(json['currently']['time'])
temp_current = int(round(json['currently']['temperature'],1))

for hour in json['hourly']['data']:
  temps.append(hour['temperature'])

if json['hourly']['data'][1]['time'] - t0 > 30:
 print 'greater'
else:
 print 'less'

temp1 = int(temps[0])
temp2 = int(temps[1])

# data[1] is the best place to start for forecast

forecast1 = int(json['hourly']['data'][1]['temperature'])
forecast3 = int(json['hourly']['data'][3]['temperature'])
cor1 = int(json['hourly']['data'][1]['precipProbability']) * 100
cor3 = int(json['hourly']['data'][3]['precipProbability']) * 100
print "%i with %i%% chance of rain. Then %s" % (temp_current,cor1,summary)
#print forecast3
