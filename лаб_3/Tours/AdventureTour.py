"""Класс: Приключенческий тур"""
from datetime import datetime
from typing import List, Optional


class AdventureTour:
    """Класс представляющий приключенческий тур"""
    
    def __init__(self, tour_id: str, name: str, location: str, difficulty_level: str, 
                 start_date: datetime, duration_days: int, price: float, min_age: int):
        self.tour_id = tour_id
        self.name = name
        self.location = location
        self.difficulty_level = difficulty_level
        self.start_date = start_date
        self.duration_days = duration_days
        self.price = price
        self.min_age = min_age
        self.equipment_required = []
        self.max_participants = 15
        self.current_participants = 0
        self.safety_rating = 5.0
        
    def add_equipment(self, equipment: str) -> None:
        """Добавление необходимого оборудования"""
        if equipment not in self.equipment_required:
            self.equipment_required.append(equipment)
    
    def check_age_requirement(self, age: int) -> bool:
        """Проверка возрастного требования"""
        return age >= self.min_age
    
    def add_participant(self, age: int) -> None:
        """Добавление участника с проверкой возраста"""
        if not self.check_age_requirement(age):
            raise ValueError(f"Минимальный возраст: {self.min_age}")
        if self.current_participants < self.max_participants:
            self.current_participants += 1
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.current_participants * self.price
    
    def update_safety_rating(self, rating: float) -> None:
        """Обновление рейтинга безопасности"""
        self.safety_rating = (self.safety_rating + rating) / 2


