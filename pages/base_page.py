from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    @allure.step('клик по элементу')
    def click_element(self, locator):
        element = self.web_driver.find_element(*locator)
        element.click()

    @allure.step('ожидание появления и клик по элементу')
    def wait_and_click_element(self, locator, timeout=30):
        return WebDriverWait(self.web_driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('возвращаем текущую страницу')
    def get_current_url(self):
        return self.web_driver.current_url

    @allure.step('поиск элеменета')
    def find_element(self, *locator):
        return self.web_driver.find_element(*locator).click()

    @allure.step('ввод текста')
    def enter_text_to_field(self, locator, text):
        element = WebDriverWait(self.web_driver, 20).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    @allure.step('ожидание появления элемента')
    def wait_element(self, locator, timeout=20):
        return WebDriverWait(self.web_driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('ожидание исчезновения элемента')
    def wait_disappear_element(self, locator):
        return WebDriverWait(self.web_driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('перетаскивание элемента на заданное место')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = WebDriverWait(self.web_driver, 10).until(
        EC.presence_of_element_located(source_locator))
        target_element = WebDriverWait(self.web_driver, 10).until(
        EC.presence_of_element_located(target_locator))
        actions = ActionChains(self.web_driver)
        actions.drag_and_drop(source_element, target_element).perform()


    @allure.step('ожидание появления элемента и возвращение текста')
    def wait_element_return_text(self, locator):
        return self.wait_element(locator).text

    @allure.step('ожидание появления и клик по перекрытому элементу')
    def wait_and_click_invisible_element(self, locator, timeout=30):
        element = WebDriverWait(self.web_driver, timeout).until(EC.element_to_be_clickable(locator))
        self.web_driver.execute_script("arguments[0].click();", element)

    @allure.step('ожидание появления списка элементов')
    def wait_all_element_located(self, locator, timeout=20):
        elements = WebDriverWait(self.web_driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]


    def find_element_return_text(self, locator):
        element = self.web_driver.find_element(*locator)
        return element.text


