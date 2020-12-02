from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


def test_add_book_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.button_add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.title_of_book_same()
    page.price_same()


@pytest.mark.smoke
@pytest.mark.parametrize('add_link',
                         ['0', '1', '2', '3', '4', '5', '6', pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, add_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{add_link}"
    page = ProductPage(browser, link)
    page.open()
    page.button_add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.title_of_book_same()
    page.price_same()
