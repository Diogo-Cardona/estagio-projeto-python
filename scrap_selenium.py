from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def parse_arg(voltage, current, percentage, arg):
    # Split the string into lines
    lines = arg.split("\n")
    for line in lines:
        # Extract the SOC and removes % and stores it to a vector
        match = re.search(r'^SOC\s*:\s*(\d+)%$', line)
        if match:
            percentage.append(match.group(1))
        # Extract the Voltage and removes mV and stores it to a vector
        match = re.search(r'^Voltage\s*:\s*(\d+)mV$', line)
        if match:
            voltage.append(match.group(1))
        # Extract the Current and removes mA and stores it to a vector
        match = re.search(r'^Current\s*:\s*(\d+)mA$', line)
        if match:
            current.append(match.group(1))
    

 
def scrap_sel(duration, url, current, voltage, percentage, tempo)
    driver = webdriver.Chrome()
    driver.get(url)
    timer = time.time()
    while time.time() - timer < duration:
        v2 = driver.find_element(By.XPATH, '//*[@id="bmsPage"]')
        my_string = v2.text
        parse_arg(voltage, current, percentage, my_string)
        moment = time.time() - timer
        tempo.append(moment)
        time.sleep(0.5)
    driver.quit()