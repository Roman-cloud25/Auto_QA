import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_screenshot(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.get("https://itcareerhub.de/ru")
    time.sleep(4)

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    time.sleep(4)

    payment_block = driver.find_element(By.ID, "rec1345258701")
    payment_block.screenshot("screenshots/itcareerhub.png")
