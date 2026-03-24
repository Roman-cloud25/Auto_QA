import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.globalsqa.com/demo-site/draganddrop/"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 15)
    try:
        consent_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.fc-button.fc-cta-consent")
            )
        )
        consent_button.click()
    except Exception:
        pass

    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )

    browser.switch_to.frame(iframe)

    first_photo = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#gallery li:first-child")
        )
    )

    trash = wait.until(
        EC.visibility_of_element_located((By.ID, "trash"))
    )

    assert len(browser.find_elements(By.CSS_SELECTOR, "#gallery li")) == 4

    ActionChains(browser).drag_and_drop(first_photo, trash).perform()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#trash li"))
    )

    trash_count = len(browser.find_elements(By.CSS_SELECTOR, "#trash li"))

    gallery_count = len(browser.find_elements(By.CSS_SELECTOR, "#gallery li"))

    assert trash_count == 1
    assert gallery_count == 3

    browser.switch_to.default_content()

