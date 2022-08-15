from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import math


class ProductPage(BasePage):
    def add_product_to_basket(self):
        try:
            product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            print(f"The product '{product}' has been added to the cart")
        except:
            print("There is no add to cart button")

    def product_name_matches_with_added_product(self):
        added_product = self.browser.find_element(By.CSS_SELECTOR, "#messages strong").text
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.browser.implicitly_wait(10)
        cart_product = self.browser.find_element(By.CSS_SELECTOR, "div h3 a").text
        assert cart_product == added_product, "Another product has been added to the cart"

    def product_price_matches_with_cart_price(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = str(product)
        basket_price = str(basket)
        print(f"Product price: {basket_price}")
        assert product_price == basket_price, "The prices don't match, check if any more products have been added"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
