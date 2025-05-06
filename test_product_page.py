from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_name_product_and_basket()