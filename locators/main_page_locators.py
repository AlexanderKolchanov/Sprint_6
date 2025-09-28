from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH,".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH,".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # Куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    # FAQ секция
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    FAQ_ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel') and @aria-hidden='false']")
    
    # Конкретные вопросы (по тексту)
    QUESTION_0 = (By.ID, "accordion__heading-0")
    QUESTION_1 = (By.ID, "accordion__heading-1")
    QUESTION_2 = (By.ID, "accordion__heading-2")
    QUESTION_3 = (By.ID, "accordion__heading-3")
    QUESTION_4 = (By.ID, "accordion__heading-4")
    QUESTION_5 = (By.ID, "accordion__heading-5")
    QUESTION_6 = (By.ID, "accordion__heading-6")
    QUESTION_7 = (By.ID, "accordion__heading-7")
    
    # Ответы
    ANSWER_0 = (By.ID, "accordion__panel-0")
    ANSWER_1 = (By.ID, "accordion__panel-1")
    ANSWER_2 = (By.ID, "accordion__panel-2")
    ANSWER_3 = (By.ID, "accordion__panel-3")
    ANSWER_4 = (By.ID, "accordion__panel-4")
    ANSWER_5 = (By.ID, "accordion__panel-5")
    ANSWER_6 = (By.ID, "accordion__panel-6")
    ANSWER_7 = (By.ID, "accordion__panel-7")