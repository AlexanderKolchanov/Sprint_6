import allure
import pytest
from pages.main_page import MainPage
from urls import URLs


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат"')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Переходим на страницу заказа и возвращаемся по лого
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        
        assert main_page.check_scooter_main_page()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_yandex_logo()
        
        assert main_page.check_yandex_redirect()