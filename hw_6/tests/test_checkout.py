import pytest
from pages import (
    LoginPage,
    InventoryPage,
    CartPage,
    CheckoutStepOnePage,
    CheckoutStepTwoPage,
)
import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = {
    "username": os.getenv("SAUCE_USERNAME"),
    "password": os.getenv("SAUCE_PASSWORD"),
}

PRODUCTS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie",
]

CUSTOMER = {
    "first_name": "Roman",
    "last_name": "Serhatyi",
    "postal_code": "13125",
}

EXPECTED_TOTAL = 58.29


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    login_page.open().login(
        CREDENTIALS["username"],
        CREDENTIALS["password"],
    )

    inventory_page = InventoryPage(driver)
    for product in PRODUCTS_TO_ADD:
        inventory_page.add_to_cart(product)

    inventory_page.go_to_cart()

    CartPage(driver).proceed_to_checkout()

    CheckoutStepOnePage(driver).fill_form(
        first_name=CUSTOMER["first_name"],
        last_name=CUSTOMER["last_name"],
        postal_code=CUSTOMER["postal_code"],
    )

    total = CheckoutStepTwoPage(driver).get_total_amount()

    assert total == pytest.approx(EXPECTED_TOTAL), (
        f"Expected amount: ${EXPECTED_TOTAL}, "
        f"Actual amount: ${total}"
    )
