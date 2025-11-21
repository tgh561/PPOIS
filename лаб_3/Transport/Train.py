"""Класс: Поезд"""
from datetime import datetime
from typing import List, Optional


class Train:
    """Класс представляющий поезд"""
    
    def __init__(self, train_id: str, train_number: str, route: str, 
                 departure_station: str, arrival_station: str, departure_time: datetime, 
                 arrival_time: datetime, price: float, total_seats: int):
        self.train_id = train_id
        self.train_number = train_number
        self.route = route
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.booked_seats = 0
        self.has_restaurant = False
        self.comfort_class = "economy"
        
    def book_seat(self, seat_class: str = "economy") -> None:
        """Бронирование места"""
        if self.available_seats > 0:
            self.available_seats -= 1
            self.booked_seats += 1
            self.comfort_class = seat_class
        else:
            raise ValueError("Нет доступных мест")
    
    def cancel_seat(self) -> None:
        """Отмена места"""
        if self.available_seats < self.total_seats:
            self.available_seats += 1
            self.booked_seats -= 1
    
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в часах"""
        delta = self.arrival_time - self.departure_time
        return delta.seconds // 3600
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.booked_seats * self.price
    
    def set_comfort_class(self, comfort_class: str) -> None:
        """Установка класса комфорта"""
        self.comfort_class = comfort_class
    
    def get_occupancy_rate(self) -> float:
        """Получение процента занятости"""
        return self.booked_seats / self.total_seats


