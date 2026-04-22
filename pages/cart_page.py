from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from pages.inventory_page import InventoryPage


class CartPage:
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_ITEM = (By.XPATH, "//button[starts-with(@id, 'remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CONTINUE_SHOPPING_CART = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.inventory_page = InventoryPage(driver)


    def add_item_from_inventory_to_cart(self):
        self.inventory_page.add_first_item_to_cart()

    def click_on_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_button.click()

    def find_element_amount(self):
        cart_amount = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        # Get the text of the element which should be the cart count
        cart_count = cart_amount.text
        return cart_count


# remove item from the cart page not to be confused with remove item from inventory page
    def remove_item(self):
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REMOVE_ITEM)
        )
        remove_button.click()

    def cart_continue_shopping_button(self):
        continue_shopping_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_CART)
        )
        continue_shopping_button.click()


    def checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT)
        )
        checkout_button.click()

    