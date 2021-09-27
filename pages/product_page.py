
from .base_page import BasePage
from .locators import ProductPageLocators
from time import sleep

class PruductPage(BasePage):
    
    def should_be_basket_button(self):
        self.guest_should_see_button_add_basket()
        self.click_on_the_button_basket()
        self.solve_quiz_and_get_code()
        self.should_name_in_basket_correct()
        self.should_price_in_basket_correct()
    
    #метод  поиска кнопки "добавить в корзину" и нажатия на неё
    def click_on_the_button_basket(self):
        button_busket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)
        button_busket.click()
        sleep(1)
    
    
    
    #метод проверки нахождения кнопки "добавить в корзину"
    def guest_should_see_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BASKET_BUTTON), "The button 'add to basket' is not presented"
    
    def should_name_in_basket_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BOOK).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME).text
        assert product_name == product_name_basket, "Added book to cart and chosen one are different"
    
    def should_price_in_basket_correct(self):
        price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text
        assert price_page == price_basket, "The cost of the selected books and baskets is different"
    
    #проверка, если нет сообщения, то падаем
    #def should_not_be_success_message(self):
    #    assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
    
    #проверка, если есть сообщение то падаем
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    #success_message_is_disappeared
    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"