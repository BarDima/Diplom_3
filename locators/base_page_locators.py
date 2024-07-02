from selenium.webdriver.common.by import By

class BasePageLocators:
    enter_account_button = (By.XPATH, "*//button[text()='Войти в аккаунт']")  # кнопка войти в аккаунт
    EMAIL_FIELD = (By.XPATH, "*//input[@name = 'name']")  # поле Email
    PASSWORD_FIELD = (By.XPATH, "*//input[@name='Пароль']")  # поле пароль
    BUTTON_ENTRANCE = (By.XPATH, "*//button[text()='Войти']")  # кнопка войти
    personal_account_button = (By.XPATH, "*//a[@href='/account']")  # кнопка личный кабинет
    history_orders_button = (By.XPATH, "*//a[@href='/account/order-history']")  # кнопка история заказов
    history_of_orders = (By.XPATH, "*//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]/a/div/p[1]")  # получение истории заказов
    order_feed = (By.XPATH, "*//div[@class='OrderFeed_contentBox__3-tWb']/ul/li")  # получение ленты заказов
    order_at_work = (By.XPATH,  "*//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")#заказы в работе
    completed_orders_today = (By.XPATH, '*//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]')#выполнено заказов за сегодня
    completed_orders_total = By.XPATH, ('//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,'
                                        '"digits-large")]')#выполнено заказов за все время
    text_order_feed = (By.XPATH, '//h1[text()="Лента заказов"]')#текст лента заказов
