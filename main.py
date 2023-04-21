from w2excel import *
from scrapping import *
import random

duration = 10 #in seconds
current = []
voltage = []
percentage = []
url="https://www.timeanddate.com/worldclock/" #web interface of go1 robot: 192.168.12.1
#in this test hours and minutes are "voltage" and seconds the current
scrap(duration, url, current, voltage, percentage)

#this is only to test the excel writing function and its done
# for x in range(2000):
#     value = random.randint(1 , 2000)
#     current.append(value)
#     voltage.append(value)

write2excel("teste.xlsx", "recolha", current, voltage, percentage,  "PRODUCT")

print("done")