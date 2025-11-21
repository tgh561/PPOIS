"""Класс: Виза"""
from datetime import datetime
from typing import List, Optional


class Visa:
    """Класс представляющий визу"""
    
    def __init__(self, visa_number: str, passport_number: str, country: str, 
                 visa_type: str, issue_date: datetime, expiry_date: datetime, 
                 entries_allowed: int, current_entries: int = 0):
        self.visa_number = visa_number
        self.passport_number = passport_number
        self.country = country
        self.visa_type = visa_type
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.entries_allowed = entries_allowed
        self.current_entries = current_entries
        self.is_valid = True
        self.purpose = "tourism"
        
    def check_validity(self) -> bool:
        """Проверка действительности визы"""
        today = datetime.now()
        if today > self.expiry_date:
            self.is_valid = False
            return False
        if self.current_entries >= self.entries_allowed:
            self.is_valid = False
            return False
        return True
    
    def add_entry(self) -> None:
        """Добавление въезда"""
        if self.current_entries < self.entries_allowed:
            self.current_entries += 1
        else:
            raise ValueError("Лимит въездов исчерпан")
    
    def calculate_days_until_expiry(self) -> int:
        """Вычисление дней до истечения"""
        today = datetime.now()
        return (self.expiry_date - today).days
    
    def get_remaining_entries(self) -> int:
        """Получение оставшихся въездов"""
        return self.entries_allowed - self.current_entries
    
    def set_purpose(self, purpose: str) -> None:
        """Установка цели поездки"""
        self.purpose = purpose
    
    def is_multiple_entry(self) -> bool:
        """Проверка множественного въезда"""
        return self.entries_allowed > 1


