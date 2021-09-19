from first_test_project.first_test_project.pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY),\
            "Basket not empty, but should be"

    def should_be_message_empty_basket(self):
        assert len(self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text) > 1,\
            "Basket not empty, but should be"
