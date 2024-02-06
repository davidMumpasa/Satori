from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

try:
    # Navigate to the URL
    driver.get("http://localhost:3000")

    # Wait for the page to load
    time.sleep(2)

    # Find the register button and click it
    registerBtn = driver.find_element("css selector", "#root > div > div > div > div.col-lg-6.align-self-center > div > a.btn.btn-border-base.ml-4.aos-init.aos-animate")
    registerBtn.click()

    # Wait for the registration form to appear
    time.sleep(2)

    # Find the email input field and enter an email address
    emailInput = driver.find_element("css selector", "#form1")
    emailInput.send_keys("test@example.com")

    # Wait for a moment
    time.sleep(1)

    # Find the password input field and enter a password
    passwordInput = driver.find_element("css selector", "#form2")
    passwordInput.send_keys("your_password")

    # Wait for a moment
    time.sleep(1)

    # # Find the confirm password input field using XPath and enter the same password
    # confirmPasswordInput = driver.find_element("xpath", '//*[@id="form3"]')
    # confirmPasswordInput.send_keys("your_password")

    # # Wait for a moment
    # time.sleep(1)

    # Find the terms and conditions checkbox and click it
    termAndConCheckBox = driver.find_element("css selector", "#flexCheckDefault")
    termAndConCheckBox.click()

    # Wait for a moment
    time.sleep(1)

    # Find the sign-up button and click it
    signUpBtn = driver.find_element("css selector", "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")
    signUpBtn.click()

    # Wait for a few seconds to see the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
