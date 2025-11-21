"""Класс: Транзакция"""
from datetime import datetime
from typing import List, Optional


class Transaction:
    """Класс представляющий транзакцию"""
    
    def __init__(self, transaction_id: str, transaction_type: str, amount: float, 
                 source_account: str, destination_account: str, transaction_date: datetime, 
                 status: str = "pending", description: str = ""):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.transaction_date = transaction_date
        self.status = status
        self.description = description
        self.fee = 0.0
        self.exchange_rate = 1.0
        
    def process_transaction(self) -> bool:
        """Обработка транзакции"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        # Имитация проверки баланса
        source_balance = 1000.0
        if source_balance < self.amount + self.fee:
            raise InsufficientFundsException(source_balance, self.amount + self.fee)
        self.status = "completed"
        return True
    
    def calculate_fee(self, fee_rate: float = 0.02) -> float:
        """Вычисление комиссии"""
        self.fee = self.amount * fee_rate
        return self.fee
    
    def get_total_amount(self) -> float:
        """Получение общей суммы"""
        return self.amount + self.fee
    
    def cancel_transaction(self) -> None:
        """Отмена транзакции"""
        self.status = "cancelled"
    
    def convert_currency(self, exchange_rate: float) -> float:
        """Конвертация валюты"""
        self.exchange_rate = exchange_rate
        return self.amount * exchange_rate
    
    def is_completed(self) -> bool:
        """Проверка завершенности"""
        return self.status == "completed"


