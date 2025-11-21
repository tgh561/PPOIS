"""Тесты для класса Question"""
import pytest
from datetime import datetime, timedelta
from Support.Question import Question


class TestQuestion:
    """Тесты для класса Question"""
    
    @pytest.fixture
    def question(self):
        """Фикстура для создания вопроса"""
        return Question(
            question_id="Q001",
            client_id="ivan@example.com",
            question_text="Как забронировать тур?",
            question_date=datetime.now(),
            category="booking",
            status="open"
        )
    
    def test_init(self, question):
        """Тест инициализации"""
        assert question.question_id == "Q001"
        assert question.client_id == "ivan@example.com"
        assert question.question_text == "Как забронировать тур?"
        assert question.category == "booking"
        assert question.status == "open"
        assert question.answer is None
        assert question.answered_date is None
        assert question.answered_by is None
        assert question.priority == "normal"
    
    def test_answer_question(self, question):
        """Тест ответа на вопрос"""
        answer_text = "Позвоните по телефону 8-800-..."
        staff_id = "STAFF001"
        question.answer_question(answer_text, staff_id)
        assert question.answer == answer_text
        assert question.answered_by == staff_id
        assert question.status == "answered"
        assert question.answered_date is not None
    
    def test_set_priority(self, question):
        """Тест установки приоритета"""
        question.set_priority("high")
        assert question.priority == "high"
        
        question.set_priority("low")
        assert question.priority == "low"
    
    def test_calculate_response_time_with_answer(self, question):
        """Тест вычисления времени ответа - есть ответ"""
        question.answered_date = datetime.now() + timedelta(days=2)
        response_time = question.calculate_response_time()
        assert response_time == 2
    
    def test_calculate_response_time_no_answer(self, question):
        """Тест вычисления времени ответа - нет ответа"""
        response_time = question.calculate_response_time()
        assert response_time is None
    
    def test_is_answered_true(self, question):
        """Тест проверки наличия ответа - да"""
        question.status = "answered"
        question.answer = "Ответ на вопрос"
        assert question.is_answered() is True
    
    def test_is_answered_false_no_answer(self, question):
        """Тест проверки наличия ответа - нет ответа"""
        question.status = "answered"
        question.answer = None
        assert question.is_answered() is False
    
    def test_is_answered_false_not_answered(self, question):
        """Тест проверки наличия ответа - статус не answered"""
        question.status = "open"
        question.answer = "Ответ"
        assert question.is_answered() is False
    
    def test_escalate(self, question):
        """Тест эскалации вопроса"""
        question.escalate()
        assert question.priority == "high"
    
    def test_get_days_since_question(self, question):
        """Тест получения дней с момента вопроса"""
        question.question_date = datetime.now() - timedelta(days=5)
        days = question.get_days_since_question()
        assert days == 5



