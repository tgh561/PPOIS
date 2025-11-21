"""Тесты для класса Cancellation"""
import pytest
from datetime import datetime, timedelta
from Bookings.Cancellation import Cancellation
from Exceptions.CancellationNotAllowedException import CancellationNotAllowedException


class TestCancellation:
    """Тесты для класса Cancellation"""
    
    @pytest.fixture
    def cancellation(self):
        """Фикстура для создания отмены"""
        return Cancellation(
            cancellation_id="CANC001",
            booking_id="B001",
            cancellation_date=datetime.now() + timedelta(days=10),
            reason="Изменение планов",
            refund_amount=8000.0,
            cancellation_fee=0.1
        )
    
    def test_init(self, cancellation):
        """Тест инициализации"""
        assert cancellation.cancellation_id == "CANC001"
        assert cancellation.booking_id == "B001"
        assert cancellation.reason == "Изменение планов"
        assert cancellation.refund_amount == 8000.0
        assert cancellation.cancellation_fee == 0.1
        assert cancellation.status == "pending"
        assert cancellation.processed_date is None
        assert cancellation.refund_processed is False
    
    def test_process_cancellation_success(self, cancellation):
        """Тест успешной обработки отмены"""
        cancellation.process_cancellation()
        assert cancellation.status == "processed"
        assert cancellation.processed_date is not None
    
    def test_process_cancellation_too_late(self):
        """Тест обработки отмены слишком поздно"""
        cancellation = Cancellation(
            cancellation_id="CANC002",
            booking_id="B002",
            cancellation_date=datetime.now() - timedelta(days=1),
            reason="Too late",
            refund_amount=0.0,
            cancellation_fee=0.1
        )
        with pytest.raises(CancellationNotAllowedException):
            cancellation.process_cancellation()
    
    def test_process_refund(self, cancellation):
        """Тест обработки возврата средств"""
        cancellation.process_refund()
        assert cancellation.refund_processed is True
    
    def test_calculate_total_refund(self, cancellation):
        """Тест вычисления общей суммы возврата"""
        total_refund = cancellation.calculate_total_refund()
        # refund_amount - cancellation_fee (cancellation_fee это сумма)
        expected = 8000.0 - 0.1
        assert abs(total_refund - expected) < 0.01
    
    def test_approve_cancellation(self, cancellation):
        """Тест одобрения отмены"""
        cancellation.approve_cancellation()
        assert cancellation.status == "approved"
    
    def test_is_eligible_for_full_refund_true(self, cancellation):
        """Тест проверки права на полный возврат - да"""
        assert cancellation.is_eligible_for_full_refund(30) is True
        assert cancellation.is_eligible_for_full_refund(40) is True
    
    def test_is_eligible_for_full_refund_false(self, cancellation):
        """Тест проверки права на полный возврат - нет"""
        assert cancellation.is_eligible_for_full_refund(29) is False
        assert cancellation.is_eligible_for_full_refund(15) is False

