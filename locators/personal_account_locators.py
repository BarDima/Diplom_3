from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PROFILE_BUTTON = (By.XPATH, "*//a[@href='/account/profile']")#кнопка профиль
    exit_button = (By.XPATH, "*//button[text()='Выход']")#кнопка выход
