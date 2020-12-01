from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_add_book_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/" \
           "catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.button_add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.title_of_book_same()
    page.price_same()
