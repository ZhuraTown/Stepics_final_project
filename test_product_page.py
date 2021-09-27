


from .pages.product_page import PruductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest
import time

LINK_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
LINK_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope='function', autouse=True) 
    def setup(self,browser,request):
        link = f"http://selenium1py.pythonanywhere.com/{request.config.getoption('language')}"
        email,password = str(time.time()) + "@fakemail.org" ,'000000hsj'
        page = LoginPage(browser,link)
        page.open()
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self,browser):
        link = LINK_PROMO
        page = PruductPage(browser, link)
        page.open()
        page.should_be_basket_button()


    def test_user_cant_see_success_message(self,browser):
        link = LINK_PAGE
        page = PruductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = LINK_PROMO
    page = PruductPage(browser, link)
    page.open()
    page.should_be_basket_button()


@pytest.mark.parametrize('number_link', [range(7),pytest.param("7",marks=pytest.mark.xfail(reason='bugged')),range(8,10)])
def test_guest_can_add_product_to_basket(browser,number_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
    page = PruductPage(browser, link)
    page.open()
    page.should_be_basket_button()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LINK_PAGE
    page = PruductPage(browser, link)
    page.open()
    page.click_on_the_button_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = LINK_PAGE
    page = PruductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LINK_PAGE
    page = PruductPage(browser, link)
    page.open()
    page.click_on_the_button_basket()
    page.should_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = LINK_PAGE
    page = PruductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = LINK_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser,request):
    link = f"http://selenium1py.pythonanywhere.com/{request.config.getoption('language')}/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.should_basket_is_empty_negative()
    page.should_basket_is_empty(request.config.getoption('language'))

    
    
    
    