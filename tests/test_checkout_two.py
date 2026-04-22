import pytest 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.checkout_one_page import CheckoutStepone
from pages.checkout_two_page import CheckoutSteptwo
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
    checkoutone_page.checkout_info_firstname("John")
    checkoutone_page.checkout_info_lastname("wick")
    checkoutone_page.checkout_info_zipcode("11223")
    checkoutone_page.checkout_info()
    assert "step-two" in driver.current_url
    
    time.sleep(5)
    checkouttwo_page = CheckoutSteptwo(driver)
    checkouttwo_page.checkout_steptwo_cancelbutton()
    assert "inventory" in driver.current_url

def test_finish_button(logged_in, driver):
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
    checkoutone_page.checkout_info_firstname("John")
    checkoutone_page.checkout_info_lastname("wick")
    checkoutone_page.checkout_info_zipcode("11223")
    checkoutone_page.checkout_info()
    assert "step-two" in driver.current_url
    
    time.sleep(5)
    checkouttwo_page = CheckoutSteptwo(driver)
    checkouttwo_page.checkout_steptwo_finishbutton()
    assert "checkout-complete" in driver.current_url





