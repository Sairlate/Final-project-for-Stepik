from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
            "Your basket isn't empty"

    def should_not_be_products(self):
        try:
            self.browser.find_element(*BasketPageLocators.PRODUCTS)
            print("Basket is empty")
        except:
            return True
        return False