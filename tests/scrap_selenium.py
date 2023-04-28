from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#url = 'https://www.timeanddate.com/worldclock/'
url = 'https://www.pcdiga.com/secador-de-cabelo-dreame-hair-glory-hair-dryer-rosa-ahd6a-rs-6973734684256'
duration = 5

driver = webdriver.Chrome()
driver.get(url)

timer = time.time()
for i in range(4):
    v2 = driver.find_element(By.CSS_SELECTOR, "#__next").
    print(v2)
    time.sleep(1)

driver.quit()