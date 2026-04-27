import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_one_page import CheckoutStepone
from pages.checkout_two_page import CheckoutSteptwo
from pages.checkout_complete_page import CheckoutCompletePage


@pytest.fixture
def logged_in(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    return InventoryPage(driver)


def go_to_checkout_complete(driver, inventory_page):
    inventory_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_on_cart()

    cart_page.checkout()

    checkout_one = CheckoutStepone(driver)
    checkout_one.checkout_info_firstname("John")
    checkout_one.checkout_info_lastname("Wick")
    checkout_one.checkout_info_zipcode("11223")
    checkout_one.checkout_info()

    checkout_two = CheckoutSteptwo(driver)
    checkout_two.checkout_steptwo_finishbutton()


def test_checkout_complete_page_display(logged_in, driver):
    go_to_checkout_complete(driver, logged_in)

    complete_page = CheckoutCompletePage(driver)

    assert "checkout-complete" in driver.current_url
    assert "Thank you for your order!" in complete_page.get_complete_header()


def test_checkout_complete_text(logged_in, driver):
    go_to_checkout_complete(driver, logged_in)

    complete_page = CheckoutCompletePage(driver)

    assert "Your order has been dispatched" in complete_page.get_complete_text()


def test_back_home_button(logged_in, driver):
    go_to_checkout_complete(driver, logged_in)

    complete_page = CheckoutCompletePage(driver)
    complete_page.click_back_home()

    assert "inventory" in driver.current_url