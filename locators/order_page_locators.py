from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля первой формы заказа
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    
    # Поля второй формы заказа
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    FIELD_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    CHECKBOX_BLACK_COLOR_SCOOTER = (By.ID, "black")
    CHECKBOX_GREY_COLOR_SCOOTER = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # ЛОКАТОР ДЛЯ КНОПКИ "ЗАКАЗАТЬ"
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    
    # Модальное окно подтверждения
    BUTTON_YES_CONFIRM_ORDER = (By.XPATH, "//button[text()='Да']")
    
    # Кнопка статуса заказа после успешного оформления
    BUTTON_CHECK_STATUS_OF_ORDER = (By.XPATH, "//button[text()='Посмотреть статус']")