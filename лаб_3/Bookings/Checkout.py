"""Класс: Оформление заказа"""
from datetime import datetime
from typing import List, Optional


class Checkout:
    """Класс представляющий процесс оформления заказа"""
    
    def __init__(self, checkout_id: str, turist_id: str, booking_items: List[str], 
                 total_amount: float, checkout_date: datetime, discount_code: str = None):
        self.checkout_id = checkout_id
        self.turist_id = turist_id
        self.booking_items = booking_items
        self.total_amount = total_amount
        self.checkout_date = checkout_date
        self.discount_code = discount_code
        self.discount_amount = 0.0
        self.final_amount = total_amount
        self.status = "in_progress"
        self.shipping_address = None
        
    def apply_discount(self, discount_rate: float) -> None:
        """Применение скидки"""
        self.discount_amount = self.total_amount * discount_rate
        self.final_amount = self.total_amount - self.discount_amount
    
    def add_shipping_address(self, address: str) -> None:
        """Добавление адреса доставки"""
        self.shipping_address = address
    
    def complete_checkout(self) -> str:
        """Завершение оформления"""
        self.status = "completed"
        return f"Оформление {self.checkout_id} завершено"
    
    def calculate_final_total(self) -> float:
        """Вычисление финальной суммы"""
        return self.final_amount
    
    def add_item(self, item_id: str, price: float) -> None:
        """Добавление позиции"""
        self.booking_items.append(item_id)
        self.total_amount += price
        self.final_amount = self.total_amount - self.discount_amount


