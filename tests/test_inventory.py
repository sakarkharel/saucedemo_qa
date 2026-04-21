import pytest 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time
@pytest.fixture
def logged_in(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "Login failed or page did not load correctly"
    return InventoryPage(driver)

#data of tiems 

def test_products_are_displayed(logged_in):
    names = logged_in.get_product_names()
    prices = logged_in.get_product_prices()

    assert len(names)>0
    assert len(prices)>0

#doing actions in cart part 
def test_add_to_cart_updates_badge(logged_in):
    logged_in.add_first_item_to_cart()
    assert logged_in.get_cart_count() == "1"

def test_remove_from_cart(logged_in):
    logged_in.add_first_item_to_cart()
    logged_in.remove_first_item()
    # assert logged_in.get_cart_count() == "0"

    logged_in.wait.until(
        lambda d: logged_in.get_cart_count() == "0"
    )

    assert logged_in.get_cart_count() == "0"

# sorting theproducts based on prices and alphabets 
def test_sort_low_to_high(logged_in):
    logged_in.sort_products("lohi")
    prices = logged_in.get_product_prices()
    prices = [float(p.replace("$", "")) for p in prices]
    assert prices == sorted(prices)

def test_sort_high_to_low(logged_in):
    logged_in.sort_products("hilo")
    prices = logged_in.get_product_prices()
    prices = [float(p.replace("$", "")) for p in prices]
    assert prices == sorted(prices, reverse=True)

def test_sort_a_to_z(logged_in):
    logged_in.sort_products("az")
    names = logged_in.get_product_names()
    assert names == sorted(names)

def test_sort_z_to_a(logged_in):
    logged_in.sort_products("za")
    names = logged_in.get_product_names()
    assert names == sorted(names, reverse=True)

def test_twitter(logged_in, driver):
    logged_in.click_twitter()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert "x.com" in driver.current_url

def test_facebook(logged_in, driver):
    logged_in.click_facebook()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert "facebook.com" in driver.current_url