from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Firefox()

try:
    driver.get("https://itcareerhub.de/ru")
    driver.maximize_window()
    time.sleep(4)

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    time.sleep(4)

    payment_block = driver.find_element(By.ID, "rec1345258701")
    payment_block.screenshot("screenshots/itcareerhub.png")

finally:
    driver.quit()
