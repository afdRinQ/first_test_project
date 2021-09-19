from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        product_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        product_button.click()

    def should_be_product_page(self):
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text ==\
               self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text,\
            f" 'ожидали' " \
            f" '{self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text}'" \
            f" 'получили'" \
            f" '{self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text}'"

    def should_be_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text ==\
               self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text,\
            f" 'ожидали'" \
            f"'{self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text}'" \
            f" 'получили'" \
            f" '{self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text}'"
