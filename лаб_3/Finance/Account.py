"""Класс: Счет"""
from datetime import datetime
from typing import List, Optional


class Account:
    """Класс представляющий банковский счет"""
    
    def __init__(self, account_id: str, account_number: str, account_type: str, 
                 balance: float, currency: str, owner_id: str, opening_date: datetime, 
                 interest_rate: float = 0.0):
        self.account_id = account_id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.currency = currency
        self.owner_id = owner_id
        self.opening_date = opening_date
        self.interest_rate = interest_rate
        self.transactions = []
        self.is_active = True
        self.overdraft_limit = 0.0
        
    def deposit(self, amount: float) -> None:
        """Пополнение счета"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount,
            "date": datetime.now()
        })
    
    def withdraw(self, amount: float) -> None:
        """Снятие средств"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        available_balance = self.balance + self.overdraft_limit
        if available_balance < amount:
            raise InsufficientFundsException(self.balance, amount)
        self.balance -= amount
        self.transactions.append({
            "type": "withdrawal",
            "amount": amount,
            "date": datetime.now()
        })
    
    def transfer_to_account(self, target_account: 'Account', amount: float) -> None:
        """Перевод денег с одного счета на другой"""
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def calculate_interest(self, months: int) -> float:
        """Вычисление процентов"""
        return self.balance * (self.interest_rate / 100) * months
    
    def get_transaction_count(self) -> int:
        """Получение количества транзакций"""
        return len(self.transactions)
    
    def close_account(self) -> None:
        """Закрытие счета"""
        if self.balance != 0:
            raise ValueError("Баланс должен быть нулевым")
        self.is_active = False
    
    def link_to_bank(self, bank) -> None:
        """Связь с банком (ассоциация с Bank)"""
        from Finance.Bank import Bank
        if isinstance(bank, Bank):
            self.bank_id = bank.bank_id
    
    def add_card(self, card) -> None:
        """Добавление карты (ассоциация с Card)"""
        from Finance.Card import Card
        if isinstance(card, Card):
            if card.card_number not in [t.get("card_number", "") for t in self.transactions]:
                self.cards = getattr(self, 'cards', [])
                self.cards.append(card.card_number)


