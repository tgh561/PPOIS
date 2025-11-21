"""Класс: Служба поддержки"""
from datetime import datetime
from typing import List


class Support:
    """Класс представляющий сотрудника службы поддержки"""
    
    def __init__(self, name: str, surname: str, employee_id: str, shift: str, 
                 hire_date: datetime, salary: float, languages: List[str]):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.shift = shift
        self.hire_date = hire_date
        self.salary = salary
        self.languages = languages
        self.tickets_resolved = 0
        self.average_resolution_time = 0.0
        self.satisfaction_rating = 0.0
        
    def resolve_ticket(self, ticket_id: str, resolution_time: float) -> None:
        """Решение тикета"""
        self.tickets_resolved += 1
        self.average_resolution_time = (self.average_resolution_time + resolution_time) / 2
    
    def add_language(self, language: str) -> None:
        """Добавление языка"""
        if language not in self.languages:
            self.languages.append(language)
    
    def update_satisfaction_rating(self, rating: float) -> None:
        """Обновление рейтинга удовлетворенности"""
        self.satisfaction_rating = (self.satisfaction_rating + rating) / 2
    
    def calculate_productivity(self) -> float:
        """Вычисление продуктивности"""
        return self.tickets_resolved / max(self.average_resolution_time, 1)
    
    def is_available_for_shift(self, shift: str) -> bool:
        """Проверка доступности для смены"""
        return self.shift == shift


