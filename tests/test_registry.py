import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def is_valid_email(email):
    # Regular expression to check the email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def test_successful_registration(driver):
    try:
        driver.get("https://stellarburgers.nomoreparties.site/login")

        registration_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a'))
        )
        registration_button.click()

        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys("Marina Orangkhadivi")

        email_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        email = "marinaorangkhadivi3111@test.te"
        email_input.send_keys(email)

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password = "123456"
        password_input.send_keys(password)

        if not is_valid_email(email):
            print("Error: Invalid email format.")
            return

        if len(password) < 6:
            print("Error: Password must be at least 6 characters long.")
            return

        registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        registration_button.click()

        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'))).text
        assert text == 'Соберите бургер'

    except (NoSuchElementException, TimeoutException) as e:
        print("An error occurred:", e)

    finally:
        driver.quit()
