#checking if cancel button/go back works 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import time 
from selenium.webdriver.support import expected_conditions as EC



def continue_shopping():
    text_username = driver.find_element(by=By.ID,value ="user-name")
    text_password = driver.find_element(by=By.ID, value = "password")
    submit_button = driver.find_element(by=By.ID, value = "login-button")
    
    text_username.send_keys("standard_user")
    text_password.send_keys("secret_sauce")
    submit_button.click()
    time.sleep(2)


    button_addcartbackpack = driver.find_element(by= By.ID, value ="add-to-cart-sauce-labs-backpack")
    button_addcartbikelight = driver.find_element(by=By.ID, value = "add-to-cart-sauce-labs-bike-light")

    button_addcartbackpack.click()
    button_addcartbikelight.click()
    

    button_cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
    button_cart.click()
    time.sleep(2)

    button_continueshopping = driver.find_element(By.ID, "continue-shopping")
    button_continueshopping.click()
    time.sleep(3)

def cancel_checkout_stepone():
    button_cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
    button_cart.click()
    time.sleep(3)


    button_checkout = driver.find_element(by=By.ID, value= "checkout")
    button_checkout.click()
    time.sleep(3)

    button_cancelstepone = driver.find_element(By.ID, "cancel")
    button_cancelstepone.click()
    time.sleep(3)

def cancel_checkout_steptwo():

    button_checkout = driver.find_element(by=By.ID, value= "checkout")
    button_checkout.click()
    time.sleep(3)


    text_firstname = driver.find_element(by=By.ID, value = "first-name")
    text_lastname = driver.find_element(by=By.ID, value = "last-name")
    text_postalcode = driver.find_element(by=By.ID, value = "postal-code")
    continue_button = driver.find_element(by=By.ID, value= "continue")

    text_firstname.send_keys("Ram")
    text_lastname.send_keys("Bahadur")
    text_postalcode.send_keys("44800")
    time.sleep(3)
    continue_button.click()
    time.sleep(3)

    button_cancelsteptwo = driver.find_element(by=By.ID, value = "cancel")
    button_cancelsteptwo.click()
    time.sleep(2)




def main():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    title = driver.title
    driver.implicitly_wait(5)
    continue_shopping()
    cancel_checkout_stepone()
    cancel_checkout_steptwo()
    driver.quit()


if __name__ == "__main__":
    main()