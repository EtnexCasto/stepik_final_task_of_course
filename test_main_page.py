import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_url = browser.current_url
    login_page = LoginPage(browser, login_url)
    login_page.should_be_login_page()

@pytest.mark.actual
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,  link)
    page.open()

    page.go_to_basket()
    basket_url = browser.current_url
    basket_page = BasketPage(browser, basket_url)
    basket_page.should_not_be_basket_form()
    basket_page.should_be_message_basket_empty()