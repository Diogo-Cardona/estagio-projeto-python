from src.w2excel import *
from src.scrapping import *
import random

duration = 120 #in seconds
current = []
voltage = []
url="https://www.timeanddate.com/worldclock/"
#in this test hours and minutes are "voltage" and seconds the current
scrap(duration, url, current, voltage)

#this is only to test the excel writing function and its done
# for x in range(2000):
#     value = random.randint(1 , 2000)
#     current.append(value)
#     voltage.append(value)

write2excel("teste.xlsx", "recolha", current, voltage, "PRODUCT")

print("done")