"""Класс: Заказ"""
from datetime import datetime
from typing import List, Optional


class Order:
    """Класс представляющий заказ"""
    
    def __init__(self, order_id: str, client_id: str, order_date: datetime, 
                 total_amount: float, status: str, items: List[str]):
        self.order_id = order_id
        self.client_id = client_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status
        self.items = items
        self.shipping_date = None
        self.tracking_number = None
        self.delivery_address = None
        
    def update_status(self, new_status: str) -> None:
        """Обновление статуса заказа"""
        self.status = new_status
    
    def add_tracking(self, tracking_number: str) -> None:
        """Добавление номера отслеживания"""
        self.tracking_number = tracking_number
    
    def set_shipping_date(self, date: datetime) -> None:
        """Установка даты отправки"""
        self.shipping_date = date
    
    def calculate_days_since_order(self) -> int:
        """Вычисление дней с момента заказа"""
        return (datetime.now() - self.order_date).days
    
    def add_delivery_address(self, address: str) -> None:
        """Добавление адреса доставки"""
        self.delivery_address = address


