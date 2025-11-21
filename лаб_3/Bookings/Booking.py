"""Класс: Бронирование"""
from datetime import datetime
from typing import List, Optional


class Booking:
    """Класс представляющий бронирование"""
    
    def __init__(self, booking_id: str, turist_id: str, tour_id: str, booking_date: datetime, 
                 travel_date: datetime, number_of_people: int, total_price: float, 
                 status: str = "pending"):
        self.booking_id = booking_id
        self.turist_id = turist_id
        self.tour_id = tour_id
        self.booking_date = booking_date
        self.travel_date = travel_date
        self.number_of_people = number_of_people
        self.total_price = total_price
        self.status = status
        self.payment_status = "unpaid"
        self.confirmation_number = None
        self.cancellation_date = None
        
    def confirm(self, confirmation_number: str) -> None:
        """Подтверждение бронирования"""
        self.status = "confirmed"
        self.confirmation_number = confirmation_number
    
    def cancel(self) -> None:
        """Отмена бронирования"""
        from Exceptions.CancellationNotAllowedException import CancellationNotAllowedException
        days_until_travel = (self.travel_date - datetime.now()).days
        if days_until_travel < 7:
            raise CancellationNotAllowedException(self.booking_id, "Менее 7 дней до поездки")
        self.status = "cancelled"
        self.cancellation_date = datetime.now()
    
    def mark_paid(self) -> None:
        """Отметка об оплате"""
        self.payment_status = "paid"
    
    def calculate_refund(self, cancellation_fee: float) -> float:
        """Вычисление суммы возврата"""
        if self.payment_status == "paid":
            return self.total_price * (1 - cancellation_fee)
        return 0.0
    
    def is_confirmable(self) -> bool:
        """Проверка возможности подтверждения"""
        return self.status == "pending" and self.payment_status == "paid"
    
    def assign_tour(self, tour) -> None:
        """Назначение тура (ассоциация с Tour)"""
        from Tours.Tour import Tour
        if isinstance(tour, Tour):
            self.tour_id = tour.tour_id
    
    def assign_turist(self, turist) -> None:
        """Назначение туриста (ассоциация с Turist)"""
        from Users.Turist import Turist
        if isinstance(turist, Turist):
            self.turist_id = turist.email
    
    def process_with_payment(self, payment) -> None:
        """Обработка с платежом (ассоциация с Payment)"""
        from Bookings.Payment import Payment
        if isinstance(payment, Payment):
            if payment.is_completed():
                self.mark_paid()
    
    def link_to_invoice(self, invoice) -> None:
        """Связь со счетом (ассоциация с Invoice)"""
        from Bookings.Invoice import Invoice
        if isinstance(invoice, Invoice):
            if invoice.booking_id == self.booking_id:
                invoice.status = "paid" if self.payment_status == "paid" else "unpaid"


