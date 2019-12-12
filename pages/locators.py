from selenium.webdriver.common.by import By


class BestSellersPageLocators():
    PAGE_URL = 'https://www.gouletpens.com/collections/best-selling-fountain-pens'
    FIRST_PRODUCT_CLASS = 'findify-components--cards--product'


class ProductPageLocators():
    ADD_TO_WISHLIST_ID = 'bookmarkit'
    ADD_TO_WISHLIST_LOCATOR = (By.ID, ADD_TO_WISHLIST_ID)
    ADDED_TO_WISHLIST_LOCATOR = (By.XPATH, "//div[@status='bookmarked']")
    PRODUCT_TITLE_CLASS = 'product-info__title'


class WishlistPageLocators():
    WISHLIST_ICON_CLASS = 'header__account-nav-link--wishlist'
    CLEAR_ALL_BUTTON = '//a[contains(@class, "clearall")]'
    REMOVE_ALL_BUTTON_XPATH = "//button[@id='modal_remove_all_button']"
    REMOVE_ALL_BUTTON_LOCATOR = (By.XPATH, REMOVE_ALL_BUTTON_XPATH)
    PRODUCT_TITLE_LOCATOR = (By.CLASS_NAME, "product_title")
    EMPTY_WISHLIST_LOCATOR = (By.CLASS_NAME, 'empty-wishlist')
