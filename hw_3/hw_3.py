import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://itcareerhub.de/ru")
    time.sleep(4)


    cookie_btns = driver.find_elements(By.XPATH, "//*[normalize-space(text())='Подтвердить']")
    if cookie_btns:
        cookie_btns[0].click()
        time.sleep(1)

    yield driver
    driver.quit()



def find_visible(driver: webdriver.Firefox, xpath: str):

    elements = driver.find_elements(By.XPATH, xpath)

    return next(el for el in elements if el.is_displayed())




def test_logo_is_displayed(driver: webdriver.Firefox) -> None:

    print("\n>>> TEST: Logo")
    time.sleep(1)


    logo = driver.find_element(By.XPATH, "//img[contains(@alt, 'IT Career Hub')]")
    time.sleep(1)

    assert logo.is_displayed()
    print("    PASS: logo is found and visible ")


def test_link_programs_is_displayed(driver: webdriver.Firefox) -> None:

    print("\n>>> TEST: Link 'Programs'")
    time.sleep(1)

    link = find_visible(driver, "//*[normalize-space(text())='Программы']")
    time.sleep(1)

    assert link.is_displayed()
    print("    PASS: Link 'Programs' found and visible ")


def test_link_payment_is_displayed(driver: webdriver.Firefox) -> None:


    print("\n>>> TEST: Link 'Payment methods'")
    time.sleep(1)

    link = find_visible(driver, "//*[normalize-space(text())='Способы оплаты']")
    time.sleep(1)

    assert link.is_displayed()
    print("    PASS: Link 'Payment methods' found and visible")


def test_link_about_us_is_displayed(driver: webdriver.Firefox) -> None:

    print("\n>>> TEST: Link 'About us'")
    time.sleep(1)

    link = find_visible(driver, "//*[normalize-space(text())='О нас']")
    time.sleep(1)

    assert link.is_displayed()
    print("    PASS: Link 'About us' found and visible ")


def test_language_buttons_are_displayed(driver: webdriver.Firefox) -> None:

    print("\n>>> TEST: Language buttons ru / de")
    time.sleep(1)


    driver.get("https://itcareerhub.de/")
    time.sleep(4)


    cookie_btns = driver.find_elements(
        By.XPATH,
        "//button[.//*[contains(text(), 'Подтвердить')] or .//*[contains(text(), 'Bestätigen')]]"
        " | //a[.//*[contains(text(), 'Подтвердить')] or .//*[contains(text(), 'Bestätigen')]]"
    )

    if cookie_btns:
        for btn in cookie_btns:
            if btn.is_displayed():
                btn.click()
                break
        time.sleep(1)


    btns_ru = driver.find_elements(By.XPATH, "//a[@href='https://itcareerhub.de/ru']")
    time.sleep(1)

    btns_de = driver.find_elements(
        By.XPATH,
        "//a[@href='https://itcareerhub.de/' or @href='https://itcareerhub.de']"
    )
    time.sleep(1)

    assert len(btns_ru) > 0, "Кнопка 'ru' не найдена в HTML"
    print("    PASS: кнопка 'ru' найдена в HTML")

    assert len(btns_de) > 0, "Кнопка 'de' не найдена в HTML"
    print("    PASS: кнопка 'de' найдена в HTML")

    print("    PASS: обе кнопки языка присутствуют на странице!")


