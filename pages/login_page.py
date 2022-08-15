from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This isn't a login page"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "There is no register form"

    def register_new_user(self, email, password):
        self.browser.find_element(By.ID, "id_registration-email").send_keys(email)
        self.browser.find_element(By.ID, "id_registration-password1").send_keys(password)
        self.browser.find_element(By.ID, "id_registration-password2").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "[name='registration_submit']").click()