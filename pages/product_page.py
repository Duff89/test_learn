from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def button_add_to_cart_click(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def title_of_book_same(self):
        title_of_book = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK).text
        title_of_book_in_cart = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ITEM_HAS_BEEN_ADD_TO_BASKET).text
        assert title_of_book == title_of_book_in_cart, \
            f'title book in cart: {self.title_of_book_in_cart}, ' \
            f'title book must be: {self.title_of_book}'

    def price_same(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.COMMON_PRICE_IN_BASKET).text
        assert price_of_book in price_in_basket, \
            f'different price! now in basket: {self.price_in_basket}, ' \
            f'cost of book:{self.price_of_book}'
