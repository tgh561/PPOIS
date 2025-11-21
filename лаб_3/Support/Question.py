"""Класс: Вопрос"""
from datetime import datetime
from typing import List, Optional


class Question:
    """Класс представляющий вопрос"""
    
    def __init__(self, question_id: str, client_id: str, question_text: str, 
                 question_date: datetime, category: str, status: str = "open"):
        self.question_id = question_id
        self.client_id = client_id
        self.question_text = question_text
        self.question_date = question_date
        self.category = category
        self.status = status
        self.answer = None
        self.answered_date = None
        self.answered_by = None
        self.priority = "normal"
        
    def answer_question(self, answer_text: str, staff_id: str) -> None:
        """Ответ на вопрос"""
        self.answer = answer_text
        self.answered_date = datetime.now()
        self.answered_by = staff_id
        self.status = "answered"
    
    def set_priority(self, priority: str) -> None:
        """Установка приоритета"""
        self.priority = priority
    
    def calculate_response_time(self) -> Optional[int]:
        """Вычисление времени ответа"""
        if self.answered_date:
            delta = self.answered_date - self.question_date
            return delta.days
        return None
    
    def is_answered(self) -> bool:
        """Проверка наличия ответа"""
        return self.status == "answered" and self.answer is not None
    
    def escalate(self) -> None:
        """Эскалация вопроса"""
        self.priority = "high"
    
    def get_days_since_question(self) -> int:
        """Получение дней с момента вопроса"""
        return (datetime.now() - self.question_date).days


