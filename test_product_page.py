from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

@pytest.mark.notactual
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_name_product_and_basket()

@pytest.mark.actual
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.actual
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()
    
@pytest.mark.actual
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.should_be_disappeared_success_message()