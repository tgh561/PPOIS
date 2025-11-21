"""Класс: Турпакет"""
from datetime import datetime
from typing import List, Optional


class Package:
    """Класс представляющий турпакет"""
    
    def __init__(self, package_id: str, name: str, description: str, duration_days: int, 
                 base_price: float, includes_flight: bool, includes_hotel: bool, 
                 includes_meals: bool):
        self.package_id = package_id
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.base_price = base_price
        self.includes_flight = includes_flight
        self.includes_hotel = includes_hotel
        self.includes_meals = includes_meals
        self.destinations = []
        self.services = []
        self.bookings_count = 0
        
    def add_destination(self, destination: str) -> None:
        """Добавление направления"""
        if destination not in self.destinations:
            self.destinations.append(destination)
    
    def add_service(self, service: str) -> None:
        """Добавление услуги"""
        if service not in self.services:
            self.services.append(service)
    
    def calculate_final_price(self, discount: float = 0.0) -> float:
        """Вычисление финальной цены"""
        return self.base_price * (1 - discount)
    
    def get_inclusions(self) -> List[str]:
        """Получение включенных услуг"""
        inclusions = []
        if self.includes_flight:
            inclusions.append("Перелет")
        if self.includes_hotel:
            inclusions.append("Отель")
        if self.includes_meals:
            inclusions.append("Питание")
        return inclusions
    
    def increment_bookings(self) -> None:
        """Увеличение счетчика бронирований"""
        self.bookings_count += 1


