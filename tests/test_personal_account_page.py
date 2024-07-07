from pages.personal_account_page import PersonalAccount
from helpers import registration_user, delete_user
import allure
from config import url_personal_account, url_order_history, url_login


class TestPersonalAccountPage:

    @allure.title("переход по клику на «Личный кабинет»")
    def test_click_personal_account_button(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        personal_account = PersonalAccount(web_driver)
        personal_account.click_enter_account_button()
        personal_account.enter_email_fild(email)
        personal_account.enter_password_fild(password)
        personal_account.click_login_button()
        personal_account.click_personal_account_button()
        personal_account.wait_profile_button()
        assert personal_account.get_current_url() == url_personal_account
        delete_user(access_token)

    @allure.title('переход в раздел «История заказов»')
    def test_transition_order_history(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        personal_account = PersonalAccount(web_driver)
        personal_account.click_enter_account_button()
        personal_account.enter_email_fild(email)
        personal_account.enter_password_fild(password)
        personal_account.click_login_button()
        personal_account.click_personal_account_button()
        personal_account.click_order_history_button()
        assert personal_account.get_current_url() == url_order_history
        delete_user(access_token)

    @allure.title('выход из аккаунта')
    def test_exit_button(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        personal_account = PersonalAccount(web_driver)
        personal_account.click_enter_account_button()
        personal_account.enter_email_fild(email)
        personal_account.enter_password_fild(password)
        personal_account.click_login_button()
        personal_account.click_personal_account_button()
        personal_account.click_exit_button()
        personal_account.wait_login_button()
        assert personal_account.get_current_url() == url_login
        delete_user(access_token)



