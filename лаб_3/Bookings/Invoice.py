"""Класс: Счет"""
from datetime import datetime
from typing import List, Optional


class Invoice:
    """Класс представляющий счет"""
    
    def __init__(self, invoice_id: str, booking_id: str, client_name: str, 
                 invoice_date: datetime, due_date: datetime, subtotal: float, 
                 tax_rate: float, total: float):
        self.invoice_id = invoice_id
        self.booking_id = booking_id
        self.client_name = client_name
        self.invoice_date = invoice_date
        self.due_date = due_date
        self.subtotal = subtotal
        self.tax_rate = tax_rate
        self.total = total
        self.status = "unpaid"
        self.items = []
        self.payments = []
        
    def add_item(self, description: str, quantity: int, unit_price: float) -> None:
        """Добавление позиции в счет"""
        item = {
            "description": description,
            "quantity": quantity,
            "unit_price": unit_price,
            "total": quantity * unit_price
        }
        self.items.append(item)
        self.recalculate_totals()
    
    def recalculate_totals(self) -> None:
        """Пересчет итогов"""
        self.subtotal = sum(item["total"] for item in self.items)
        tax = self.subtotal * self.tax_rate
        self.total = self.subtotal + tax
    
    def add_payment(self, payment_amount: float) -> None:
        """Добавление платежа"""
        self.payments.append({"amount": payment_amount, "date": datetime.now()})
        total_paid = sum(p["amount"] for p in self.payments)
        if total_paid >= self.total:
            self.status = "paid"
    
    def calculate_tax(self) -> float:
        """Вычисление налога"""
        return self.subtotal * self.tax_rate
    
    def is_overdue(self) -> bool:
        """Проверка просрочки"""
        return datetime.now() > self.due_date and self.status != "paid"


