"""Тесты для класса Invoice"""
import pytest
from datetime import datetime, timedelta
from Bookings.Invoice import Invoice


class TestInvoice:
    """Тесты для класса Invoice"""
    
    @pytest.fixture
    def invoice(self):
        """Фикстура для создания счета"""
        return Invoice(
            invoice_id="INV001",
            booking_id="B001",
            client_name="Иван Иванов",
            invoice_date=datetime.now(),
            due_date=datetime.now() + timedelta(days=30),
            subtotal=10000.0,
            tax_rate=0.1,
            total=11000.0
        )
    
    def test_init(self, invoice):
        """Тест инициализации"""
        assert invoice.invoice_id == "INV001"
        assert invoice.booking_id == "B001"
        assert invoice.client_name == "Иван Иванов"
        assert invoice.subtotal == 10000.0
        assert invoice.tax_rate == 0.1
        assert invoice.total == 11000.0
        assert invoice.status == "unpaid"
        assert isinstance(invoice.items, list)
        assert isinstance(invoice.payments, list)
    
    def test_add_item(self, invoice):
        """Тест добавления позиции в счет"""
        invoice.add_item("Тур в Париж", 1, 10000.0)
        assert len(invoice.items) == 1
        assert invoice.items[0]["description"] == "Тур в Париж"
        assert invoice.items[0]["quantity"] == 1
        assert invoice.items[0]["unit_price"] == 10000.0
        assert invoice.items[0]["total"] == 10000.0
    
    def test_recalculate_totals(self, invoice):
        """Тест пересчета итогов"""
        invoice.add_item("Тур", 1, 5000.0)
        invoice.add_item("Отель", 1, 3000.0)
        
        subtotal = sum(item["total"] for item in invoice.items)
        tax = subtotal * invoice.tax_rate
        expected_total = subtotal + tax
        
        assert invoice.subtotal == subtotal
        assert invoice.total == expected_total
    
    def test_add_payment_partial(self, invoice):
        """Тест добавления частичного платежа"""
        invoice.add_payment(5000.0)
        assert len(invoice.payments) == 1
        assert invoice.status == "unpaid"
    
    def test_add_payment_full(self, invoice):
        """Тест добавления полного платежа"""
        invoice.add_payment(11000.0)
        assert invoice.status == "paid"
    
    def test_add_payment_multiple(self, invoice):
        """Тест добавления нескольких платежей"""
        invoice.add_payment(5000.0)
        assert invoice.status == "unpaid"
        
        invoice.add_payment(6000.0)
        assert invoice.status == "paid"
    
    def test_calculate_tax(self, invoice):
        """Тест вычисления налога"""
        tax = invoice.calculate_tax()
        assert tax == 10000.0 * 0.1
    
    def test_is_overdue_true(self, invoice):
        """Тест проверки просрочки - да"""
        invoice.due_date = datetime.now() - timedelta(days=1)
        invoice.status = "unpaid"
        assert invoice.is_overdue() is True
    
    def test_is_overdue_false_paid(self, invoice):
        """Тест проверки просрочки - нет (оплачено)"""
        invoice.due_date = datetime.now() - timedelta(days=1)
        invoice.status = "paid"
        assert invoice.is_overdue() is False
    
    def test_is_overdue_false_not_due(self, invoice):
        """Тест проверки просрочки - нет (не просрочено)"""
        invoice.due_date = datetime.now() + timedelta(days=1)
        invoice.status = "unpaid"
        assert invoice.is_overdue() is False



