from selenium.webdriver.common.by import By

class MainPageLocators():
    ...

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")
    STRONG_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    STRONG_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn-default")