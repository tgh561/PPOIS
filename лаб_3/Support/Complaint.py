"""Класс: Жалоба"""
from datetime import datetime
from typing import List, Optional


class Complaint:
    """Класс представляющий жалобу"""
    
    def __init__(self, complaint_id: str, client_id: str, complaint_type: str, 
                 description: str, complaint_date: datetime, priority: str = "medium"):
        self.complaint_id = complaint_id
        self.client_id = client_id
        self.complaint_type = complaint_type
        self.description = description
        self.complaint_date = complaint_date
        self.priority = priority
        self.status = "open"
        self.assigned_to = None
        self.resolution_date = None
        self.resolution_notes = ""
        
    def assign_to_staff(self, staff_id: str) -> None:
        """Назначение сотрудника"""
        self.assigned_to = staff_id
    
    def resolve(self, resolution_notes: str) -> None:
        """Решение жалобы"""
        self.status = "resolved"
        self.resolution_date = datetime.now()
        self.resolution_notes = resolution_notes
    
    def escalate(self) -> None:
        """Эскалация жалобы"""
        self.priority = "high"
    
    def set_priority(self, priority: str) -> None:
        """Установка приоритета"""
        self.priority = priority
    
    def calculate_resolution_time(self) -> Optional[int]:
        """Вычисление времени решения"""
        if self.resolution_date:
            delta = self.resolution_date - self.complaint_date
            return delta.days
        return None
    
    def is_resolved(self) -> bool:
        """Проверка решения"""
        return self.status == "resolved"
    
    def link_to_turist(self, turist) -> None:
        """Связь с туристом (ассоциация с Turist)"""
        from Users.Turist import Turist
        if isinstance(turist, Turist):
            self.client_id = turist.email
    
    def link_to_booking(self, booking) -> None:
        """Связь с бронированием (ассоциация с Booking)"""
        from Bookings.Booking import Booking
        if isinstance(booking, Booking):
            if booking.turist_id == self.client_id:
                self.booking_reference = booking.booking_id
    
    def assign_to_support_staff(self, support) -> None:
        """Назначение сотрудника поддержки (ассоциация с Support)"""
        from Users.Support import Support
        if isinstance(support, Support):
            self.assigned_to = support.employee_id


