from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
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


def filter_hilo(driver):
    dropdown = Select(wait_for(driver, By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Price (high to low)")


def filter_lohi(driver):
    dropdown = Select(wait_for(driver, By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Price (low to high)")


def filter_za(driver):
    dropdown = Select(wait_for(driver, By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Name (Z to A)")


def media_links(driver):
    wait_for(driver, By.CLASS_NAME, "social_twitter").click()
    wait_for(driver, By.CLASS_NAME, "social_facebook").click()
    wait_for(driver, By.CLASS_NAME, "social_linkedin").click()


def test_about_button(driver):
    wait_for(driver, By.CLASS_NAME, "bm-burger-button").click()
    wait_for(driver, By.ID, "about_sidebar_link").click()

    driver.get("https://www.saucedemo.com/inventory.html")


def test_logout_button(driver):
    wait_for(driver, By.CLASS_NAME, "bm-burger-button").click()
    wait_for(driver, By.ID, "logout_sidebar_link").click()


def main():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        login(driver)
        filter_hilo(driver)
        filter_lohi(driver)
        filter_za(driver)
        media_links(driver)
        test_about_button(driver)
        test_logout_button(driver)

        print("Test completed successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()