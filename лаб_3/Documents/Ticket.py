"""Класс: Билет"""
from datetime import datetime
from typing import List, Optional


class Ticket:
    """Класс представляющий билет"""
    
    def __init__(self, ticket_id: str, ticket_type: str, holder_name: str, 
                 event_name: str, venue: str, event_date: datetime, price: float, 
                 seat_number: str = None):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.holder_name = holder_name
        self.event_name = event_name
        self.venue = venue
        self.event_date = event_date
        self.price = price
        self.seat_number = seat_number
        self.is_used = False
        self.purchase_date = datetime.now()
        self.qr_code = None
        
    def validate_ticket(self) -> bool:
        """Валидация билета"""
        today = datetime.now()
        if self.is_used:
            return False
        if today > self.event_date:
            return False
        return True
    
    def use_ticket(self) -> None:
        """Использование билета"""
        if not self.validate_ticket():
            raise ValueError("Билет недействителен")
        self.is_used = True
    
    def set_qr_code(self, qr_code: str) -> None:
        """Установка QR-кода"""
        self.qr_code = qr_code
    
    def calculate_days_until_event(self) -> int:
        """Вычисление дней до события"""
        today = datetime.now()
        return (self.event_date - today).days
    
    def is_expired(self) -> bool:
        """Проверка истечения"""
        return datetime.now() > self.event_date
    
    def get_ticket_info(self) -> str:
        """Получение информации о билете"""
        return f"Билет {self.ticket_id} для {self.event_name} в {self.venue}"


