import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
from datetime import datetime


page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
dollars = soup.find('table',class_='mfd-table mfd-currency-table')
kurs = dollars.find_all('tr')

date = []
prices = []

for i in kurs:
	tdq = i.find_all('td')
	if len(tdq) > 0:
		date.append(datetime.strptime(tdq[0].text[2:], '%d.%m.%Y'))
		prices.append(float(tdq[1].text))

pyplot.plot(date, prices)
pyplot.show()



