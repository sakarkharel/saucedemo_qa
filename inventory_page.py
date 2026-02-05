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
    

#chalena hyaa 
def filter():
   filter = driver.find_element(by=By.CLASS_NAME, value = "product_sort_container")
   filter.click()



def main():
    login()
    filter()


main()