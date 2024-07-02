from selenium.webdriver.common.by import By

class HomePageLocators:

    DESIGNER_BUTTON = (By.XPATH, "*//p[text()='Конструктор']")#кнопка конструктор
    order_feed = (By.XPATH, "*//p[text()='Лента Заказов']")#кнопка лента заказов
    SAUCES_BUTTON = (By.XPATH, "*//span[text()='Соусы']")#кнопка соусы
    pop_up_window = (By.XPATH, "*//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")#всплывающее окно с деталями ингредиентов
    closes_pop_up_window = (By.XPATH, "*//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']")#кнопка закрытия всплывающего окана
    order_feed_text = (By.XPATH, "*//h1[text()='Лента заказов']")#текст лента заказов
    MAKE_BURGER_TEXT = (By.XPATH, "*//h1[text()='Соберите бургер']")  # текст "Соберите бургер", раздел конструктор
    sauces_spicy = (By.XPATH, "*//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @href='/ingredient/61c0c5a71d1f82001bdaaa72']")#нгредиент соус spicy-X
    buns_r2_d3 = (By.XPATH, "*//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")#булка флурисцентная r2 d3
    place_of_relocation = (By.XPATH, "*//div[@class='constructor-element constructor-element_pos_top']")#место перетаскивания ингредиентов
    counter_increases = (By.XPATH, "*//p[@class='counter_counter__num__3nue1' and text()='2']")#увеличение счетчика добаления ингредиентов
    SECTION_FILLINGS = (By.XPATH, "*//h2[text()='Начинки']")  # раздел начинки
    filling = (By.XPATH, "*//a[@href='/ingredient/61c0c5a71d1f82001bdaaa70']")  #начинка Говяжий метеорит (отбивная)
    checkout_button = (By.XPATH, "*//button[text()='Оформить заказ']")#оформить заказ кнопка
    pop_up_window_order_prepared = (By.XPATH, "*//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")  # всплывающее окно ваш заказ начали готовить
    pop_up_window_order = (By.XPATH, "*//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")  # всплывающее окно с деталями заказа
    pop_up_window_order_close = (By.XPATH, "*//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'and @type='button']")  # кнопка закрытия всплывающего окна с номером заказа
    pop_up_window_number_order = (By.XPATH, "*//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")  # номер заказа
    order = (By.XPATH, "*//ul[@class='OrderFeed_list__OLh59']/li[1]")#последний заказ из списка


