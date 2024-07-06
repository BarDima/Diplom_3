import allure
from pages.forgot_password_pages import ForgotPassword
from config import url_password_recovery, url_reset_password


class TestForgotPasswordPage:

    @allure.title("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_password_recovery_button(self, web_driver):
        forgot_password = ForgotPassword(web_driver)
        forgot_password.click_enter_account_button()
        forgot_password.click_forgot_password_button()
        assert forgot_password.get_current_url() == url_password_recovery

    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_recovery(self, web_driver):
        forgot_password = ForgotPassword(web_driver)
        forgot_password.click_enter_account_button()
        forgot_password.click_forgot_password_button()
        forgot_password.enter_email_recovery()
        forgot_password.click_recovery_button()
        forgot_password.wait_password_field_forgot()
        assert forgot_password.get_current_url() == url_reset_password

    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_show_password_button(self, web_driver):
        forgot_password = ForgotPassword(web_driver)
        forgot_password.click_enter_account_button()
        forgot_password.click_forgot_password_button()
        forgot_password.enter_email_recovery()
        forgot_password.click_recovery_button()
        forgot_password.enter_text_to_field_recovery_password()
        forgot_password.click_show_button()
        active_filed = forgot_password.wait_active_field_password()
        assert active_filed.is_displayed()



