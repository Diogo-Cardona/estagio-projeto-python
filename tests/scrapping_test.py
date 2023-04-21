from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import time


url = "https://www.timeanddate.com/worldclock/"
browser = mechanicalsoup.Browser()

#xpath //*[@id="c320"]
for x in range(3):
    page = browser.get(url)
    print(page)
    
    if x < 3:
        time.sleep(60)


