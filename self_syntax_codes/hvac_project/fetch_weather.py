#The script retrieves the current temperature for a given city using API. 
#It needs the city code which can be fetched from city.json file(also provided).
#The script should be executed once in an interval of 15 mins. This stands as an API limitation.
#
#Written on 04/26/2018
#

import urllib2
import json
import time

API_ID="a68ee39f1943509d4321114f4eac3643"
CITY_ID="1259229"							#Change as per the city code. Currently set for Pune.


URL="http://api.openweathermap.org/data/2.5/weather?id="+CITY_ID+"&APPID="+API_ID

try:	
	resp=urllib2.urlopen(URL)
	#print resp.read()
	json_inp=resp.read()
except Exception, e:
	print "Error connecting to URL: Check your network connection"

w_dict=json.loads(json_inp)

temp=w_dict['main']['temp']
temp=temp-273
temp=str(temp)

city=w_dict['name']
hum=str(w_dict['main']['humidity'])

print city+" weather report:\n"+time.asctime(time.localtime())+"\nTemperature : "+temp+"\nHumidity : "+hum

	



