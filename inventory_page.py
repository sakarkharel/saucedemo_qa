from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import time 
from selenium.webdriver.support import expected_conditions as EC



def login(driver):
    text_username = driver.find_element(by=By.ID,value ="user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")
    
    text_username.send_keys("standard_user")
    text_password.send_keys("secret_sauce")
    submit_button.click()
    time.sleep(3)


def filter_hilo(driver):
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (high to low)")
    time.sleep(3)

def filter_lohi(driver):
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")
    time.sleep(3)

def filter_za(driver):
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (Z to A)")
    time.sleep(3)

def media_link(driver):
    link_twitter = driver.find_element(by=By.CLASS_NAME, value = "social_twitter")
    link_twitter.click()
    time.sleep(3)
    
    link_facebook = driver.find_element(by=By.CLASS_NAME, value = "social_facebook")
    link_facebook.click()
    time.sleep(3)

    link_linkedin = driver.find_element(by=By.CLASS_NAME, value = "social_linkedin")
    link_linkedin.click()
    time.sleep(3)


def test_about_button(driver):
    burgerbutton = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burgerbutton.click()

    about = driver.find_element(By.ID, "about_sidebar_link")
    about.click()
    time.sleep(2)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    

def test_logout_button(driver):
    burgerbutton = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burgerbutton.click()

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    time.sleep(3)


def main():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    title = driver.title
    driver.implicitly_wait(5)
    login(driver)
    filter_hilo(driver)
    filter_lohi(driver)
    filter_za(driver)
    media_link(driver)
    test_about_button(driver)
    test_logout_button(driver)


if __name__ == '__main__':
    main()