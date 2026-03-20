import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text_presence(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    expected_text = "semper posuere integer et senectus justo curabitur."

    text_locator = (By.XPATH, f"//*[contains(normalize-space(.), '{expected_text}')]")

    text_element = wait.until(EC.visibility_of_element_located(text_locator))

    assert text_element.is_displayed(), "Error: Text not found"
