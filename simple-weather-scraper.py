import urllib2
from bs4 import BeautifulSoup

#Create/open a file called wunder.txt (which will be comma-delimited file)
f = open('sample-weather-data.txt', 'w')
f.write('city,timestamp,dayMean,dayHigh,dayLow,dayPrecip' + '\n')

#Iterate through months and day
for d in range(1,8):

  #Open wunderground.com url
  timestamp = "2016/1/" + str(d)
  print "Getting data for JAX - " + timestamp
  url = "http://www.wunderground.com/history/airport/KJAX/2016/1/" + str(d) + "/DailyHistory.html"
  page = urllib2.urlopen(url)

  #Get temperature from page
  soup = BeautifulSoup(page)
  #values = soup.body.wx-value.string
  dayMean = soup.findAll(attrs={"class":"wx-value"})[0].string
  dayHigh = soup.findAll(attrs={"class":"wx-value"})[2].string
  dayLow = soup.findAll(attrs={"class":"wx-value"})[5].string
  dayPrecip = soup.findAll(attrs={"class":"wx-value"})[9].string
  
  #Write timestamp and temp to file
  f.write('Jacksonville,' + timestamp + ',' + dayMean + ',' + dayHigh + ',' + dayLow + ',' + dayPrecip + '\n')

#Done getting data! Close file.
f.close()
