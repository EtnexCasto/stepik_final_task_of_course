from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_not_be_basket_form(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Корзина не пуста."

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Сообщения о пустой корзине нет."

        