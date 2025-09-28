import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import DataUser1, DataUser2


class TestOrder:
    """
    Класс тестов для проверки функциональности оформления заказа.
    Содержит тесты позитивного сценария с различными наборами данных.
    """
    
    @pytest.mark.parametrize('order_button, user_data', [
        ('top', DataUser1()),  # Верхняя кнопка заказа с данными первого пользователя
        ('bottom', DataUser2())  # Нижняя кнопка заказа с данными второго пользователя
    ])
    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Тестирование позитивного сценария заказа из разных точек входа')
    def test_successful_order(self, driver, order_button, user_data):
        """
        Тест проверяет успешное оформление заказа самоката.
        
        Args:
            driver: Фикстура с инициализированным браузером
            order_button (str): Точка входа в заказ ('top' или 'bottom')
            user_data: Данные пользователя для заполнения формы
        """
        # Инициализация Page Object для главной страницы и страницы заказа
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Открытие главной страницы и принятие cookies
        main_page.open()
        main_page.accept_cookies()
        
        # Выбор точки входа в заказ (верхняя или нижняя кнопка)
        if order_button == 'top':
            main_page.click_order_button_top()  # Клик по верхней кнопке "Заказать"
        else:
            main_page.click_order_button_bottom()  # Клик по нижней кнопке "Заказать"
        
        # Заполнение первой формы с персональными данными пользователя
        order_page.data_entry_first_form(user_data)
        
        # Заполнение второй формы с данными об аренде самоката
        order_page.data_entry_second_form(user_data)
        
        # Проверка отображения кнопки проверки статуса заказа (признак успешного оформления)
        assert order_page.check_displaying_of_button_check_status_of_order()