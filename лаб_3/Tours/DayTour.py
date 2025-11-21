"""Класс: Однодневный тур"""
from datetime import datetime
from typing import List, Optional


class DayTour:
    """Класс представляющий однодневный тур"""
    
    def __init__(self, tour_id: str, name: str, location: str, start_time: datetime, 
                 end_time: datetime, price: float, max_participants: int, includes_meal: bool):
        self.tour_id = tour_id
        self.name = name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.max_participants = max_participants
        self.includes_meal = includes_meal
        self.current_participants = 0
        self.transport_included = False
        
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в часах"""
        delta = self.end_time - self.start_time
        return delta.seconds // 3600
    
    def add_participant(self) -> None:
        """Добавление участника"""
        if self.current_participants < self.max_participants:
            self.current_participants += 1
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.current_participants * self.price
    
    def is_full(self) -> bool:
        """Проверка заполненности"""
        return self.current_participants >= self.max_participants
    
    def enable_transport(self) -> None:
        """Включение транспорта"""
        self.transport_included = True


