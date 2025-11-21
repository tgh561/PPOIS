"""Класс: Автобус"""
from datetime import datetime
from typing import List, Optional


class Bus:
    """Класс представляющий автобус"""
    
    def __init__(self, bus_id: str, route: str, departure_station: str, 
                 arrival_station: str, departure_time: datetime, arrival_time: datetime, 
                 price: float, capacity: int, driver_id: str):
        self.bus_id = bus_id
        self.route = route
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.capacity = capacity
        self.driver_id = driver_id
        self.current_passengers = 0
        self.booking_count = 0
        self.has_wifi = False
        
    def add_passenger(self) -> None:
        """Добавление пассажира"""
        if self.current_passengers < self.capacity:
            self.current_passengers += 1
            self.booking_count += 1
        else:
            raise ValueError("Автобус переполнен")
    
    def remove_passenger(self) -> None:
        """Удаление пассажира"""
        if self.current_passengers > 0:
            self.current_passengers -= 1
            self.booking_count -= 1
    
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в часах"""
        delta = self.arrival_time - self.departure_time
        return delta.seconds // 3600
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.current_passengers * self.price
    
    def enable_wifi(self) -> None:
        """Включение WiFi"""
        self.has_wifi = True
    
    def get_occupancy_rate(self) -> float:
        """Получение процента занятости"""
        return self.current_passengers / self.capacity


