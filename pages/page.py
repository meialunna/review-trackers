from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BestSellersPageLocators
from pages.locators import ProductPageLocators
from pages.locators import WishlistPageLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class BestSellersPage(BasePage):
    def open(self):
        self.driver.get(BestSellersPageLocators.PAGE_URL)

    def open_first_product(self):
        self.driver.find_elements_by_class_name(BestSellersPageLocators.FIRST_PRODUCT)[0].click()


class ProductPage(BasePage):
    def add_product_to_wishlist(self):
        self.wait.until(EC.visibility_of_element_located(ProductPageLocators.ADD_TO_WISHLIST))
        self.driver.find_element_by_id(ProductPageLocators.ADD_TO_WISHLIST_ID).click()
        self.wait.until(EC.visibility_of_element_located(ProductPageLocators.ADDED_TO_WISHLIST))

    def product_title(self):
        return self.driver.find_element_by_class_name(ProductPageLocators.PRODUCT_TITLE).text


class WishlistPage(BasePage):
    def open(self):
        self.driver.find_element_by_class_name(WishlistPageLocators.WISHLIST_ICON).click()

    def clear_all_wishlist(self):
        self.driver.find_element_by_xpath(WishlistPageLocators.CLEAR_ALL_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(WishlistPageLocators.REMOVE_ALL_BUTTON))
        self.driver.find_element_by_xpath(WishlistPageLocators.REMOVE_ALL_BUTTON_XPATH).click()

