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
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        self.wait.until(lambda driver: driver.title != "")
        return self.driver.title

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.is_displayed()

    @allure.step('Проверить, что элемент стал видимым')
    def wait_for_element_visible(self, locator):
        return self.wait_visibility_of_element(locator)

    @allure.step('Открыть URL')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def get_page_url(self):
        return self.driver.current_url

    @allure.step('Дождаться и переключиться на новую вкладку')
    def wait_and_switch_to_new_tab(self):
        """
        Умное переключение на новую вкладку.
        Перенесена логика из MainPage.check_yandex_redirect()
        """
        # Сохраняем текущую вкладку
        original_window = self.driver.current_window_handle
        
        # Ждем появления второй вкладки
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        
        # Переключаемся на новую вкладку (последнюю в списке)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        
        # Ждем загрузки страницы и проверяем URL
        self.wait.until(lambda driver: driver.current_url != 'about:blank')
        
        return original_window

    @allure.step('Переключиться на вкладку')
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step('Закрыть текущую вкладку')
    def close_current_tab(self):
        self.driver.close()