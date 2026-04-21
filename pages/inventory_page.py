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
    TWITTER = (By.CLASS_NAME, "social_twitter")
    FACEBOOK = (By.CLASS_NAME, "social_facebook")
    LINKEDIN = (By.CLASS_NAME, "social_linkedin")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")


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

    # naviagtes to social media pages 
    # repeating scroll + click logic per method to ensure stable element interaction
    def click_twitter(self):
        twitter_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TWITTER)
        )
        self.driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        twitter_element
        )
        twitter_element.click()
        # add exception handling here :


    def click_facebook(self):
        facebook_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FACEBOOK)
        )
        self.driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        facebook_element
        )
        facebook_element.click()

    def click_linkedin(self):
        linkedin_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINKEDIN)
        )
        self.driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        linkedin_element
        )
        linkedin_element.click()

    # methods for burger button

    def about_button(self):
        burger_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        burger_element.click()
        about_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ABOUT)
        )
        about_element.click()


    def logout_button(self):
        burger_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        burger_element.click()
        logout_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT)
        )
        logout_element.click()

        

    

    





