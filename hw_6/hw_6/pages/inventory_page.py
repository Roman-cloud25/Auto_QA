from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _ADD_BTN = lambda self, product_id: (
        By.CSS_SELECTOR,
        f"[data-test='add-to-cart-{product_id}']",
    )

    PRODUCT_SLUGS = {
        "Sauce Labs Backpack": "sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "sauce-labs-onesie",
    }

    def add_to_cart(self, product_name: str):
        slug = self.PRODUCT_SLUGS[product_name]
        self.click(self._ADD_BTN(slug))
        return self

    def go_to_cart(self):
        self.click(self.CART_LINK)
