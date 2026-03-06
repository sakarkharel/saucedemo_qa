from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


def open_page(driver):
    driver.get(URL)


def login(driver, username, password):
    wait = WebDriverWait(driver, 10)

    username_box = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password_box = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_box.clear()
    password_box.clear()

    username_box.send_keys(username)
    password_box.send_keys(password)
    login_button.click()


def sql_injection(driver):
    open_page(driver)
    login(driver, "' OR '1'='1", "anything")


def special_char(driver):
    open_page(driver)
    login(driver, "!@#$%^&*()", "!@#$%^&*()")


def case_sensitive(driver):
    open_page(driver)
    login(driver, "STANDARD_USER", "SECRET_SAUCE")


def lead_trail_space(driver):
    open_page(driver)
    login(driver, " standard_user ", " secret_sauce ")


def long_input(driver):
    open_page(driver)
    long_username = "a" * 1000
    long_password = "b" * 1000
    login(driver, long_username, long_password)


def refresh_test(driver):
    open_page(driver)

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    driver.refresh()

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()


def rapid_click(driver):
    open_page(driver)
    login(driver, "standard_user", "secret_sauce")

    for _ in range(5):
        driver.find_element(By.ID, "login-button").click()


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        sql_injection(driver)
        special_char(driver)
        case_sensitive(driver)
        lead_trail_space(driver)
        long_input(driver)
        refresh_test(driver)
        rapid_click(driver)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()