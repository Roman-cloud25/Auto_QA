import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 15)
    try:
        consent_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Consent') or contains(., 'Accept')]"))
        )
        consent_button.click()
        print("Consent popup closed")
    except:
        print("Consent popup did not appear")

    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    driver.switch_to.frame(iframe)

    first_photo = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li:first-child"))
    )

    trash = driver.find_element(By.ID, "trash")

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", trash)
    time.sleep(2)

    actions = ActionChains(driver)

    actions.click_and_hold(first_photo)
    actions.pause(0.8)
    actions.move_by_offset(20, 20)
    actions.pause(0.6)
    actions.move_to_element(trash)
    actions.pause(1.0)
    actions.release()
    actions.perform()

    time.sleep(3)

    trash_count = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))
    gallery_count = len(driver.find_elements(By.CSS_SELECTOR, "#gallery li"))

    assert trash_count == 1, f"There should be 1 photo in the basket, but it turned out {trash_count}"
    assert gallery_count == 3, f"There should be 3 photos left in the gallery, but it turned out that way {gallery_count}"

    driver.switch_to.default_content()