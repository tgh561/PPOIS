"""Класс: Круиз"""
from datetime import datetime
from typing import List, Optional


class Cruise:
    """Класс представляющий круиз"""
    
    def __init__(self, cruise_id: str, ship_name: str, departure_port: str, 
                 arrival_port: str, departure_date: datetime, arrival_date: datetime, 
                 price_per_person: float, total_cabins: int, route: List[str]):
        self.cruise_id = cruise_id
        self.ship_name = ship_name
        self.departure_port = departure_port
        self.arrival_port = arrival_port
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price_per_person = price_per_person
        self.total_cabins = total_cabins
        self.route = route
        self.available_cabins = total_cabins
        self.booked_cabins = 0
        self.has_all_inclusive = True
        self.entertainment_available = []
        
    def book_cabin(self, cabin_type: str = "standard") -> None:
        """Бронирование каюты"""
        if self.available_cabins > 0:
            self.available_cabins -= 1
            self.booked_cabins += 1
        else:
            raise ValueError("Нет доступных кают")
    
    def cancel_cabin(self) -> None:
        """Отмена каюты"""
        if self.available_cabins < self.total_cabins:
            self.available_cabins += 1
            self.booked_cabins -= 1
    
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в днях"""
        return (self.arrival_date - self.departure_date).days
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.booked_cabins * self.price_per_person
    
    def add_entertainment(self, entertainment: str) -> None:
        """Добавление развлечения"""
        if entertainment not in self.entertainment_available:
            self.entertainment_available.append(entertainment)
    
    def get_occupancy_rate(self) -> float:
        """Получение процента занятости"""
        return self.booked_cabins / self.total_cabins


