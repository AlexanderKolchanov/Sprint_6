import allure
import pytest
from pages.main_page import MainPage
from data import FAQData


class TestFAQ:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_number, expected_answer', FAQData.FAQ_ANSWERS)
    def test_faq_questions_display_correct_answers(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Скроллим к FAQ и кликаем на вопрос
        main_page.scroll_to_faq_section()
        main_page.click_faq_question(question_number)
        
        # Получаем текст ответа и проверяем
        actual_answer = main_page.get_faq_answer_text(question_number)
        assert expected_answer in actual_answer