# This script by Mykhailenko Vladyslav 😁 https://github.com/VladyslavMykhailenko

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#check gmail
driver.get("https://www.google.com/account/about/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Go to Google Account").click()
driver.find_element(By.ID, "identifierId").send_keys("qat0368@gmail.com")
time.sleep(4)
driver.find_element(By.XPATH, "//*[text()='Next']").click()
time.sleep(4)
driver.find_element(By.XPATH, "//*[@type='password']").send_keys("gfhjkmgfhjkm!`")
time.sleep(2)
driver.find_element(By.XPATH, "//*[text()='Next']").click()
time.sleep(1)
driver.get("https://mail.google.com/mail/")

# closing the browser
driver.quit()