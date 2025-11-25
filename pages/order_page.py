import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    """
    Page Object для страницы оформления заказа.
    Содержит методы для взаимодействия с формами заказа.
    """

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self, station_name):
        """Выбор станции метро из выпадающего списка по названию"""
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click_on_element(station_locator)

    @allure.step('Проверить отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        """Проверка отображения кнопки статуса заказа (признак успешного оформления)"""
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_CHECK_STATUS_OF_ORDER)

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, user_data):
        """
        Заполнение первой формы заказа с персональными данными пользователя.
        
        Args:
            user_data: Объект с данными пользователя (DataUser1 или DataUser2)
        """
        # Ожидание загрузки формы перед началом заполнения
        self.wait_visibility_of_element(OrderPageLocators.INPUT_NAME)
        
        # Заполнение имени пользователя
        self.click_on_element(OrderPageLocators.INPUT_NAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_NAME, user_data.name)
        
        # Заполнение фамилии пользователя
        self.click_on_element(OrderPageLocators.INPUT_LASTNAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_LASTNAME, user_data.surname)
        
        # Заполнение адреса доставки
        self.click_on_element(OrderPageLocators.INPUT_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.INPUT_ADDRESS, user_data.address)
        
        # Выбор станции метро из выпадающего списка
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        self.send_keys_to_input(OrderPageLocators.INPUT_METRO, user_data.station_name)
        self.select_station(user_data.station_name)
        
        # Заполнение номера телефона
        self.click_on_element(OrderPageLocators.INPUT_PHONE)
        self.send_keys_to_input(OrderPageLocators.INPUT_PHONE, user_data.telephone)
        
        # Переход ко второй форме заказа
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, user_data):
        """
        Заполнение второй формы заказа с данными об аренде самоката.
        
        Args:
            user_data: Объект с данными пользователя (DataUser1 или DataUser2)
        """
        # Ожидание загрузки второй формы
        self.wait_visibility_of_element(OrderPageLocators.INPUT_DATE)
        
        # Заполнение даты доставки самоката
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.send_keys_to_input(OrderPageLocators.INPUT_DATE, user_data.date)
        
        # Выбор цвета самоката в зависимости от данных пользователя
        if 'чёрный' in user_data.color:
            self.click_on_element(OrderPageLocators.CHECKBOX_BLACK_COLOR_SCOOTER)
        else:
            self.click_on_element(OrderPageLocators.CHECKBOX_GREY_COLOR_SCOOTER)
        
        # Выбор срока аренды из выпадающего списка
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{user_data.period}']")
        self.click_on_element(period_locator)
        
        # Заполнение комментария для курьера
        self.click_on_element(OrderPageLocators.INPUT_COMMENT)
        self.send_keys_to_input(OrderPageLocators.INPUT_COMMENT, user_data.comment)
        
        # Нажатие кнопки оформления заказа
        self.click_on_element(OrderPageLocators.BUTTON_MAKE_ORDER)
        
        # Ожидание появления модального окна подтверждения заказа
        self.wait_visibility_of_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)
        
        # Подтверждение заказа в модальном окне
        self.click_on_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)