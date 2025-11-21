"""Тесты для класса Card"""
import pytest
from datetime import datetime, timedelta
from Finance.Card import Card
from Exceptions.InsufficientFundsException import InsufficientFundsException
from Exceptions.CardNotFoundException import CardNotFoundException
from Exceptions.InvalidCardNumberException import InvalidCardNumberException


class TestCard:
    """Тесты для класса Card"""
    
    @pytest.fixture
    def card(self):
        """Фикстура для создания карты"""
        return Card(
            card_number="1234567890123456",
            cardholder_name="Иван Иванов",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Test Bank"
        )
    
    def test_init(self, card):
        """Тест инициализации"""
        assert card.card_number == "1234567890123456"
        assert card.cardholder_name == "Иван Иванов"
        assert card.card_type == "Visa"
        assert card.balance == 1000.0
        assert card.bank_name == "Test Bank"
        assert card.is_active is True
        assert card.daily_limit == 10000.0
        assert isinstance(card.transaction_history, list)
    
    def test_validate_card_number_valid(self, card):
        """Тест валидации валидного номера карты"""
        result = card.validate_card_number()
        assert result is True
    
    def test_validate_card_number_invalid_short(self):
        """Тест валидации слишком короткого номера карты"""
        card = Card(
            card_number="12345",
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        with pytest.raises(InvalidCardNumberException):
            card.validate_card_number()
    
    def test_validate_card_number_invalid_long(self):
        """Тест валидации слишком длинного номера карты"""
        card = Card(
            card_number="1" * 25,
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        with pytest.raises(InvalidCardNumberException):
            card.validate_card_number()
    
    def test_check_expiry_valid(self, card):
        """Тест проверки действительной карты"""
        assert card.check_expiry() is True
    
    def test_check_expiry_expired(self):
        """Тест проверки просроченной карты"""
        card = Card(
            card_number="1234567890123456",
            cardholder_name="Test",
            expiry_date=datetime.now() - timedelta(days=1),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        assert card.check_expiry() is False
    
    def test_verify_card_active(self, card):
        """Тест проверки активной карты"""
        result = card.verify_card()
        assert result is True
    
    def test_verify_card_inactive(self):
        """Тест проверки неактивной карты"""
        card = Card(
            card_number="1234567890123456",
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        card.is_active = False
        with pytest.raises(CardNotFoundException):
            card.verify_card()
    
    def test_deduct_amount_success(self, card):
        """Тест успешного списания средств"""
        initial_balance = card.balance
        amount = 200.0
        card.deduct_amount(amount)
        assert card.balance == initial_balance - amount
        assert len(card.transaction_history) == 1
        assert card.transaction_history[0]["type"] == "debit"
        assert card.transaction_history[0]["amount"] == amount
    
    def test_deduct_amount_insufficient_funds(self, card):
        """Тест списания при недостатке средств"""
        with pytest.raises(InsufficientFundsException):
            card.deduct_amount(2000.0)
    
    def test_add_amount(self, card):
        """Тест пополнения карты"""
        initial_balance = card.balance
        amount = 500.0
        card.add_amount(amount)
        assert card.balance == initial_balance + amount
        assert len(card.transaction_history) == 1
        assert card.transaction_history[0]["type"] == "credit"
        assert card.transaction_history[0]["amount"] == amount
    
    def test_transfer_to_card_success(self, card):
        """Тест перевода денег с одной карты на другую"""
        target_card = Card(
            card_number="6543210987654321",
            cardholder_name="Петр Петров",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="456",
            card_type="MasterCard",
            balance=500.0,
            bank_name="Bank"
        )
        
        initial_balance_card1 = card.balance
        initial_balance_card2 = target_card.balance
        transfer_amount = 200.0
        
        card.transfer_to_card(target_card, transfer_amount)
        
        assert card.balance == initial_balance_card1 - transfer_amount
        assert target_card.balance == initial_balance_card2 + transfer_amount
    
    def test_transfer_to_card_insufficient_funds(self, card):
        """Тест перевода при недостатке средств"""
        target_card = Card(
            card_number="6543210987654321",
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="456",
            card_type="MasterCard",
            balance=500.0,
            bank_name="Bank"
        )
        
        with pytest.raises(InsufficientFundsException):
            card.transfer_to_card(target_card, 2000.0)
    
    def test_get_balance(self, card):
        """Тест получения баланса"""
        assert card.get_balance() == 1000.0
        card.add_amount(100.0)
        assert card.get_balance() == 1100.0
    
    def test_transaction_history(self, card):
        """Тест истории транзакций"""
        assert len(card.transaction_history) == 0
        
        card.add_amount(100.0)
        assert len(card.transaction_history) == 1
        
        card.deduct_amount(50.0)
        assert len(card.transaction_history) == 2
        
        assert card.transaction_history[0]["type"] == "credit"
        assert card.transaction_history[1]["type"] == "debit"



