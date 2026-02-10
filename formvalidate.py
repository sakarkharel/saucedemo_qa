from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

def login():
    text_username = driver.find_element(By.ID, "user-name")
    text_password = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "login-button")
    
    text_username.send_keys("standard_user")
    text_password.send_keys("secret_sauce")
    submit_button.click()
    time.sleep(2)

def homepage():
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

def cart():
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

def checkout_stepone():
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    text_firstname = driver.find_element(By.ID, "first-name")
    text_lastname = driver.find_element(By.ID, "last-name")
    text_postalcode = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    text_firstname.send_keys("Ram")
    text_lastname.send_keys("Bahadur")
    text_postalcode.send_keys("44800")
    
    continue_button.click()
    time.sleep(2)
    # driver.get("https://www.saucedemo.com/checkout-step-one.html")


def validate_checkout_form():
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    time.sleep(2)

    scenarios = [
        {"firstname": "", "lastname": "", "postalcode": "", "description": "All fields are empty"},
        {"firstname": "", "lastname": "Bahadur", "postalcode": "44800", "description": "First name is missing"},
        {"firstname": "Ram", "lastname": "", "postalcode": "44800", "description": "Last name is missing"},
        {"firstname": "Ram", "lastname": "Bahadur", "postalcode": "", "description": "Postal code is missing"},
    ]

    for scenario in scenarios:
        print(f"Running scenario: {scenario['description']}")

        text_firstname = driver.find_element(By.ID, "first-name")
        text_lastname = driver.find_element(By.ID, "last-name")
        text_postalcode = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        
        text_firstname.clear()
        text_lastname.clear()
        text_postalcode.clear()

        
        text_firstname.send_keys(scenario["firstname"])
        text_lastname.send_keys(scenario["lastname"])
        text_postalcode.send_keys(scenario["postalcode"])

        continue_button.click()
        time.sleep(1)

        
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        print("Error message shown:", error_message)

        #error mesage shouldnt be empty, if empty shows like this - no error shown for frist name is empty
        assert error_message != "", f" No error shown for: {scenario['description']}"

        
        driver.get("https://www.saucedemo.com/checkout-step-one.html")
        time.sleep(1)

# def checkout_steptwo():
#     driver.find_element(By.ID, "finish").click()
#     time.sleep(2)

def main():
    login()
    homepage()
    cart()
    checkout_stepone()
    # checkout_steptwo()
    validate_checkout_form()  
    # checkout_steptwo()
    driver.quit()

main()







