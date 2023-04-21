from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap(duration, url, current, voltage, percentage):
    driver = webdriver.Chrome()
    driver.get(url)

    timer = time.time()
    while time.time() - timer < duration:
        v1 = driver.find_element(By.XPATH, '//*[@id="c320"]').text
        v2 = driver.find_element(By.XPATH, '//*[@id="c320sec"]').text
        #v3 = driver.find_element(By.XPATH, ' ').text
        current.append(v2)
        voltage.append(v1)
        #percentage.append(v3)
        time.sleep(1)

    driver.quit()




