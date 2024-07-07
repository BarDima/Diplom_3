from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    forgot_password_button = (By.XPATH, "*//a[@href='/forgot-password']")  # кнопка восстановление пароля
    email_field_forgot_password = (By.XPATH, "*//input[@class='text input__textfield text_type_main-default']")  # поле email восстановление пароля
    forgot_button = (By.XPATH, "*//button[text()='Восстановить']")# кнопка восстановить
    login_to_account_button = (By.XPATH, "*//button[text()='Войти в аккаунт']")# кнопка войти в аккаунт
    password_field_forgot = (By.XPATH, "*//input[ @ name = 'Введите новый пароль']")#поле ввода нового пароля
    show_button = (By.XPATH, "*//div[@class='input__icon input__icon-action']")#кнопка показать пароль
    active_field_password = (By.XPATH, "*//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")#активное поле пароль