"""Класс: Групповой тур"""
from datetime import datetime
from typing import List, Optional


class GroupTour:
    """Класс представляющий групповой тур"""
    
    def __init__(self, tour_id: str, name: str, destination: str, start_date: datetime, 
                 end_date: datetime, price_per_person: float, min_group_size: int, 
                 max_group_size: int):
        self.tour_id = tour_id
        self.name = name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.price_per_person = price_per_person
        self.min_group_size = min_group_size
        self.max_group_size = max_group_size
        self.current_size = 0
        self.group_discount = 0.0
        self.participants = []
        
    def add_participant(self, participant_id: str) -> None:
        """Добавление участника"""
        if self.current_size < self.max_group_size:
            self.current_size += 1
            self.participants.append(participant_id)
            self.calculate_group_discount()
    
    def calculate_group_discount(self) -> None:
        """Вычисление групповой скидки"""
        if self.current_size >= 15:
            self.group_discount = 0.15
        elif self.current_size >= 10:
            self.group_discount = 0.10
        elif self.current_size >= 5:
            self.group_discount = 0.05
    
    def calculate_total_price(self) -> float:
        """Вычисление общей цены"""
        base_total = self.current_size * self.price_per_person
        return base_total * (1 - self.group_discount)
    
    def is_minimum_met(self) -> bool:
        """Проверка минимального количества"""
        return self.current_size >= self.min_group_size
    
    def get_duration_days(self) -> int:
        """Получение продолжительности в днях"""
        return (self.end_date - self.start_date).days


