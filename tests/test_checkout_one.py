import pytest 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.checkout_one_page import CheckoutStepone
import time

@pytest.fixture
def logged_in(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "Login failed or page did not load correctly"
    return InventoryPage(driver)

def test_cancel_button(logged_in, driver):
    inventory_page=logged_in
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == "1"

    #cart clicking 
    cart_page = CartPage(driver)
    cart_page.click_on_cart()
    time.sleep(5)
    assert "cart" in driver.current_url

    #now remving item
    cart_page.checkout()

    # finally cancel button click 

    checkoutone_page = CheckoutStepone(driver)
    checkoutone_page.checkout_stepone_cancelbutton()
    time.sleep(5)
    assert "cart" in driver.current_url



def test_checkout_info_validation(logged_in, driver):
    inventory_page = logged_in
    inventory_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_on_cart()
    cart_page.checkout()

    scenarios = [
        {"firstname": "", "lastname": "", "zipcode": "", "expected": "First Name is required"},
        {"firstname": "", "lastname": "Bahadur", "zipcode": "44800", "expected": "First Name is required"},
        {"firstname": "Ram", "lastname": "", "zipcode": "44800", "expected": "Last Name is required"},
        {"firstname": "Ram", "lastname": "Bahadur", "zipcode": "", "expected": "Postal Code is required"},
    ]

    for scenario in scenarios:
        checkout_page = CheckoutStepone(driver)

 
        checkout_page.checkout_info_firstname(scenario["firstname"])
        checkout_page.checkout_info_lastname(scenario["lastname"])
        checkout_page.checkout_info_zipcode(scenario["zipcode"])

        checkout_page.checkout_info()

        error_message = checkout_page.checkout_error()
        assert scenario["expected"] in error_message

        driver.refresh()

def test_valid_credentials(logged_in, driver):

    inventory_page = logged_in
    inventory_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_on_cart()
    cart_page.checkout()

    checkout_page = CheckoutStepone(driver)
    checkout_page.checkout_info_firstname("John")
    checkout_page.checkout_info_lastname("wick")
    checkout_page.checkout_info_zipcode("11223")
    checkout_page.checkout_info()
    assert "step-two" in driver.current_url


