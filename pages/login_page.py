from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Not present \'login\' in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина

        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL_TO_ENTER), "not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице

        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL_TO_REGISTER), "not register form"
