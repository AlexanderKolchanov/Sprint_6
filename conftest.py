import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from urls import URLs


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для инициализации драйвера Firefox.
    
    Устанавливает драйвер через webdriver_manager, открывает браузер в полном окне
    и переходит на базовый URL перед выполнением теста.
    
    Returns:
        WebDriver: Настроенный экземпляр драйвера Firefox
    """
    # Установка и инициализация сервиса Firefox драйвера
    service = Service(GeckoDriverManager().install())
    
    # Создание экземпляра драйвера Firefox
    driver = webdriver.Firefox(service=service)
    
    # Максимизация окна браузера
    driver.maximize_window()
    
    # Переход на базовый URL домашней страницы
    driver.get(URLs.base_url)
    
    # Возврат драйвера тестовой функции
    yield driver
    
    # Закрытие браузера после завершения теста
    driver.quit()