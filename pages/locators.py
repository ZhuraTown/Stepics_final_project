
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_IN_ASSERT = ('login')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

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