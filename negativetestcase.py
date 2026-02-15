#During this negative test case, the website continues to complete the shopping process with no items in the cart 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
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
    time.sleep(10)

def homepage():
    # button_addcartbackpack = driver.find_element(by= By.ID, value ="add-to-cart-sauce-labs-backpack")
    # button_addcartbikelight = driver.find_element(by=By.ID, value = "add-to-cart-sauce-labs-bike-light")

    # button_addcartbackpack.click()
    # button_addcartbikelight.click()
    

    button_cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
    button_cart.click()
    time.sleep(5)

def cart():
    button_checkout = driver.find_element(by=By.ID, value= "checkout")
    button_checkout.click()
    time.sleep(5)

def checkout_stepone():
    text_firstname = driver.find_element(by=By.ID, value = "first-name")
    text_lastname = driver.find_element(by=By.ID, value = "last-name")
    text_postalcode = driver.find_element(by=By.ID, value = "postal-code")
    continue_button = driver.find_element(by=By.ID, value= "continue")

    text_firstname.send_keys("Ram")
    text_lastname.send_keys("Bahadur")
    text_postalcode.send_keys("44800")
    time.sleep(5)
    continue_button.click()
    time.sleep(5)

def checkout_steptwo():
    button_checkouttwo = driver.find_element(by=By.ID, value = "finish")
    button_checkouttwo.click()
    time.sleep(5)


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    title = driver.title
    driver.implicitly_wait(5)


    login()
    homepage()
    cart()
    checkout_stepone()
    checkout_steptwo()
    driver.quit()





if __name__ == "__main__":
    main()
