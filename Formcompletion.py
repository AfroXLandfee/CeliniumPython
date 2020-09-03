from selenium import webdriver
#it allows us to get press keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "/Users/pavlosstamos/Desktop/Selinium/chromedriver"
driver = webdriver.Chrome(Path)

driver.get("https://techwithtim.net")
print(driver.title)

#searchbox
search = driver.find_element_by_name("s")
#it will clear the remainders in the searchbar
search.clear()
#write test
search.send_keys("test")
#send enter
search.send_keys(Keys.RETURN)

#it is the div id
# main = driver.find_element_by_id("main")

try:
    #main is the id, wait for the driver 10s until it locates  | by id main|  div
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally :
    driver.quit()
