from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, " #login_link")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, " #login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, " #register_form")


class ProductPageLocators:
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR,
                          ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME,
                    'h1')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR,
                           '#messages > div:nth-child(1) > div > strong')
    BASKET_PRICE = (By.CSS_SELECTOR,
                    "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,
                     "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,
                       ".alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
