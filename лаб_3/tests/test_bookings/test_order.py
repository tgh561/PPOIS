"""Тесты для класса Order"""
import pytest
from datetime import datetime, timedelta
from Bookings.Order import Order


class TestOrder:
    """Тесты для класса Order"""
    
    @pytest.fixture
    def order(self):
        """Фикстура для создания заказа"""
        return Order(
            order_id="ORD001",
            client_id="ivan@example.com",
            order_date=datetime.now(),
            total_amount=15000.0,
            status="pending",
            items=["ITEM001", "ITEM002"]
        )
    
    def test_init(self, order):
        """Тест инициализации"""
        assert order.order_id == "ORD001"
        assert order.client_id == "ivan@example.com"
        assert order.total_amount == 15000.0
        assert order.status == "pending"
        assert order.items == ["ITEM001", "ITEM002"]
        assert order.shipping_date is None
        assert order.tracking_number is None
        assert order.delivery_address is None
    
    def test_update_status(self, order):
        """Тест обновления статуса заказа"""
        order.update_status("processing")
        assert order.status == "processing"
        
        order.update_status("shipped")
        assert order.status == "shipped"
    
    def test_add_tracking(self, order):
        """Тест добавления номера отслеживания"""
        tracking_number = "TRACK123456"
        order.add_tracking(tracking_number)
        assert order.tracking_number == tracking_number
    
    def test_set_shipping_date(self, order):
        """Тест установки даты отправки"""
        shipping_date = datetime.now() + timedelta(days=2)
        order.set_shipping_date(shipping_date)
        assert order.shipping_date == shipping_date
    
    def test_calculate_days_since_order(self, order):
        """Тест вычисления дней с момента заказа"""
        order.order_date = datetime.now() - timedelta(days=5)
        days = order.calculate_days_since_order()
        assert days == 5
    
    def test_add_delivery_address(self, order):
        """Тест добавления адреса доставки"""
        address = "Санкт-Петербург, ул. Тестовая, д. 10"
        order.add_delivery_address(address)
        assert order.delivery_address == address



