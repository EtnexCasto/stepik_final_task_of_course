from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.actual
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_url = browser.current_url
        login_page = LoginPage(browser, login_url)

        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, password="12341231249109419")
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.add_to_basket()



@pytest.mark.neactual
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_name_product_and_basket()

@pytest.mark.neactual
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.neactual
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()
    
@pytest.mark.neactual
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.should_be_disappeared_success_message()

@pytest.mark.neactual
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.neactual
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()