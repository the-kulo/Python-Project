import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.hnust.edu.cn/cms/web/search/index.jsp")
search = driver.find_element(By.NAME, "query")
search.send_keys("万步炎")
search.send_keys(Keys.RETURN)

time.sleep(10)

titles = driver.find_elements(By.TAG_NAME, "h2")
for title in titles:
    print(title.text)

time.sleep(5)
driver.quit()
