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


def test_loading_images(driver: webdriver.Firefox) -> None:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    container = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "image-container"))
    )

    WebDriverWait(driver, 15).until(
        lambda d: len(container.find_elements(By.TAG_NAME, "img")) >= 3
        and all(
            img.get_attribute("src")
            for img in container.find_elements(By.TAG_NAME, "img")
        )
    )

    images = container.find_elements(By.TAG_NAME, "img")
    third_image = images[2]
    alt_value = third_image.get_attribute("alt")
    assert alt_value == "award", f"Expected 'award', but got '{alt_value}'"
