import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"

TARGET_TEXT = "semper posuere integer et senectus justo curabitur."


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_text_in_iframe(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 10)

    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe")
        )
    )

    text_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "p")
        )
    )

    assert TARGET_TEXT in text_element.text, f"Text '{TARGET_TEXT}' not found"

    assert text_element.is_displayed(), f"Text '{TARGET_TEXT}' found"

    browser.switch_to.default_content()
te--    c