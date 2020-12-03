from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators
from selenium import webdriver


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert "Your basket is empty" in self.browser.find_element(
            *BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text, "Basket is not empty"
