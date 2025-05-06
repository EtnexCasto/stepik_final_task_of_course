from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_btn.click()
    
    def should_be_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Кнопка 'Добавить в корзину' не найдена."

    def take_name_of_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        return name.text
    
    def take_price_of_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return price.text

    def should_be_equal_name_product_and_basket(self):
        strong_name = self.browser.find_element(*ProductPageLocators.STRONG_NAME_PRODUCT)
        assert strong_name.text == ProductPage.take_name_of_product(self), "Название товара не совпадает с добавленным в корзину."

    def should_be_equal_price_product_and_basket(self):
        strong_price = self.browser.find_element(*ProductPageLocators.STRONG_PRICE_PRODUCT)
        assert strong_price.text == ProductPage.take_price_of_product(self), "Цена товара не совпадает с ценой в корзине."