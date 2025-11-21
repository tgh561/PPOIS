"""Класс: Ресторан"""
from datetime import datetime
from typing import List, Optional


class Restaurant:
    """Класс представляющий ресторан"""
    
    def __init__(self, restaurant_id: str, name: str, location: str, cuisine_type: str, 
                 price_range: str, rating: float, capacity: int, opening_hours: str):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.cuisine_type = cuisine_type
        self.price_range = price_range
        self.rating = rating
        self.capacity = capacity
        self.opening_hours = opening_hours
        self.current_guests = 0
        self.menu_items = []
        self.reservations = []
        
    def make_reservation(self, guest_count: int) -> None:
        """Бронирование столика"""
        if self.current_guests + guest_count <= self.capacity:
            self.current_guests += guest_count
        else:
            raise ValueError("Ресторан переполнен")
    
    def cancel_reservation(self, guest_count: int) -> None:
        """Отмена бронирования"""
        self.current_guests = max(0, self.current_guests - guest_count)
    
    def add_menu_item(self, item_name: str, price: float) -> None:
        """Добавление позиции в меню"""
        self.menu_items.append({"name": item_name, "price": price})
    
    def calculate_average_price(self) -> float:
        """Вычисление средней цены"""
        if not self.menu_items:
            return 0.0
        return sum(item["price"] for item in self.menu_items) / len(self.menu_items)
    
    def update_rating(self, rating: float) -> None:
        """Обновление рейтинга"""
        self.rating = (self.rating + rating) / 2
    
    def is_available(self) -> bool:
        """Проверка доступности"""
        return self.current_guests < self.capacity


