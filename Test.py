from selenium import webdriver
#it allows us to get press keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "/Users/pavlosstamos/GitHub/CeliniumPython/chromedriver"
driver = webdriver.Chrome(path)

page = driver.get("https://google.com")

time.sleep(3)

try:
    fbutton = driver.find_element_by_id("introAgreeButton")
    fbutton.click()
except :
    pass

sbox = driver.find_element_by_name("q")
sbox.clear()
sbox.send_keys("YouTube", Keys.ENTER )

assert "No results found." not in driver.page_source
driver.find_element_by_xpath('(//div[@class="r"]/a)[1]').click()

time.sleep(0)

try:
    fbutton = driver.find_element_by_tag_name("paper-button")
    fbutton.click()
except :
    pass

ytbox = driver.find_element_by_id("search")
ytbox.clear()
ytbox.send_keys("Breaking Me", Keys.RETURN)




