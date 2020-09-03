from selenium.webdriver.common.keys import Keys
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "/Users/pavlosstamos/GitHub/CeliniumPython/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net/")

#this is the text of the link
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    btn.click()

    driver.back()
    driver.back()
    driver.back()
    
except :
    driver.quit()

