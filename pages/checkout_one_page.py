from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from pages.inventory_page import InventoryPage


class CheckoutStepone:
    CANCEL_BUTTON = (By.ID, "cancel")
    CHECKOUT_BUTTON = (By.ID, "continue")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.inventory_page = InventoryPage(driver)
    

    def checkout_stepone_cancelbutton(self):
        cancel_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        )
        cancel_button.click()

    def checkout_info_firstname(self, firstname):
        info_firstname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_NAME)
        )
        info_firstname.clear()
        info_firstname.send_keys(firstname)

    
    def checkout_info_lastname(self, lastname):
        info_lastname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )
        info_lastname.clear()
        info_lastname.send_keys(lastname)


    def checkout_info_zipcode(self, zipcode):
        info_zipcode = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ZIP_CODE)
        )
        info_zipcode.clear()
        info_zipcode.send_keys(zipcode)

    def checkout_error(self):
        error_element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error_element.text

    
    def checkout_info(self):
        checkout_info_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_info_button.click()
    
