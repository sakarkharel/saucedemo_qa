from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 


def sql_injection(driver):
    text_username = driver.find_element(by=By.ID, value="user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys("' OR '1'='1")
    text_password.send_keys("anything")
    submit_button.click()
    time.sleep(3)


def special_char(driver):
    driver.get("https://www.saucedemo.com/")
    text_username = driver.find_element(by=By.ID, value = "user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys("!@#$%^&*()")
    text_password.send_keys("!@#$%^&*()")
    submit_button.click()
    time.sleep(3)

def case_sensitive(driver):
    driver.get("https://www.saucedemo.com/")
    text_username = driver.find_element(by=By.ID, value = "user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys("STANDARD_USER")
    text_password.send_keys("SECRET_SAUCE")
    submit_button.click()
    time.sleep(3)

def lead_trail_space(driver):
    driver.get("https://www.saucedemo.com/")
    text_username = driver.find_element(by=By.ID, value = "user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys(" standard_user ")
    text_password.send_keys(" secret_sauce ")
    submit_button.click()
    time.sleep(3)

def long_input(driver, long_username,long_password ):
    driver.get("https://www.saucedemo.com/")
    text_username = driver.find_element(by=By.ID, value = "user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys(long_username)
    text_password.send_keys(long_password)
    submit_button.click()
    time.sleep(3)

#refreshing page after entering credentials 
def refresh(driver):
    driver.get("https://www.saucedemo.com/")
    text_username = driver.find_element(by=By.ID, value = "user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")

    text_username.send_keys("standard_user")
    text_password.send_keys("secret_sauce")
    driver.refresh()
    time.sleep(3)
    submit_button.click()


def main ():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    title = driver.title
    driver.implicitly_wait(5)
    long_username = "a" * 1000
    long_password = "b" * 1000
    sql_injection(driver)
    special_char(driver)
    case_sensitive(driver)
    lead_trail_space(driver)
    long_input(driver, long_username, long_password)
    refresh(driver)




if __name__ == "__main__":
    main()
