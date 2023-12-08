from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON_HOME = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')


    PERSONAL_CABINET_LINK = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
    CONSTRUCTOR_LINK = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')


    BULKI_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]')
    SOUSI_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    NACHINKI_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
