"""Класс: Тур"""
from datetime import datetime
from typing import List, Optional


class Tour:
    """Класс представляющий тур"""
    
    def __init__(self, tour_id: str, name: str, description: str, destination: str, 
                 start_date: datetime, end_date: datetime, price: float, max_participants: int):
        self.tour_id = tour_id
        self.name = name
        self.description = description
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.max_participants = max_participants
        self.current_participants = 0
        self.duration_days = (end_date - start_date).days
        self.is_active = True
        self.rating = 0.0
        self.bookings = []
        
    def check_availability(self) -> bool:
        """Проверка доступности мест"""
        from Exceptions.TourFullException import TourFullException
        if self.current_participants >= self.max_participants:
            raise TourFullException(self.name)
        return True
    
    def add_participant(self) -> None:
        """Добавление участника"""
        self.check_availability()
        self.current_participants += 1
    
    def remove_participant(self) -> None:
        """Удаление участника"""
        if self.current_participants > 0:
            self.current_participants -= 1
    
    def calculate_total_revenue(self) -> float:
        """Вычисление общей выручки"""
        return self.current_participants * self.price
    
    def get_available_spots(self) -> int:
        """Получение доступных мест"""
        return self.max_participants - self.current_participants
    
    def update_rating(self, rating: float) -> None:
        """Обновление рейтинга"""
        self.rating = (self.rating + rating) / 2
    
    def assign_destination(self, destination) -> None:
        """Назначение направления (ассоциация с Destination)"""
        from Destinations.Destination import Destination
        if isinstance(destination, Destination):
            self.destination = destination.name
    
    def assign_guide(self, guide) -> None:
        """Назначение гида (ассоциация с Guide)"""
        from Users.Guide import Guide
        if isinstance(guide, Guide):
            self.guide_id = guide.guide_id
    
    def link_to_booking(self, booking) -> None:
        """Связь с бронированием (ассоциация с Booking)"""
        from Bookings.Booking import Booking
        if isinstance(booking, Booking):
            if booking.tour_id == self.tour_id:
                self.add_participant()
    
    def assign_flight(self, flight) -> None:
        """Назначение рейса (ассоциация с Flight)"""
        from Transport.Flight import Flight
        if isinstance(flight, Flight):
            self.flight_id = flight.flight_id
    
    def assign_hotel(self, hotel) -> None:
        """Назначение отеля (ассоциация с Hotel)"""
        from Destinations.Hotel import Hotel
        if isinstance(hotel, Hotel):
            self.hotel_id = hotel.hotel_id


