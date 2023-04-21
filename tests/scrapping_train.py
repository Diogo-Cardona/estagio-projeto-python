from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup


url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
image1, image2 = soup.find_all("img")
print(soup.title.string)
print(image1.name)
print("done first part")

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")
