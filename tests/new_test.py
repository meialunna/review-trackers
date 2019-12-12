import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BestSellersPage
from pages.page import ProductPage
from pages.page import WishlistPage
from pages.locators import WishlistPageLocators


class NewTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        best_sellers_page = BestSellersPage(self.driver)
        best_sellers_page.open()
        best_sellers_page.open_first_product()

        product_page = ProductPage(self.driver)
        product_page.add_product_to_wishlist()

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_wishlist(self):
        product_page = ProductPage(self.driver)
        product_title = product_page.product_title()

        wishlist_page = WishlistPage(self.driver)
        wishlist_page.open()

        self.assertTrue(EC.text_to_be_present_in_element(WishlistPageLocators.PRODUCT_TITLE_LOCATOR, product_title))

    def test_remove_all_from_wishlist(self):
        wishlist_page = WishlistPage(self.driver)
        wishlist_page.open()

        self.assertTrue(EC.presence_of_element_located(WishlistPageLocators.PRODUCT_TITLE_LOCATOR))

        wishlist_page.clear_all_wishlist()
        self.assertTrue(EC.presence_of_element_located(WishlistPageLocators.EMPTY_WISHLIST_LOCATOR))



if __name__ == '__main__':
    unittest.main()
