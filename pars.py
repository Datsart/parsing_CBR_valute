import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, 'lxml')
for valute in soup.find_all('valute'):
    numcode = int(valute.find('numcode').text)
    charcode = valute.find('charcode').text
    nominal = valute.find('nominal').text
    name = valute.find('name').text
    value = valute.find('value').text
    value = round(float(value.replace(',', '.')), 2)
    print(numcode, charcode, nominal, name, value)