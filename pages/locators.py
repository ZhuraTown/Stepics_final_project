
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_IN_ASSERT = ('login')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-emai,[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1,[name='registration-password1']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2,[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    PRODUCT_BASKET_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    
    PRODUCT_PRICE = (By.CSS_SELECTOR,'div.product_main p.price_color')
    PRODUCT_NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_BASKET_PRICE =  (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")##messages div:nth-child(3) strong
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")#a.btn.btn-default.navbar-btn.btn-cart.navbar-right
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.col-sm-1 p.price_color")
    