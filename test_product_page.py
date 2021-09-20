#Тест для поиска кнопки "добавить товар в корзину" на странице link
#решить в окне задачу и выдать в консоли ответ


from .pages.product_page import PruductPage
import pytest
from time import sleep

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PruductPage(browser, link)
    page.open()
    page.should_be_basket_button()


@pytest.mark.parametrize('number_link', [range(7),pytest.param("7",marks=pytest.mark.xfail(reason='bugged')),range(8,10)])
def test_guest_can_add_product_to_basket(browser,number_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
    page = PruductPage(browser, link)
    page.open()
    page.should_be_basket_button()