
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    #Проверка, что в корзине нету товаров
    def should_basket_is_empty(self,language):
        #В зависимости от выбранного языка, будет проводиться проверка словом. 
        dictionary_words = {'ru': 'пуста',
                            'en-gb': 'empty',
                            'fr': "panier est vide"}
                            
        text_basket = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert dictionary_words.get(language) in text_basket, 'The basket is not empty'
    
    def should_basket_is_empty_negative(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRICE), "The basket is not empty"
        # is_not_element_present

    
    