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

#chalena hyaa 


    # sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    # sort_dropdown.select_by_visible_text("Name(Z to A)")
    # time.sleep(5)


    # sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    # sort_dropdown.select_by_visible_text("Price(low to high)")
    # time.sleep(5)

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


def main():
    login()
    filter_hilo()
    filter_lohi()
    filter_za()


main()