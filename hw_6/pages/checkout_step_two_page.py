from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def get_total(self) -> str:
        return self.get_text(self.TOTAL_LABEL)

    def get_total_amount(self) -> float:
        raw = self.get_total()
        amount = raw.split("$")[-1]
        return float(amount)
