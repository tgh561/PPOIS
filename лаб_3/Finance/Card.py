"""Класс: Банковская карта"""
from datetime import datetime
from typing import List, Optional
import re


class Card:
    """Класс представляющий банковскую карту"""
    
    def __init__(self, card_number: str, cardholder_name: str, expiry_date: datetime, 
                 cvv: str, card_type: str, balance: float, bank_name: str):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.card_type = card_type
        self.balance = balance
        self.bank_name = bank_name
        self.is_active = True
        self.transaction_history = []
        self.daily_limit = 10000.0
        
    def validate_card_number(self) -> bool:
        """Валидация номера карты"""
        from Exceptions.InvalidCardNumberException import InvalidCardNumberException
        # Простая валидация: удаляем пробелы и проверяем длину
        cleaned = re.sub(r'\s', '', self.card_number)
        if len(cleaned) < 13 or len(cleaned) > 19:
            raise InvalidCardNumberException(self.card_number)
        return True
    
    def check_expiry(self) -> bool:
        """Проверка срока действия"""
        today = datetime.now()
        return today < self.expiry_date
    
    def verify_card(self) -> bool:
        """Проверка карты"""
        from Exceptions.CardNotFoundException import CardNotFoundException
        if not self.is_active:
            raise CardNotFoundException(self.card_number)
        if not self.check_expiry():
            return False
        return self.validate_card_number()
    
    def deduct_amount(self, amount: float) -> None:
        """Списание суммы"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        if self.balance < amount:
            raise InsufficientFundsException(self.balance, amount)
        self.balance -= amount
        self.transaction_history.append({
            "type": "debit",
            "amount": amount,
            "date": datetime.now()
        })
    
    def add_amount(self, amount: float) -> None:
        """Пополнение карты"""
        self.balance += amount
        self.transaction_history.append({
            "type": "credit",
            "amount": amount,
            "date": datetime.now()
        })
    
    def transfer_to_card(self, target_card: 'Card', amount: float) -> None:
        """Перевод денег с одной карты на другую"""
        self.verify_card()
        target_card.verify_card()
        self.deduct_amount(amount)
        target_card.add_amount(amount)
    
    def get_balance(self) -> float:
        """Получение баланса"""
        return self.balance


