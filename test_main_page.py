#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()
#
#from .pages.main_page import MainPage
#
#
#def go_to_login_page(browser):
#    login_link = browser.find_element_by_css_selector("#login_link")
#  link = "http://selenium1py.pythonanywhere.com/"
 
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from time import sleep

from .pages.login_page import LoginPage
 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



@pytest.mark.smoke
def test_url_for_login_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()

@pytest.mark.smoke
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()

@pytest.mark.smoke
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_register_form()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser,request):
    link = f"http://selenium1py.pythonanywhere.com/{request.config.getoption('language')}"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.should_basket_is_empty_negative()
    page.should_basket_is_empty(request.config.getoption('language')) # Для удобства определения языка, нужно для вызова метода отправлять ему язык в строке
    
    #Гость открывает главную страницу
    #Переходит в корзину по кнопке в шапке сайта
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста