from .base_page import BasePage

from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "Your basket is empty" in self.browser.find_element(By.CSS_SELECTOR, "#content_inner p").text, \
            "Your basket isn't empty"

    def should_not_be_products(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".basket-items")
            print("Basket is empty")
        except:
            return True
        return False