"""Класс: Отмена"""
from datetime import datetime
from typing import List, Optional


class Cancellation:
    """Класс представляющий отмену бронирования"""
    
    def __init__(self, cancellation_id: str, booking_id: str, cancellation_date: datetime, 
                 reason: str, refund_amount: float, cancellation_fee: float):
        self.cancellation_id = cancellation_id
        self.booking_id = booking_id
        self.cancellation_date = cancellation_date
        self.reason = reason
        self.refund_amount = refund_amount
        self.cancellation_fee = cancellation_fee
        self.status = "pending"
        self.processed_date = None
        self.refund_processed = False
        
    def process_cancellation(self) -> None:
        """Обработка отмены"""
        from Exceptions.CancellationNotAllowedException import CancellationNotAllowedException
        days_until_travel = (self.cancellation_date - datetime.now()).days
        if days_until_travel < 1:
            raise CancellationNotAllowedException(self.booking_id, "Слишком поздно для отмены")
        self.status = "processed"
        self.processed_date = datetime.now()
    
    def process_refund(self) -> None:
        """Обработка возврата средств"""
        self.refund_processed = True
    
    def calculate_total_refund(self) -> float:
        """Вычисление общей суммы возврата"""
        return self.refund_amount - self.cancellation_fee
    
    def approve_cancellation(self) -> None:
        """Одобрение отмены"""
        self.status = "approved"
    
    def is_eligible_for_full_refund(self, days_before: int) -> bool:
        """Проверка права на полный возврат"""
        return days_before >= 30


