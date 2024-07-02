from pages.home_page import HomePage
import allure
from config import URL, url_order_feed
from helpers import registration_user, delete_user

class TestHomePage:

    @allure.title("переход по клику на «Конструктор»")
    def test_click_designer_button(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_order_feed()
        home_page.click_designer_button()
        home_page.wait_make_burger_text()
        assert home_page.get_current_url() == URL

    @allure.title("переход по клику на «Лента заказов»")
    def test_click_order_feed(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_order_feed()
        home_page.wait_order_feed()
        assert home_page.get_current_url() == url_order_feed

    @allure.title("клик на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_pop_ap_window(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_souces_spicy()
        assert home_page.wait_pop_up_window().is_displayed()

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_ingredient_pop_ap_window_closes(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_souces_spicy()
        home_page.wait_pop_up_window()
        home_page.click_cross_pop_au_window()
        assert home_page.wait_pop_up_window_disappear()

    @allure.title("при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_counter_increases_adding_ingredient(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.drag_buns_in_order()
        assert home_page.wait_counter_increases_ingredients().is_displayed()

    @allure.title("залогиненный пользователь может оформить заказ")
    def test_iogin_user_add_order(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        home_page = HomePage(web_driver)
        home_page.click_enter_account_button()
        home_page.enter_email_fild(email)
        home_page.enter_password_fild(password)
        home_page.click_login_button()
        home_page.drag_buns_in_order()
        home_page.drag_sauces_in_order()
        home_page.drag_filling_in_order()
        home_page.click_checkout_button()
        assert home_page.wait_pop_up_window_order_prepared().is_displayed()
        delete_user(access_token)

    @allure.title("клик на заказ, откроется всплывающее окно с деталями")
    def test_pop_up_window_order_details(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_order_feed()
        home_page.click_order()
        assert home_page.wait_pop_up_window_order_details().is_displayed()

    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_in_order_feed(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        home_page = HomePage(web_driver)
        home_page.click_enter_account_button()
        home_page.enter_email_fild(email)
        home_page.enter_password_fild(password)
        home_page.click_login_button()
        home_page.drag_buns_in_order()
        home_page.drag_sauces_in_order()
        home_page.drag_filling_in_order()
        home_page.click_checkout_button()
        home_page.click_closes_order_number_button()
        home_page.click_personal_account_button()
        home_page.click_order_history_button()
        order_history = home_page.getting_order_history()
        home_page.click_order_feed()
        order_feed = home_page.getting_order_feed()
        order_history_ids = [order.split('\n')[0] for order in order_history]
        order_feed_ids = [order.split('\n')[0] for order in order_feed]
        for order_id in order_history_ids:
            assert order_id in order_feed_ids
        delete_user(access_token)

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_order_in_order_feed(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        home_page = HomePage(web_driver)
        home_page.click_enter_account_button()
        home_page.enter_email_fild(email)
        home_page.enter_password_fild(password)
        home_page.click_login_button()
        home_page.drag_buns_in_order()
        home_page.drag_sauces_in_order()
        home_page.drag_filling_in_order()
        home_page.click_checkout_button()
        home_page.click_closes_order_number_button()
        home_page.click_personal_account_button()
        home_page.click_order_history_button()
        order_history = home_page.getting_order_history()
        home_page.click_order_feed()
        order_work = home_page.getting_order_at_work()
        order_history_ids = [order.split('\n')[0].lstrip('#') for order in order_history]
        order_feed_ids = [order.split('\n')[0] for order in order_work]
        for order_id in order_history_ids:
            assert order_id in order_feed_ids
        delete_user(access_token)

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increases_counter_total_orders(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        home_page = HomePage(web_driver)
        home_page.click_enter_account_button()
        home_page.enter_email_fild(email)
        home_page.enter_password_fild(password)
        home_page.click_login_button()
        home_page.click_order_feed()
        total_number = home_page.get_total_orders_number()
        home_page.click_designer_button()
        home_page.drag_buns_in_order()
        home_page.drag_sauces_in_order()
        home_page.drag_filling_in_order()
        home_page.click_checkout_button()
        home_page.click_closes_order_number_button()
        home_page.click_order_invisible_feed()
        new_total_number = home_page.get_total_orders_number()
        assert total_number < new_total_number
        delete_user(access_token)

    @allure.title('При создании нового заказа счётчик Выполнено за день увеличивается')
    def test_increases_counter_total_orders(self, web_driver):
        data = registration_user()
        email = data[1]
        password = data[2]
        access_token = data[0]
        home_page = HomePage(web_driver)
        home_page.click_enter_account_button()
        home_page.enter_email_fild(email)
        home_page.enter_password_fild(password)
        home_page.click_login_button()
        home_page.click_order_feed()
        today_number = home_page.get_today_orders_number()
        home_page.click_designer_button()
        home_page.drag_buns_in_order()
        home_page.drag_sauces_in_order()
        home_page.drag_filling_in_order()
        home_page.click_checkout_button()
        home_page.click_closes_order_number_button()
        home_page.click_order_invisible_feed()
        new_today_number = home_page.get_today_orders_number()
        assert today_number < new_today_number
        delete_user(access_token)


















