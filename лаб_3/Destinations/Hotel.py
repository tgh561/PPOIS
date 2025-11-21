"""Класс: Отель"""
from datetime import datetime
from typing import List, Optional


class Hotel:
    """Класс представляющий отель"""
    
    def __init__(self, hotel_id: str, name: str, location: str, stars: int, 
                 total_rooms: int, price_per_night: float, check_in_time: str, 
                 check_out_time: str):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.stars = stars
        self.total_rooms = total_rooms
        self.price_per_night = price_per_night
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.available_rooms = total_rooms
        self.rating = 0.0
        self.amenities = []
        self.bookings = []
        
    def check_availability(self, check_in_date: datetime, check_out_date: datetime) -> bool:
        """Проверка доступности номеров"""
        from Exceptions.HotelFullException import HotelFullException
        if self.available_rooms <= 0:
            raise HotelFullException(self.name, str(check_in_date))
        return True
    
    def book_room(self, check_in_date: datetime, nights: int) -> None:
        """Бронирование номера"""
        self.check_availability(check_in_date, None)
        self.available_rooms -= 1
    
    def release_room(self) -> None:
        """Освобождение номера"""
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1
    
    def calculate_total_price(self, nights: int) -> float:
        """Вычисление общей цены"""
        return self.price_per_night * nights
    
    def add_amenity(self, amenity: str) -> None:
        """Добавление удобства"""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
    
    def update_rating(self, rating: float) -> None:
        """Обновление рейтинга"""
        self.rating = (self.rating + rating) / 2
    
    def assign_to_destination(self, destination) -> None:
        """Назначение направления (ассоциация с Destination)"""
        from Destinations.Destination import Destination
        if isinstance(destination, Destination):
            self.location = destination.city
    
    def process_reservation(self, reservation) -> None:
        """Обработка резервации (ассоциация с Reservation)"""
        from Bookings.Reservation import Reservation
        if isinstance(reservation, Reservation):
            if reservation.service_type == "hotel":
                self.book_room(reservation.start_date, reservation.calculate_duration())
    
    def assign_to_city(self, city) -> None:
        """Назначение города (ассоциация с City)"""
        from Destinations.City import City
        if isinstance(city, City):
            self.location = city.name


