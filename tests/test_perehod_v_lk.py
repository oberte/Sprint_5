import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_successful_login(driver, user_credentials):
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button_home = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'))
        )
        login_button_home.click()

        email = user_credentials['email']
        password = user_credentials['password']

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'))
        )
        email_input.send_keys(email)

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        login_button.click()

        text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'))).text
        assert text == 'Соберите бургер'

    except (NoSuchElementException, TimeoutException) as e:
        print("Произошла ошибка:", e)

    finally:
        driver.quit()
