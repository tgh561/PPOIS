"""Тесты для класса Checkout"""
import pytest
from datetime import datetime
from Bookings.Checkout import Checkout


class TestCheckout:
    """Тесты для класса Checkout"""
    
    @pytest.fixture
    def checkout(self):
        """Фикстура для создания оформления заказа"""
        return Checkout(
            checkout_id="CHK001",
            turist_id="ivan@example.com",
            booking_items=["ITEM001", "ITEM002"],
            total_amount=20000.0,
            checkout_date=datetime.now(),
            discount_code="DISCOUNT10"
        )
    
    def test_init(self, checkout):
        """Тест инициализации"""
        assert checkout.checkout_id == "CHK001"
        assert checkout.turist_id == "ivan@example.com"
        assert checkout.booking_items == ["ITEM001", "ITEM002"]
        assert checkout.total_amount == 20000.0
        assert checkout.discount_code == "DISCOUNT10"
        assert checkout.discount_amount == 0.0
        assert checkout.final_amount == 20000.0
        assert checkout.status == "in_progress"
        assert checkout.shipping_address is None
    
    def test_apply_discount(self, checkout):
        """Тест применения скидки"""
        discount_rate = 0.1
        checkout.apply_discount(discount_rate)
        assert checkout.discount_amount == 20000.0 * 0.1
        assert checkout.final_amount == 20000.0 * 0.9
    
    def test_add_shipping_address(self, checkout):
        """Тест добавления адреса доставки"""
        address = "Москва, ул. Примерная, д. 1"
        checkout.add_shipping_address(address)
        assert checkout.shipping_address == address
    
    def test_complete_checkout(self, checkout):
        """Тест завершения оформления"""
        result = checkout.complete_checkout()
        assert checkout.status == "completed"
        assert "Оформление CHK001 завершено" in result
    
    def test_calculate_final_total(self, checkout):
        """Тест вычисления финальной суммы"""
        total = checkout.calculate_final_total()
        assert total == 20000.0
        
        checkout.apply_discount(0.1)
        total = checkout.calculate_final_total()
        assert total == 20000.0 * 0.9
    
    def test_add_item(self, checkout):
        """Тест добавления позиции"""
        initial_total = checkout.total_amount
        initial_count = len(checkout.booking_items)
        
        checkout.add_item("ITEM003", 5000.0)
        assert len(checkout.booking_items) == initial_count + 1
        assert checkout.total_amount == initial_total + 5000.0
        assert checkout.final_amount == (initial_total + 5000.0) - checkout.discount_amount



