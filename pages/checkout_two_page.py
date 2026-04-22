from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from pages.inventory_page import InventoryPage
from pages.checkout_one_page import CheckoutStepone


class CheckoutSteptwo:
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH__BUTTON = (By.ID, "finish")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.inventory_page = InventoryPage(driver)


    def checkout_steptwo_cancelbutton(self):
        cancel_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        )
        cancel_button.click()

    def checkout_steptwo_finishbutton(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH__BUTTON)
        )
        finish_button.click()

    

