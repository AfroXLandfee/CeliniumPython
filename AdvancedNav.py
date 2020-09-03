from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path = "/Users/pavlosstamos/GitHub/CeliniumPython/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count= driver.find_element_by_id("cookies")
# in all the elements that have productPrice in the name add i wich starts at 1 and ends at 0
items = [ driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1) ]


actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    cookie.click()
# splitting by the space and taking the first split element
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()



