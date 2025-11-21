"""Класс: Тикет поддержки"""
from datetime import datetime
from typing import List, Optional


class Ticket:
    """Класс представляющий тикет службы поддержки"""
    
    def __init__(self, ticket_id: str, client_id: str, subject: str, description: str, 
                 ticket_date: datetime, category: str, priority: str = "medium"):
        self.ticket_id = ticket_id
        self.client_id = client_id
        self.subject = subject
        self.description = description
        self.ticket_date = ticket_date
        self.category = category
        self.priority = priority
        self.status = "open"
        self.assigned_to = None
        self.resolution_date = None
        self.messages = []
        self.satisfaction_rating = None
        
    def assign_to_support(self, support_id: str) -> None:
        """Назначение сотрудника поддержки"""
        self.assigned_to = support_id
    
    def add_message(self, message_text: str, sender_id: str, is_staff: bool = False) -> None:
        """Добавление сообщения"""
        self.messages.append({
            "text": message_text,
            "sender_id": sender_id,
            "is_staff": is_staff,
            "date": datetime.now()
        })
    
    def resolve_ticket(self, resolution_notes: str) -> None:
        """Решение тикета"""
        self.status = "resolved"
        self.resolution_date = datetime.now()
        self.add_message(resolution_notes, self.assigned_to, True)
    
    def close_ticket(self) -> None:
        """Закрытие тикета"""
        self.status = "closed"
    
    def set_satisfaction_rating(self, rating: float) -> None:
        """Установка рейтинга удовлетворенности"""
        if rating < 1.0 or rating > 5.0:
            raise ValueError("Рейтинг должен быть от 1 до 5")
        self.satisfaction_rating = rating
    
    def calculate_resolution_time(self) -> Optional[int]:
        """Вычисление времени решения"""
        if self.resolution_date:
            delta = self.resolution_date - self.ticket_date
            return delta.days
        return None
    
    def escalate_priority(self) -> None:
        """Повышение приоритета"""
        priority_levels = ["low", "medium", "high", "urgent"]
        current_index = priority_levels.index(self.priority) if self.priority in priority_levels else 1
        if current_index < len(priority_levels) - 1:
            self.priority = priority_levels[current_index + 1]
    
    def is_resolved(self) -> bool:
        """Проверка решения"""
        return self.status == "resolved" or self.status == "closed"


