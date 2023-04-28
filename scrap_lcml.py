import requests
from lxml import html

url = 'https://www.timeanddate.com/worldclock/'
response = requests.get(url)

tree = html.fromstring(response.content)
value = tree.xpath('//*[@id="c320"]/text()')

print(value)