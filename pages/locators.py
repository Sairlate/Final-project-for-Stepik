from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTER_SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success > div")


class ProductPageLocators():
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-1 p")
    BASKET_PRICE = (By.CLASS_NAME, "total.align-right")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages strong")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "div h3 a")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
