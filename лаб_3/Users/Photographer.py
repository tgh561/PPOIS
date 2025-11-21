"""Класс: Фотограф"""
from datetime import datetime
from typing import List


class Photographer:
    """Класс представляющий фотографа"""
    
    def __init__(self, name: str, surname: str, photographer_id: str, specialization: str, 
                 experience_years: int, hourly_rate: float, equipment: List[str]):
        self.name = name
        self.surname = surname
        self.photographer_id = photographer_id
        self.specialization = specialization
        self.experience_years = experience_years
        self.hourly_rate = hourly_rate
        self.equipment = equipment
        self.sessions_completed = 0
        self.portfolio_size = 0
        self.rating = 0.0
        self.is_available = True
        
    def add_equipment(self, item: str) -> None:
        """Добавление оборудования"""
        if item not in self.equipment:
            self.equipment.append(item)
    
    def complete_session(self) -> None:
        """Завершение фотосессии"""
        self.sessions_completed += 1
    
    def calculate_earnings(self, hours: int) -> float:
        """Вычисление заработка"""
        return hours * self.hourly_rate
    
    def add_to_portfolio(self) -> None:
        """Добавление в портфолио"""
        self.portfolio_size += 1
    
    def update_rating(self, rating: float) -> None:
        """Обновление рейтинга"""
        self.rating = (self.rating + rating) / 2


