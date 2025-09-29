
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import URLs
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.url = URLs.scooter_url

    @allure.step('Открыть главную страницу')
    def open(self):
        # ✅ Исправлено: используем метод из BasePage вместо прямого обращения к driver
        self.go_to_url(self.url)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click_on_element(self.locators.COOKIE_BUTTON)

    @allure.step('Нажать кнопку "Заказать" вверху страницы')
    def click_order_button_top(self):
        self.click_on_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step('Нажать кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(self.locators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(self.locators.YANDEX_LOGO)

    @allure.step('Проскроллить к разделу FAQ')
    def scroll_to_faq_section(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)

    @allure.step('Нажать на вопрос FAQ по номеру')
    def click_faq_question(self, question_number):
        question_locator = getattr(self.locators, f"QUESTION_{question_number}")
        self.click_on_element(question_locator)

    @allure.step('Получить текст ответа FAQ по номеру')
    def get_faq_answer_text(self, answer_number):
        answer_locator = getattr(self.locators, f"ANSWER_{answer_number}")
        return self.get_text_on_element(answer_locator)

    @allure.step('Проверить, что ответ FAQ отображается')
    def is_faq_answer_visible(self, answer_number):
        answer_locator = getattr(self.locators, f"ANSWER_{answer_number}")
        return self.check_displaying_of_element(answer_locator)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        # ✅ Исправлено: используем метод из BasePage вместо прямого обращения к driver
        return self.get_page_url()

    @allure.step('Проверить переход на главную страницу Самоката')
    def check_scooter_main_page(self):
        return self.get_current_url() == URLs.scooter_url

    @allure.step('Проверить переход на Дзен через логотип Яндекса')
    def check_yandex_redirect(self):
        """
        Проверка редиректа на Дзен после клика на логотип Яндекса.
        ✅ ИСПРАВЛЕНО: убраны прямые обращения к driver и WebDriverWait
        """
        # ✅ Исправлено: используем метод из BasePage вместо прямого WebDriverWait
        original_window = self.wait_and_switch_to_new_tab()
        
        # Получаем URL новой вкладки
        current_url = self.get_current_url()
        
        # ✅ Исправлено: используем методы из BasePage
        self.close_current_tab()
        self.switch_to_window(original_window)
        
        return "dzen.ru" in current_url