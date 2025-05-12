from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Адрес логина не найден."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена."

    def register_new_user(self, email, password):
        email_find = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_find.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD_AGAIN_INPUT)
        password2_input.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        reg_button.click()