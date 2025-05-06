from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")
    STRONG_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    STRONG_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alertinner p strong")
