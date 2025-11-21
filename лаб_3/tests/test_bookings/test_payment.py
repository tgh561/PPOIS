"""Тесты для класса Payment"""
import pytest
from datetime import datetime
from Bookings.Payment import Payment
from Bookings.Booking import Booking
from Finance.Card import Card
from Finance.Account import Account
from Finance.Transaction import Transaction
from Exceptions.InsufficientFundsException import InsufficientFundsException


class TestPayment:
    """Тесты для класса Payment"""
    
    @pytest.fixture
    def payment(self):
        """Фикстура для создания платежа"""
        return Payment(
            payment_id="P001",
            booking_id="B001",
            amount=1000.0,
            payment_date=datetime.now(),
            payment_method="card",
            card_number="1234567890123456"
        )
    
    def test_init(self, payment):
        """Тест инициализации"""
        assert payment.payment_id == "P001"
        assert payment.booking_id == "B001"
        assert payment.amount == 1000.0
        assert payment.payment_method == "card"
        assert payment.card_number == "1234567890123456"
        assert payment.status == "pending"
        assert payment.refund_amount == 0.0
        assert payment.payment_fee == 0.0
    
    def test_process_payment_success(self, payment):
        """Тест успешной обработки платежа"""
        result = payment.process_payment()
        assert result is True
        assert payment.status == "completed"
    
    def test_process_payment_insufficient_funds(self):
        """Тест обработки платежа при недостатке средств"""
        payment = Payment(
            payment_id="P002",
            booking_id="B002",
            amount=2000.0,
            payment_date=datetime.now(),
            payment_method="card"
        )
        with pytest.raises(InsufficientFundsException):
            payment.process_payment()
    
    def test_process_refund(self, payment):
        """Тест обработки возврата"""
        refund_amount = 800.0
        payment.process_refund(refund_amount)
        assert payment.refund_amount == refund_amount
        assert payment.status == "refunded"
    
    def test_calculate_payment_fee_default(self, payment):
        """Тест вычисления комиссии по умолчанию"""
        fee = payment.calculate_payment_fee()
        expected = 1000.0 * 0.03
        assert fee == expected
        assert payment.payment_fee == expected
    
    def test_calculate_payment_fee_custom(self, payment):
        """Тест вычисления комиссии с кастомным процентом"""
        fee_rate = 0.05
        fee = payment.calculate_payment_fee(fee_rate)
        expected = 1000.0 * fee_rate
        assert fee == expected
    
    def test_get_total_amount(self, payment):
        """Тест получения общей суммы"""
        payment.calculate_payment_fee()
        total = payment.get_total_amount()
        assert total == 1000.0 + payment.payment_fee
    
    def test_is_completed_true(self, payment):
        """Тест проверки завершенности - да"""
        payment.status = "completed"
        assert payment.is_completed() is True
    
    def test_is_completed_false(self, payment):
        """Тест проверки завершенности - нет"""
        assert payment.is_completed() is False
    
    def test_process_with_card_success(self, payment):
        """Тест обработки платежа с картой (ассоциация)"""
        from datetime import timedelta
        card = Card(
            card_number="1234567890123456",
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=2000.0,
            bank_name="Bank"
        )
        payment.calculate_payment_fee()
        payment.process_with_card(card)
        assert payment.status == "completed"
    
    def test_link_to_booking_same_id(self, payment):
        """Тест связи с бронированием - тот же ID"""
        booking = Booking(
            booking_id="B001",
            turist_id="ivan@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now(),
            number_of_people=2,
            total_price=1000.0
        )
        payment.link_to_booking(booking)
        assert booking.payment_status == "paid"
    
    def test_link_to_booking_different_id(self, payment):
        """Тест связи с бронированием - другой ID"""
        booking = Booking(
            booking_id="B002",
            turist_id="ivan@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now(),
            number_of_people=2,
            total_price=1000.0
        )
        payment.link_to_booking(booking)
        assert booking.payment_status == "unpaid"
    
    def test_process_with_account_success(self, payment):
        """Тест обработки с аккаунтом (ассоциация)"""
        account = Account(
            account_id="ACC001",
            account_number="1234567890",
            account_type="checking",
            balance=2000.0,
            currency="USD",
            owner_id="user001",
            opening_date=datetime.now()
        )
        payment.calculate_payment_fee()
        payment.process_with_account(account)
        assert payment.status == "completed"
    
    def test_link_to_transaction_success(self, payment):
        """Тест связи с транзакцией (ассоциация)"""
        transaction = Transaction(
            transaction_id="TXN001",
            transaction_type="payment",
            amount=1000.0,
            source_account="ACC001",
            destination_account="ACC002",
            transaction_date=datetime.now()
        )
        payment.link_to_transaction(transaction)
        assert payment.status == "completed"
        assert payment.transaction_id == "TXN001"



