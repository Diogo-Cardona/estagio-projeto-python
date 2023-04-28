from w2excel import *
from scrapping import *
import random

duration = 3 #in seconds
current = []
voltage = []
percentage = []
tempo = []
url="http://192.168.12.1/bms" #web interface of go1 robot: http://192.168.12.1/bms
#in this test hours and minutes are "voltage" and seconds the current
scrap(duration, url, current, voltage, percentage, tempo)

#this is only to test the excel writing function and its done
# for x in range(2000):
#     value = random.randint(1 , 2000)
#     current.append(value)
#     voltage.append(value)

#write2excel("teste.xlsx", "recolha", current, voltage, percentage, tempo,  "PRODUCT")

print("done")