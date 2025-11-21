"""Класс: Ваучер"""
from datetime import datetime
from typing import List, Optional


class Voucher:
    """Класс представляющий ваучер"""
    
    def __init__(self, voucher_id: str, booking_id: str, voucher_code: str, 
                 discount_amount: float, valid_from: datetime, valid_until: datetime, 
                 is_used: bool = False):
        self.voucher_id = voucher_id
        self.booking_id = booking_id
        self.voucher_code = voucher_code
        self.discount_amount = discount_amount
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.is_used = is_used
        self.used_date = None
        self.discount_percentage = 0.0
        
    def validate_voucher(self) -> bool:
        """Валидация ваучера"""
        now = datetime.now()
        if self.is_used:
            return False
        if now < self.valid_from or now > self.valid_until:
            return False
        return True
    
    def use_voucher(self) -> None:
        """Использование ваучера"""
        if not self.validate_voucher():
            raise ValueError("Ваучер недействителен")
        self.is_used = True
        self.used_date = datetime.now()
    
    def calculate_discount(self, total_amount: float) -> float:
        """Вычисление скидки"""
        if self.discount_percentage > 0:
            return total_amount * (self.discount_percentage / 100)
        return self.discount_amount
    
    def set_percentage_discount(self, percentage: float) -> None:
        """Установка процентной скидки"""
        self.discount_percentage = percentage
    
    def is_expired(self) -> bool:
        """Проверка истечения срока"""
        return datetime.now() > self.valid_until


