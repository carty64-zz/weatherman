import urllib
import json
import time
# -*- coding: UTF-8 -*-

response = urllib.urlopen ('https://api.forecast.io/forecast/a7c7969da1021ba738c1faf83d35fc0e/37.7782,-122.4122').read()
json = json.loads(response)

#file = open('weatherjson.json', 'r')
#data = file.read()
#json = json.loads(data, encoding="utf-8")


summary = json['hourly']['summary']
summary = summary.lower()
t0 = int(time.time())
temp_current = int(round(json['currently']['temperature'],1))
x = 0
#temps = []
#for hour in json['hourly']['data']:
#  temps.append(hour['temperature'])

#times = []
#for t in json['hourly']['data']:
#  times.append(t['time'])

#rain = []
#for r in json['hourly']['data']:
#  rain.append(r['precipProbability'])

#print t0
#print (times[0] - t0)/60, (times[1] - t0)/60, (times[2] - t0)/60

#if json['hourly']['data'][1]['time'] - t0 > 30:
# print 'greater'
#else:
# print 'less'
rain = json['hourly']['data'][x]['precipProbability'] * 100
#temp1 = int(temps[0])
#temp2 = int(temps[1])

#print int(temps[x])

# data[1] is the best place to start for forecast
print "%i with %i%% chance of rain. Then %s" % (temp_current,rain,summary)
x = int(raw_input('How far ahead? '))
