from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class InventoryPage:

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[starts-with(@id, 'remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    #for data of items 

    def get_product_names(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [e.text for e in elements] # returning the names of all items 
    
    def get_product_prices(self):
        elements = WebDriverWait(self.driver,10).until(
            EC.visibility_of_all_elements_located(self.PRODUCT_PRICES)
        )
        return [e.text for e in elements]
    
    
    # Doing actions in cart 
    def add_first_item_to_cart(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTONS)
        )
        buttons.click()

    # def add_item_by_index(self, index):
    #     buttons = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_all_elements_located(self.ADD_TO_CART_BUTTONS)
    #     )
    #     buttons[index].click()
    
    def remove_first_item(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REMOVE_BUTTONS)
        )
        buttons.click()
    
    def get_cart_count(self):
        try:
            badge=self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return badge.text
        except TimeoutException:
            return "0"

       #sorting the products based on prices and alphabets  
    def sort_products(self, option_value):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SORT_DROPDOWN)
        )
        dropdown.click()
        dropdown.find_element(By.XPATH, f".//option[@value='{option_value}']").click()


    # # Navigation (moving to another page)
    # def go_to_cart(self):
    #     self.driver.find_element(*self.CART_ICON).click()

    # # sorting the products based on prices and alphabets 
    # def sort_products(self, option_value):
    #     dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
    #     dropdown.click()
    #     dropdown.find_element(By.XPATH, f"//option[@value='{option_value}']").click()

    # #UI
    # def open_menu(self):
    #     self.driver.find_element(*self.MENU_BUTTON).click()

    