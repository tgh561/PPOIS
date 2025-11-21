"""Класс: Рейс"""
from datetime import datetime
from typing import List, Optional


class Flight:
    """Класс представляющий рейс"""
    
    def __init__(self, flight_id: str, airline: str, flight_number: str, 
                 departure_airport: str, arrival_airport: str, departure_time: datetime, 
                 arrival_time: datetime, price: float, available_seats: int):
        self.flight_id = flight_id
        self.airline = airline
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.available_seats = available_seats
        self.total_seats = available_seats
        self.booking_count = 0
        self.baggage_allowance = 20.0
        
    def book_seat(self) -> None:
        """Бронирование места"""
        if self.available_seats > 0:
            self.available_seats -= 1
            self.booking_count += 1
        else:
            raise ValueError("Нет доступных мест")
    
    def cancel_seat(self) -> None:
        """Отмена места"""
        if self.available_seats < self.total_seats:
            self.available_seats += 1
            self.booking_count -= 1
    
    def calculate_duration(self) -> int:
        """Вычисление продолжительности в часах"""
        delta = self.arrival_time - self.departure_time
        return delta.seconds // 3600
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return (self.total_seats - self.available_seats) * self.price
    
    def is_full(self) -> bool:
        """Проверка заполненности"""
        return self.available_seats == 0
    
    def get_seat_occupancy_rate(self) -> float:
        """Получение процента занятости"""
        return (self.total_seats - self.available_seats) / self.total_seats
    
    def link_to_booking(self, booking) -> None:
        """Связь с бронированием (ассоциация с Booking)"""
        from Bookings.Booking import Booking
        if isinstance(booking, Booking):
            self.book_seat()
    
    def assign_to_tour(self, tour) -> None:
        """Назначение тура (ассоциация с Tour)"""
        from Tours.Tour import Tour
        if isinstance(tour, Tour):
            tour.flight_id = self.flight_id
    
    def link_to_reservation(self, reservation) -> None:
        """Связь с резервацией (ассоциация с Reservation)"""
        from Bookings.Reservation import Reservation
        if isinstance(reservation, Reservation):
            if reservation.service_type == "flight":
                self.book_seat()


