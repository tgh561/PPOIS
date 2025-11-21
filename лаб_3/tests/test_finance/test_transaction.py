"""Тесты для класса Transaction"""
import pytest
from datetime import datetime
from Finance.Transaction import Transaction
from Exceptions.InsufficientFundsException import InsufficientFundsException


class TestTransaction:
    """Тесты для класса Transaction"""
    
    @pytest.fixture
    def transaction(self):
        """Фикстура для создания транзакции"""
        return Transaction(
            transaction_id="TXN001",
            transaction_type="transfer",
            amount=500.0,
            source_account="ACC001",
            destination_account="ACC002",
            transaction_date=datetime.now(),
            status="pending",
            description="Payment for booking"
        )
    
    def test_init(self, transaction):
        """Тест инициализации"""
        assert transaction.transaction_id == "TXN001"
        assert transaction.transaction_type == "transfer"
        assert transaction.amount == 500.0
        assert transaction.source_account == "ACC001"
        assert transaction.destination_account == "ACC002"
        assert transaction.status == "pending"
        assert transaction.description == "Payment for booking"
        assert transaction.fee == 0.0
        assert transaction.exchange_rate == 1.0
    
    def test_process_transaction_success(self, transaction):
        """Тест успешной обработки транзакции"""
        result = transaction.process_transaction()
        assert result is True
        assert transaction.status == "completed"
    
    def test_process_transaction_insufficient_funds(self):
        """Тест обработки транзакции при недостатке средств"""
        transaction = Transaction(
            transaction_id="TXN002",
            transaction_type="transfer",
            amount=2000.0,
            source_account="ACC001",
            destination_account="ACC002",
            transaction_date=datetime.now()
        )
        with pytest.raises(InsufficientFundsException):
            transaction.process_transaction()
    
    def test_calculate_fee_default(self, transaction):
        """Тест вычисления комиссии по умолчанию"""
        fee = transaction.calculate_fee()
        expected = 500.0 * 0.02
        assert fee == expected
        assert transaction.fee == expected
    
    def test_calculate_fee_custom(self, transaction):
        """Тест вычисления комиссии с кастомным процентом"""
        fee_rate = 0.05
        fee = transaction.calculate_fee(fee_rate)
        expected = 500.0 * fee_rate
        assert fee == expected
    
    def test_get_total_amount(self, transaction):
        """Тест получения общей суммы"""
        transaction.calculate_fee()
        total = transaction.get_total_amount()
        assert total == 500.0 + transaction.fee
    
    def test_cancel_transaction(self, transaction):
        """Тест отмены транзакции"""
        transaction.cancel_transaction()
        assert transaction.status == "cancelled"
    
    def test_convert_currency(self, transaction):
        """Тест конвертации валюты"""
        exchange_rate = 0.85  # EUR to USD
        converted = transaction.convert_currency(exchange_rate)
        assert transaction.exchange_rate == exchange_rate
        assert converted == 500.0 * exchange_rate
    
    def test_is_completed_true(self, transaction):
        """Тест проверки завершенности - да"""
        transaction.status = "completed"
        assert transaction.is_completed() is True
    
    def test_is_completed_false(self, transaction):
        """Тест проверки завершенности - нет"""
        assert transaction.is_completed() is False
        
        transaction.status = "pending"
        assert transaction.is_completed() is False



