import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = 'https://www.pcdiga.com/secador-de-cabelo-dreame-hair-glory-hair-dryer-rosa-ahd6a-rs-6973734684256' # http://192.168.12.1/bms
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

#teste1 = soup.find_all('div' )#,class_="flex gap-x-4 items-center")




