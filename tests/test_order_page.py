import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import DataUser1, DataUser2


class TestOrder:
    
    @allure.title('Проверка успешного оформления заказа через верхнюю кнопку')
    def test_successful_order_via_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button_top()  # ✅ Конкретный метод
        
        order_page.data_entry_first_form(DataUser1())
        order_page.data_entry_second_form(DataUser1())
        
        assert order_page.check_displaying_of_button_check_status_of_order()

    @allure.title('Проверка успешного оформления заказа через нижнюю кнопку')
    def test_successful_order_via_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button_bottom()  # ✅ Конкретный метод
        
        order_page.data_entry_first_form(DataUser2())
        order_page.data_entry_second_form(DataUser2())
        
        assert order_page.check_displaying_of_button_check_status_of_order()