# This script by Mykhailenko Vladyslav 😁 https://github.com/VladyslavMykhailenko

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def delay():
    time.sleep(random.randint(2, 4))

driver = webdriver.Chrome()
#check gmail
driver.get("https://www.google.com/account/about/")
driver.maximize_window()
delay()  # simulate long running test
driver.find_element(By.PARTIAL_LINK_TEXT, "Go to Google Account").click()
driver.find_element(By.ID, "identifierId").send_keys("qat0368@gmail.com")
delay()  # simulate long running test
driver.find_element(By.XPATH, "//*[text()='Next']").click()
delay()  # simulate long running test
driver.find_element(By.XPATH, "//*[@type='password']").send_keys("gfhjkmgfhjkm!`")
delay()  # simulate long running test
driver.find_element(By.XPATH, "//*[text()='Next']").click()
delay()  # simulate long running test
driver.get("https://mail.google.com/mail/")
delay()  # simulate long running test
# closing the browser
driver.quit()