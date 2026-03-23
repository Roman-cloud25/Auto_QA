from typing import Generator
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver() -> Generator[webdriver.Firefox, None, None]:
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_text_change(driver: webdriver.Firefox) -> None:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("ITCH")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH")
    )
    button_text = button.text
    assert button_text == "ITCH", f"Expected 'ITCH', but got '{button_text}'"
