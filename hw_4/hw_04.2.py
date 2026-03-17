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


def test_loading_images(driver: webdriver.Firefox) -> None:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    time.sleep(6)
    container = driver.find_element(By.ID, "image-container")
    images = container.find_elements(By.TAG_NAME, "img")
    third_image = images[2]
    alt_value = third_image.get_attribute("alt")
    assert alt_value == "award", f"Expected 'award', but got '{alt_value}'"
