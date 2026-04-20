from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.open(self.URL)
        self.wait_for_login_page()

    def wait_for_login_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.username_input)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.login_button)
        )

    def login(self, username, password):
        self.wait_for_login_page()

        user = self.driver.find_element(*self.username_input)
        pwd = self.driver.find_element(*self.password_input)
        btn = self.driver.find_element(*self.login_button)

        user.clear()
        user.send_keys(username)

        pwd.clear()
        pwd.send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def wait_for_inventory(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains("inventory")
        )

    def get_url(self):
        return self.driver.current_url

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text