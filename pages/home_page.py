import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators

class HomePage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("клик по кнопке лента заказов")
    def click_order_feed(self):
        self.wait_and_click_element(HomePageLocators.order_feed)

    @allure.step("ожидание загрузки страницы лента заказов")
    def wait_order_feed(self):
        self.wait_element(HomePageLocators.order_feed_text)

    @allure.step("клик по кнопке конструктор")
    def click_designer_button(self):
        self.wait_and_click_element(HomePageLocators.DESIGNER_BUTTON)

    @allure.step("ожидание загрузки раздела конструктор")
    def wait_make_burger_text(self):
        self.wait_element(HomePageLocators.MAKE_BURGER_TEXT)

    @allure.step("клик по кнопке соусы")
    def click_sauces_button(self):
        self.wait_and_click_element(HomePageLocators.SAUCES_BUTTON)

    @allure.step("клик по кнопке соус Spicy-x")
    def click_souces_spicy(self):
        self.wait_and_click_element(HomePageLocators.sauces_spicy)

    @allure.step('загрузка всплывающего окна с деталями ингредиентов соуса spicy-X')
    def wait_pop_up_window(self):
        return self.wait_element(HomePageLocators.pop_up_window)

    @allure.step('закрытие всплывающего окна с деталями ингредиентов соуса spicy-X')
    def wait_pop_up_window_disappear(self):
        return self.wait_disappear_element(HomePageLocators.pop_up_window)

    @allure.step('клик по крестику всплывающего окна с деталями ингредиентов соуса spicy-X')
    def click_cross_pop_au_window(self):
        self.wait_and_click_element(HomePageLocators.closes_pop_up_window)

    @allure.step('добавляем ингредиент Флюоресцентная булка R2-D3 в заказ')
    def drag_buns_in_order(self):
        self.drag_and_drop_element(HomePageLocators.buns_r2_d3, HomePageLocators.place_of_relocation)

    @allure.step('изменения счетчика ингредиента булки после добавления в заказ')
    def wait_counter_increases_ingredients(self):
        return self.wait_element(HomePageLocators.counter_increases)

    @allure.step("клик по кнопке войти в аккаунт")
    def click_enter_account_button(self):
        self.wait_and_click_element(BasePageLocators.enter_account_button)

    @allure.step("ввод данных в поле email")
    def enter_email_fild(self, email):
        self.enter_text_to_field(BasePageLocators.EMAIL_FIELD, email)

    @allure.step("ввод данных в поле password")
    def enter_password_fild(self, password):
        self.enter_text_to_field(BasePageLocators.PASSWORD_FIELD, password)

    @allure.step("клик по кнопке войти")
    def click_login_button(self):
        self.wait_and_click_element(BasePageLocators.BUTTON_ENTRANCE)


    @allure.step("клик по кнопке начинки")
    def click_fillings_button(self):
        self.wait_and_click_element(HomePageLocators.SECTION_FILLINGS)

    @allure.step('добавляем ингредиент Соус Spicy-X в заказ')
    def drag_sauces_in_order(self):
        self.drag_and_drop_element(HomePageLocators.sauces_spicy, HomePageLocators.place_of_relocation)

    @allure.step('добавляем ингредиент начинка Говяжий метеорит (отбивная)')
    def drag_filling_in_order(self):
        self.drag_and_drop_element(HomePageLocators.filling, HomePageLocators.place_of_relocation)

    @allure.step("клик по кнопке оформить заказ")
    def click_checkout_button(self):
        self.wait_and_click_element(HomePageLocators.checkout_button)

    @allure.step('загрузка всплывающего окна ваш заказ готовится')
    def wait_pop_up_window_order_prepared(self):
        return self.wait_element(HomePageLocators.pop_up_window_order_prepared)

    @allure.step('получение номера заказа')
    def receiving_order_number(self):
        return self.wait_element_return_text(HomePageLocators.pop_up_window_number_order)

    @allure.step('клик по кнопке закрытия всплывающего окна с номером заказа')
    def click_closes_order_number_button(self):
        return self.wait_and_click_invisible_element(HomePageLocators.pop_up_window_order_close)

    @allure.step("клик по заказу из ленты")
    def click_order(self):
        self.wait_and_click_element(HomePageLocators.order)

    @allure.step('загрузка всплывающего окна c деталями заказа')
    def wait_pop_up_window_order_details(self):
        return self.wait_element(HomePageLocators.pop_up_window_order)

    @allure.step("клик по кнопке личный кабинет")
    def click_personal_account_button(self):
        self.wait_and_click_invisible_element(BasePageLocators.personal_account_button)

    @allure.step("клик по кнопке история заказов")
    def click_order_history_button(self):
        self.wait_and_click_element(BasePageLocators.history_orders_button)

    @allure.step('получение истории заказов')
    def getting_order_history(self):
        return self.wait_all_element_located(BasePageLocators.history_of_orders)

    @allure.step('получение ленты заказов')
    def getting_order_feed(self):
        return self.wait_all_element_located(BasePageLocators.order_feed)

    @allure.step('получение заказов в работе')
    def getting_order_at_work(self):
        return self.wait_all_element_located(BasePageLocators.order_at_work)

    @allure.step('Получение количества заказов выполненных за сегодня')
    def get_today_orders_number(self):
        return self.find_element_return_text(BasePageLocators.completed_orders_today)

    @allure.step('Получение количества заказов выполненных за все время')
    def get_total_orders_number(self):
        return self.find_element_return_text(BasePageLocators.completed_orders_total)

    @allure.step("клик по скрытой кнопке лента заказов")
    def click_order_invisible_feed(self):
        self.wait_and_click_invisible_element(HomePageLocators.order_feed)

















