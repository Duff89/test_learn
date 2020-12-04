from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    INPUT_EMAIL_TO_ENTER = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_EMAIL_TO_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")
    COMMON_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    MESSAGE_ITEM_HAS_BEEN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasketPageLocators:
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_PRESENT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
