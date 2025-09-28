from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельности элемента')
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        element.click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        element = self.wait_visibility_of_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.text

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.is_displayed()

    @allure.step('Проверить, что элемент стал видимым')
    def wait_for_element_visible(self, locator):
        return self.wait_visibility_of_element(locator)