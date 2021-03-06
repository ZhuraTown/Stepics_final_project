from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

from time import sleep

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
    #метод для захода на страницу залогинивания
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
    
    def find_and_paste_text(self,find_el,text):
        self.browser.find_element(*find_el).send_keys(text)
    
    def register_new_user(self,email,password):
        self.go_to_login_page()
        self.find_and_paste_text(LoginPageLocators.REGISTER_EMAIL,email)
        self.find_and_paste_text(LoginPageLocators.REGISTER_PASSWORD, password)
        self.find_and_paste_text(LoginPageLocators.REGISTER_CONFIRM_PASSWORD, password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        sleep(3)
    
    #метод для проверки корректности ссылки на логин на сайте
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_IN_ASSERT in self.browser.current_url, " 'Login' is not found in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"