from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    INPUT_EMAIL_TO_ENTER = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_EMAIL_TO_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
