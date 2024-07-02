import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.base_page_locators import BasePageLocators

class PersonalAccount(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("клик по кнопке войти в аккаунт")
    def click_enter_account_button(self):
        self.wait_and_click_element(BasePageLocators.enter_account_button)

    @allure.step("клик по кнопке личный кабинет")
    def click_personal_account_button(self):
        self.wait_and_click_element(BasePageLocators.personal_account_button)

    @allure.step("ввод данных в поле email")
    def enter_email_fild(self, email):
        self.enter_text_to_field(BasePageLocators.EMAIL_FIELD, email)

    @allure.step("ввод данных в поле password")
    def enter_password_fild(self, password):
        self.enter_text_to_field(BasePageLocators.PASSWORD_FIELD, password)

    @allure.step("клик по кнопке войти")
    def click_login_button(self):
        self.wait_and_click_element(BasePageLocators.BUTTON_ENTRANCE)

    @allure.step("ожидание кнопки профиль")
    def wait_profile_button(self):
        self.wait_element(PersonalAccountLocators.PROFILE_BUTTON)

    @allure.step("клик по кнопке история заказов")
    def click_order_history_button(self):
        self.wait_and_click_element(BasePageLocators.history_orders_button)

    @allure.step("клик по кнопке выход")
    def click_exit_button(self):
        self.wait_and_click_element(PersonalAccountLocators.exit_button)

    @allure.step("Ожидание кнопки войти")
    def wait_login_button(self):
        self.wait_element(BasePageLocators.BUTTON_ENTRANCE)