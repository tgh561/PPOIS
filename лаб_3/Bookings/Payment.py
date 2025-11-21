"""Класс: Платеж"""
from datetime import datetime
from typing import List, Optional


class Payment:
    """Класс представляющий платеж"""
    
    def __init__(self, payment_id: str, booking_id: str, amount: float, payment_date: datetime, 
                 payment_method: str, card_number: str = None, transaction_id: str = None):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.card_number = card_number
        self.transaction_id = transaction_id
        self.status = "pending"
        self.refund_amount = 0.0
        self.payment_fee = 0.0
        
    def process_payment(self) -> bool:
        """Обработка платежа"""
        from Exceptions.InsufficientFundsException import InsufficientFundsException
        # Имитация проверки баланса
        account_balance = 1000.0
        if account_balance < self.amount + self.payment_fee:
            raise InsufficientFundsException(account_balance, self.amount + self.payment_fee)
        self.status = "completed"
        return True
    
    def process_refund(self, refund_amount: float) -> None:
        """Обработка возврата"""
        self.refund_amount = refund_amount
        self.status = "refunded"
    
    def calculate_payment_fee(self, fee_rate: float = 0.03) -> float:
        """Вычисление комиссии за платеж"""
        self.payment_fee = self.amount * fee_rate
        return self.payment_fee
    
    def get_total_amount(self) -> float:
        """Получение общей суммы"""
        return self.amount + self.payment_fee
    
    def is_completed(self) -> bool:
        """Проверка завершенности"""
        return self.status == "completed"
    
    def process_with_card(self, card) -> None:
        """Обработка платежа с картой (ассоциация с Card)"""
        from Finance.Card import Card
        if isinstance(card, Card):
            card.verify_card()
            card.deduct_amount(self.amount + self.payment_fee)
            self.status = "completed"
    
    def link_to_booking(self, booking) -> None:
        """Связь с бронированием (ассоциация с Booking)"""
        from Bookings.Booking import Booking
        if isinstance(booking, Booking):
            if booking.booking_id == self.booking_id:
                booking.mark_paid()
    
    def process_with_account(self, account) -> None:
        """Обработка с аккаунтом (ассоциация с Account)"""
        from Finance.Account import Account
        if isinstance(account, Account):
            account.withdraw(self.amount + self.payment_fee)
            self.status = "completed"
    
    def link_to_transaction(self, transaction) -> None:
        """Связь с транзакцией (ассоциация с Transaction)"""
        from Finance.Transaction import Transaction
        if isinstance(transaction, Transaction):
            if transaction.process_transaction():
                self.status = "completed"
                self.transaction_id = transaction.transaction_id


