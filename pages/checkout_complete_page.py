from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_complete_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def get_complete_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_TEXT)
        ).text

    def click_back_home(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()