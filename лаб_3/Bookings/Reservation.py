"""Класс: Резервация"""
from datetime import datetime
from typing import List, Optional


class Reservation:
    """Класс представляющий резервацию"""
    
    def __init__(self, reservation_id: str, client_id: str, service_type: str, 
                 service_id: str, reservation_date: datetime, start_date: datetime, 
                 end_date: datetime, price: float):
        self.reservation_id = reservation_id
        self.client_id = client_id
        self.service_type = service_type
        self.service_id = service_id
        self.reservation_date = reservation_date
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.status = "active"
        self.special_requests = []
        
    def add_special_request(self, request: str) -> None:
        """Добавление специального запроса"""
        if request not in self.special_requests:
            self.special_requests.append(request)
    
    def extend_reservation(self, additional_days: int) -> None:
        """Продление резервации"""
        from datetime import timedelta
        self.end_date += timedelta(days=additional_days)
        self.price += self.price * (additional_days / (self.end_date - self.start_date).days)
    
    def cancel_reservation(self) -> None:
        """Отмена резервации"""
        self.status = "cancelled"
    
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в днях"""
        return (self.end_date - self.start_date).days
    
    def is_active(self) -> bool:
        """Проверка активности"""
        return self.status == "active" and datetime.now() < self.end_date
    
    def link_to_turist(self, turist) -> None:
        """Связь с туристом (ассоциация с Turist)"""
        from Users.Turist import Turist
        if isinstance(turist, Turist):
            self.client_id = turist.email
    
    def assign_hotel(self, hotel) -> None:
        """Назначение отеля (ассоциация с Hotel)"""
        from Destinations.Hotel import Hotel
        if isinstance(hotel, Hotel):
            if self.service_type == "hotel":
                self.service_id = hotel.hotel_id


