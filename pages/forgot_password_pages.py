from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage
from data import email, password
import allure



class ForgotPassword(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
    @allure.step("Клик по кнопке войти в аккаунт")
    def click_login_button(self):
        self.wait_and_click_element(ForgotPasswordLocators.login_to_account_button)

    @allure.step("Клик по кнопке Восстановить пароль")
    def click_forgot_password_button(self):
        self.wait_and_click_element(ForgotPasswordLocators.forgot_password_button)

    @allure.step("ввод почты восстановление пароля")
    def enter_email_recovery(self):
        self.enter_text_to_field(ForgotPasswordLocators.email_field_forgot_password, email)

    @allure.step("клик по кнопке восстановить")
    def click_recovery_button(self):
        self.click_element(ForgotPasswordLocators.forgot_button)

    @allure.step("ожидание появления поля ввода пароль")
    def wait_password_field_forgot(self):
        self.wait_element(ForgotPasswordLocators.password_field_forgot)


    @allure.step("ввод текста в поле восстановление пароля")
    def enter_text_to_field_recovery_password(self):
        self.enter_text_to_field(ForgotPasswordLocators.password_field_forgot, password)

    @allure.step("клик по кнопке показать/скрыть пароль")
    def click_show_button(self):
        self.wait_and_click_element(ForgotPasswordLocators.show_button)

    @allure.step("ожидание активного окна пароль")
    def wait_active_field_password(self):
        return self.wait_element(ForgotPasswordLocators.active_field_password)








