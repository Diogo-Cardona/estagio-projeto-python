from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap(duration, url, current, voltage, percentage, tempo):
    driver = webdriver.Chrome()
    driver.get(url)
    
    timer = time.time()
    while time.time() - timer < duration:
        #v1 = driver.find_element(By.XPATH, '//*[@id="bmsPage"]/div[10]/text() ').text
        v2 = driver.find_element(By.XPATH, '//*[@id="bmsPage"]/div[4]/').text
        #                                        //*[@id="c320"]
        #v3 = driver.find_element(By.XPATH, ' ').text
        moment = time.time() - timer
        tempo.append(moment)
        #voltage.append(v1)
        current.append(v2)
        #percentage.append(v3)
        time.sleep(1)

    driver.quit()




