import time
from typing import Generator
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver() -> Generator[webdriver.Firefox, None, None]:
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_text_change(driver: webdriver.Firefox) -> None:
    driver.get("http://uitestingplayground.com/textinput")
    time.sleep(2)
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")
    time.sleep(2)
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    time.sleep(2)
    button_text = button.text
    assert button_text == "ITCH", f"Expected 'ITCH', but got '{button_text}'"
