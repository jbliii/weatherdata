import requests
from bs4 import BeautifulSoup

f = open('Atl_Hurricanes.txt', 'w')
g = open('Atl_Hurricane_Paths.txt', 'w')
f.write('year|name|hLink|date|maxWind|minPressure|deaths|damage|landfall' + '\n')
g.write('year|name|hLink|pathIndex|pDate|pTime|latitude|longitude|wind|pressure|stormType|safSimp' + '\n')

for y in range(1900,2018):
    year = str(y)
    listPage = 'https://www.wunderground.com/hurricane/at' + year + '.asp'
    page = requests.get(listPage)
    soup = BeautifulSoup(page.text, 'html5lib')
    hurrTable = soup.find('table', id='stormList')
    hurricanes = hurrTable.findAll('tr')[1:]
    for h in hurricanes:
        name = h.find('a').string
        hLink = h.find('a')['href']
        date = h.findAll('td')[1].string
        maxWind = h.findAll('td')[2].string.replace('\n','').strip()
        minPressure = h.findAll('td')[3].string.replace('\n','').strip()
        if h.findAll('td')[4].string is None:
            deaths = 'NA'
            damage = 'NA'
            landfall = 'NA'
        else:
            deaths = h.findAll('td')[4].string.replace('\n','').strip()
            damage = h.findAll('td')[5].string.replace('\n','').strip()
            landfall = h.findAll('td')[6].string.replace('\n','').strip().replace('\t','')
        pathPage = requests.get('https://www.wunderground.com' + hLink)
        soupPath = BeautifulSoup(pathPage.text, 'html5lib')
        pathList = soupPath.find('table', id = 'stormList')
        paths = pathList.findAll('tr')[1:]
        f.write(year + '|' + name + '|' + str(hLink) + '|' + date + '|' + maxWind + '|' + minPressure + '|' + deaths + '|' + damage + '|' + landfall + '\n')
        print(year + ' ' + name)
        for count, p in enumerate(paths, 1):
            pDate = p.findAll('td')[0].string
            pTime = p.findAll('td')[1].string
            lat = p.findAll('td')[2].string
            lon = p.findAll('td')[3].string
            pWind = p.findAll('td')[4].string
            if int(pWind)>=157:
                safSimp = '5'
            elif int(pWind)>=130:
                safSimp = '4'
            elif int(pWind)>=111:
                safSimp = '3'
            elif int(pWind)>=96:
                safSimp = '2'
            elif int(pWind)>=74:
                safSimp = '1'
            elif int(pWind)>=39:
                safSimp = '0'
            else:
                safSimp = '-1'
            pPressure = p.findAll('td')[5].string
            pStormType = p.findAll('td')[6].string.replace('\n','').strip().replace('\t','')
            g.write(year + '|' + name + '|' + str(hLink) + '|' + str(count) + '|' + pDate + '|' + pTime + '|' + lat + '|' + lon + '|' + pWind + '|' + pPressure + '|' + pStormType + '|' + safSimp + '\n')

f.close()
g.close()
