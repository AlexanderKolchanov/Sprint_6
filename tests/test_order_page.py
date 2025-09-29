import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import DataUser1, DataUser2


class TestOrder:
    """
    Класс тестов для проверки функциональности оформления заказа.
    """

    @pytest.mark.parametrize('user_data, button_method', [
        (DataUser1(), 'click_order_button_top'),
        (DataUser2(), 'click_order_button_bottom')
    ], ids=['top_button', 'bottom_button'])
    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Тестирование позитивного сценария заказа из разных точек входа')
    def test_successful_order(self, driver, user_data, button_method):
        """
        Тест проверяет успешное оформление заказа самоката.
        
        Args:
            driver: Фикстура с инициализированным браузером
            user_data: Данные пользователя для заполнения формы
            button_method (str): Название метода для клика по кнопке заказа
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        
        # ✅ ИСПРАВЛЕНО: убрано условие if/else, используем getattr
        click_method = getattr(main_page, button_method)
        click_method()  # Вызываем метод клика по кнопке
        
        order_page.data_entry_first_form(user_data)
        order_page.data_entry_second_form(user_data)
        
        assert order_page.check_displaying_of_button_check_status_of_order()