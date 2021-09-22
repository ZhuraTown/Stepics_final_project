#Тест для поиска кнопки "добавить товар в корзину" на странице link
#решить в окне задачу и выдать в консоли ответ


from .pages.product_page import PruductPage
from .pages.login_page import LoginPage

import pytest
from time import sleep



def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PruductPage(browser, link)
    page.open()
    page.should_be_basket_button()

#@pytest.mark.skip
#@pytest.mark.parametrize('number_link', [range(7),pytest.param("7",marks=pytest.mark.xfail(reason='bugged')),range(8,10)])
#def test_guest_can_add_product_to_basket(browser,number_link):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
#    page = PruductPage(browser, link)
#    page.open()
#    page.should_be_basket_button()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PruductPage(browser, link)
    page.open()
    page.click_on_the_button_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PruductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PruductPage(browser, link)
    page.open()
    page.click_on_the_button_basket()
    page.should_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PruductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()