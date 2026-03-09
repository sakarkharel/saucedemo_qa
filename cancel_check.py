from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )


def login(driver):
    wait_for(driver, By.ID, "user-name").send_keys(USERNAME)
    wait_for(driver, By.ID, "password").send_keys(PASSWORD)
    wait_for(driver, By.ID, "login-button").click()


def add_products(driver):
    wait_for(driver, By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait_for(driver, By.ID, "add-to-cart-sauce-labs-bike-light").click()


def open_cart(driver):
    wait_for(driver, By.CLASS_NAME, "shopping_cart_link").click()


def continue_shopping(driver):
    open_cart(driver)
    wait_for(driver, By.ID, "continue-shopping").click()


def cancel_checkout_stepone(driver):
    open_cart(driver)

    wait_for(driver, By.ID, "checkout").click()
    wait_for(driver, By.ID, "cancel").click()


def cancel_checkout_steptwo(driver):
    open_cart(driver)

    wait_for(driver, By.ID, "checkout").click()

    wait_for(driver, By.ID, "first-name").send_keys("Ram")
    wait_for(driver, By.ID, "last-name").send_keys("Bahadur")
    wait_for(driver, By.ID, "postal-code").send_keys("44800")

    wait_for(driver, By.ID, "continue").click()

    wait_for(driver, By.ID, "cancel").click()


def main():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        login(driver)
        add_products(driver)

        continue_shopping(driver)
        cancel_checkout_stepone(driver)
        cancel_checkout_steptwo(driver)

        print("Cancel and Continue Shopping tests completed successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()