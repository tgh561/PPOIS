"""Тесты для класса Booking"""
import pytest
from datetime import datetime, timedelta
from Bookings.Booking import Booking
from Tours.Tour import Tour
from Users.Turist import Turist
from Bookings.Payment import Payment
from Bookings.Invoice import Invoice
from Exceptions.CancellationNotAllowedException import CancellationNotAllowedException


class TestBooking:
    """Тесты для класса Booking"""
    
    @pytest.fixture
    def booking(self):
        """Фикстура для создания бронирования"""
        return Booking(
            booking_id="B001",
            turist_id="ivan@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now() + timedelta(days=30),
            number_of_people=2,
            total_price=10000.0,
            status="pending"
        )
    
    def test_init(self, booking):
        """Тест инициализации"""
        assert booking.booking_id == "B001"
        assert booking.turist_id == "ivan@example.com"
        assert booking.tour_id == "T001"
        assert booking.number_of_people == 2
        assert booking.total_price == 10000.0
        assert booking.status == "pending"
        assert booking.payment_status == "unpaid"
        assert booking.confirmation_number is None
        assert booking.cancellation_date is None
    
    def test_confirm(self, booking):
        """Тест подтверждения бронирования"""
        confirmation_number = "CNF001"
        booking.confirm(confirmation_number)
        assert booking.status == "confirmed"
        assert booking.confirmation_number == confirmation_number
    
    def test_cancel_success(self, booking):
        """Тест успешной отмены бронирования"""
        booking.travel_date = datetime.now() + timedelta(days=10)
        booking.cancel()
        assert booking.status == "cancelled"
        assert booking.cancellation_date is not None
    
    def test_cancel_too_late(self, booking):
        """Тест отмены слишком поздно"""
        booking.travel_date = datetime.now() + timedelta(days=5)
        with pytest.raises(CancellationNotAllowedException):
            booking.cancel()
    
    def test_mark_paid(self, booking):
        """Тест отметки об оплате"""
        booking.mark_paid()
        assert booking.payment_status == "paid"
    
    def test_calculate_refund_paid(self, booking):
        """Тест расчета возврата для оплаченного бронирования"""
        booking.payment_status = "paid"
        cancellation_fee = 0.1
        refund = booking.calculate_refund(cancellation_fee)
        expected = 10000.0 * (1 - cancellation_fee)
        assert refund == expected
    
    def test_calculate_refund_unpaid(self, booking):
        """Тест расчета возврата для неоплаченного бронирования"""
        booking.payment_status = "unpaid"
        refund = booking.calculate_refund(0.1)
        assert refund == 0.0
    
    def test_is_confirmable_true(self, booking):
        """Тест проверки возможности подтверждения - да"""
        booking.status = "pending"
        booking.payment_status = "paid"
        assert booking.is_confirmable() is True
    
    def test_is_confirmable_false_pending(self, booking):
        """Тест проверки возможности подтверждения - нет (не pending)"""
        booking.status = "confirmed"
        booking.payment_status = "paid"
        assert booking.is_confirmable() is False
    
    def test_is_confirmable_false_unpaid(self, booking):
        """Тест проверки возможности подтверждения - нет (не оплачено)"""
        booking.status = "pending"
        booking.payment_status = "unpaid"
        assert booking.is_confirmable() is False
    
    def test_assign_tour(self, booking):
        """Тест назначения тура (ассоциация)"""
        tour = Tour(
            tour_id="T002",
            name="Test Tour",
            description="Description",
            destination="Paris",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price=5000.0,
            max_participants=20
        )
        booking.assign_tour(tour)
        assert booking.tour_id == "T002"
    
    def test_assign_turist(self, booking):
        """Тест назначения туриста (ассоциация)"""
        turist = Turist(
            name="Петр",
            surname="Петров",
            email="petr@example.com",
            phone="+9876543210",
            birth_date=datetime(1985, 5, 15),
            password="password",
            registration_date=datetime.now()
        )
        booking.assign_turist(turist)
        assert booking.turist_id == "petr@example.com"
    
    def test_process_with_payment_completed(self, booking):
        """Тест обработки с завершенным платежом"""
        payment = Payment(
            payment_id="P001",
            booking_id="B001",
            amount=10000.0,
            payment_date=datetime.now(),
            payment_method="card"
        )
        payment.status = "completed"
        booking.process_with_payment(payment)
        assert booking.payment_status == "paid"
    
    def test_process_with_payment_pending(self, booking):
        """Тест обработки с незавершенным платежом"""
        payment = Payment(
            payment_id="P001",
            booking_id="B001",
            amount=10000.0,
            payment_date=datetime.now(),
            payment_method="card"
        )
        payment.status = "pending"
        booking.process_with_payment(payment)
        assert booking.payment_status == "unpaid"
    
    def test_link_to_invoice_paid(self, booking):
        """Тест связи со счетом (оплачено)"""
        invoice = Invoice(
            invoice_id="INV001",
            booking_id="B001",
            client_name="Иван Иванов",
            invoice_date=datetime.now(),
            due_date=datetime.now() + timedelta(days=30),
            subtotal=10000.0,
            tax_rate=0.1,
            total=11000.0
        )
        booking.payment_status = "paid"
        booking.link_to_invoice(invoice)
        assert invoice.status == "paid"
    
    def test_link_to_invoice_unpaid(self, booking):
        """Тест связи со счетом (не оплачено)"""
        invoice = Invoice(
            invoice_id="INV001",
            booking_id="B001",
            client_name="Иван Иванов",
            invoice_date=datetime.now(),
            due_date=datetime.now() + timedelta(days=30),
            subtotal=10000.0,
            tax_rate=0.1,
            total=11000.0
        )
        booking.payment_status = "unpaid"
        booking.link_to_invoice(invoice)
        assert invoice.status == "unpaid"



