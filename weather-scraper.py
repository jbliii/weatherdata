import urllib2
import re
from bs4 import BeautifulSoup

#Create/open a file called wunder.txt (which will be comma-delimited file)
f = open('wunderground-data-TUG_.txt', 'w')
f.write('city,timestamp,dayMean,aveMean,dayHigh,aveHigh,recHigh,dayLow,aveLow,recLow,aveHumidity,dayPrecip,avePrecip' + '\n')
ave_humidity = re.compile('Average Humidity')

#Iterate through cities
for c in ("KJAX","KLGA","KSEA","KDCA","KSTL","KAUS","KLAS","KSAN","KFAR","KBOS","PHNL","KMDW","KLAX","KMIA"):

	#Define city names from airport codes
	if c == "KJAX":
		city = "Jacksonville"
	elif c == "KLGA":
		city = "New York City"
	elif c == "KSEA":
		city = "Seattle"
	elif c == "KDCA":
		city = "Washington DC"
	elif c == "KSTL":
		city = "St Louis"
	elif c == "KAUS":
		city = "Austin"
	elif c == "KLAS":
		city = "Las Vegas"
	elif c == "KSAN":
		city = "San Diego"
	elif c == "KFAR":
		city = "Fargo"
	elif c == "KBOS":
		city = "Boston"
	elif c == "PHNL":
		city = "Honolulu"
	elif c == "KMDW":
		city = "Chicago"
	elif c == "KLAX":
		city = "Los Angeles"
	elif c == "KMIA":
		city = "Miami"

	#Iterate through months and day
	for y in range(2001,2016):
	  for m in range(1,13):
		for d in range(1,32):

		  #Check if already gone through month
		  if (m == 2 and d > 28):
			break
		  elif (m in [4, 6, 9, 11] and d > 30):
			break

		  #Open wunderground.com url
		  timestamp = str(y) + str(m) + str(d)
		  print "Getting data for " + c + '-' + timestamp
		  url = "http://www.wunderground.com/history/airport/" + c + "/" + str(y) + "/" + str(m) + "/" + str(d) + "/DailyHistory.html"
		  page = urllib2.urlopen(url)

		  #Get temperature from page
		  soup = BeautifulSoup(page)
		  #values = soup.body.wx-value.string
		  dayMean = soup.findAll(attrs={"class":"wx-value"})[0].string
		  aveMean = soup.findAll(attrs={"class":"wx-value"})[1].string
		  dayHigh = soup.findAll(attrs={"class":"wx-value"})[2].string
		  aveHigh = soup.findAll(attrs={"class":"wx-value"})[3].string
		  recHigh = soup.findAll(attrs={"class":"wx-value"})[4].string
		  dayLow = soup.findAll(attrs={"class":"wx-value"})[5].string
		  aveLow = soup.findAll(attrs={"class":"wx-value"})[6].string
		  recLow = soup.findAll(attrs={"class":"wx-value"})[7].string
		  aveHum = soup.find('td',text=ave_humidity).find_next('td').string
		  dayPrecip = soup.findAll(attrs={"class":"wx-value"})[9].string
		  avePrecip = soup.findAll(attrs={"class":"wx-value"})[10].string
		  
		  
		  #Format year for timestamp
		  yStamp = str(y)
		  
		  #Format month for timestamp    
		  if len(str(m)) < 2:
			mStamp = '0' + str(m)
		  else:
			mStamp = str(m)

		  #Format day for timestamp
		  if len(str(d)) < 2:
			dStamp = '0' + str(d)
		  else:
			dStamp = str(d)

		  #Build timestamp
		  timestamp = yStamp + mStamp + dStamp

		  #Write timestamp and temp to file
		  f.write(city + ',' + timestamp + ',' + dayMean + ',' + aveMean + ',' + dayHigh + ',' + aveHigh + ',' + recHigh + ',' + dayLow + ',' + aveLow + ',' + recLow + ',' + aveHum + ',' + dayPrecip + ',' + avePrecip + '\n')

#Done getting data! Close file.
f.close()
