
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = r"C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(path)

driver.get("https://bitgrit.net/")

link=driver.find_element_by_link_text("Competitions")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "competition_title_12"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Participate"))
    )
    element.click()
    #element = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "lnk_register"))
    #)
    #element.click()
except  :
    driver.quit()

