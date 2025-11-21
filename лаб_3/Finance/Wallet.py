"""Класс: Кошелек"""
from datetime import datetime
from typing import List, Optional, Dict


class Wallet:
    """Класс представляющий электронный кошелек"""
    
    def __init__(self, wallet_id: str, owner_id: str, currency: str, balance: float, 
                 creation_date: datetime, wallet_type: str = "digital"):
        self.wallet_id = wallet_id
        self.owner_id = owner_id
        self.currency = currency
        self.balance = balance
        self.creation_date = creation_date
        self.wallet_type = wallet_type
        self.is_active = True
        self.cards = []
        self.transaction_history = []
        
    def add_card(self, card_id: str) -> None:
        """Добавление карты"""
        if card_id not in self.cards:
            self.cards.append(card_id)
    
    def remove_card(self, card_id: str) -> None:
        """Удаление карты"""
        if card_id in self.cards:
            self.cards.remove(card_id)
    
    def add_funds(self, amount: float, source: str = "deposit") -> None:
        """Пополнение кошелька"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        self.transaction_history.append({
            "type": "credit",
            "amount": amount,
            "source": source,
            "date": datetime.now()
        })
    
    def deduct_funds(self, amount: float, description: str = "") -> None:
        """Списание средств"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        if self.balance < amount:
            raise InsufficientFundsException(self.balance, amount)
        self.balance -= amount
        self.transaction_history.append({
            "type": "debit",
            "amount": amount,
            "description": description,
            "date": datetime.now()
        })
    
    def transfer_to_wallet(self, target_wallet: 'Wallet', amount: float) -> None:
        """Перевод денег с одного кошелька на другой"""
        self.deduct_funds(amount, f"Transfer to {target_wallet.wallet_id}")
        target_wallet.add_funds(amount, f"Transfer from {self.wallet_id}")
    
    def get_total_transactions(self) -> int:
        """Получение общего количества транзакций"""
        return len(self.transaction_history)
    
    def calculate_monthly_spending(self, month: int, year: int) -> float:
        """Вычисление месячных трат"""
        monthly_debits = [
            t["amount"] for t in self.transaction_history
            if t["type"] == "debit" and t["date"].month == month and t["date"].year == year
        ]
        return sum(monthly_debits)


