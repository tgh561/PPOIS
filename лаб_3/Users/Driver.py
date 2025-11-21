"""Класс: Водитель"""
from datetime import datetime
from typing import List


class Driver:
    """Класс представляющий водителя"""
    
    def __init__(self, name: str, surname: str, driver_id: str, license_number: str, 
                 license_expiry: datetime, experience_years: int, hourly_rate: float):
        self.name = name
        self.surname = surname
        self.driver_id = driver_id
        self.license_number = license_number
        self.license_expiry = license_expiry
        self.experience_years = experience_years
        self.hourly_rate = hourly_rate
        self.total_trips = 0
        self.total_distance = 0.0
        self.safety_rating = 5.0
        self.is_available = True
        
    def check_license_validity(self) -> bool:
        """Проверка действительности лицензии"""
        today = datetime.now()
        return today < self.license_expiry
    
    def add_trip(self, distance: float) -> None:
        """Добавление поездки"""
        self.total_trips += 1
        self.total_distance += distance
    
    def calculate_earnings(self, hours: int) -> float:
        """Вычисление заработка"""
        return hours * self.hourly_rate
    
    def update_safety_rating(self, rating: float) -> None:
        """Обновление рейтинга безопасности"""
        self.safety_rating = (self.safety_rating + rating) / 2
    
    def set_availability(self, available: bool) -> None:
        """Установка доступности"""
        self.is_available = available


