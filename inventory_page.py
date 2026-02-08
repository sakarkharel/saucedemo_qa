from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import time 
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
title = driver.title
driver.implicitly_wait(5)

def login():
    text_username = driver.find_element(by=By.ID,value ="user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")
    
    text_username.send_keys("standard_user")
    text_password.send_keys("secret_sauce")
    submit_button.click()
    time.sleep(5)


def filter_hilo():
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (high to low)")
    time.sleep(5)

def filter_lohi():
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")
    time.sleep(5)

def filter_za():
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (Z to A)")
    time.sleep(5)

def media_link():
    link_twitter = driver.find_element(by=By.CLASS_NAME, value = "social_twitter")
    link_twitter.click()
    time.sleep(5)
    
    link_facebook = driver.find_element(by=By.CLASS_NAME, value = "social_facebook")
    link_facebook.click()
    time.sleep(5)

    link_linkedin = driver.find_element(by=By.CLASS_NAME, value = "social_linkedin")
    link_linkedin.click()
    time.sleep(5)


def test_about_button():
    burgerbutton = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burgerbutton.click()

    about = driver.find_element(By.ID, "about_sidebar_link")
    about.click()
    time.sleep(5)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(5)
    

def test_logout_button():
    burgerbutton = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burgerbutton.click()

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    time.sleep(5)


def main():
    login()
    filter_hilo()
    filter_lohi()
    filter_za()
    media_link()
    test_about_button()
    test_logout_button()


main()