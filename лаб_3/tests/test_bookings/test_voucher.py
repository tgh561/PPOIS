"""Тесты для класса Voucher"""
import pytest
from datetime import datetime, timedelta
from Bookings.Voucher import Voucher


class TestVoucher:
    """Тесты для класса Voucher"""
    
    @pytest.fixture
    def voucher(self):
        """Фикстура для создания ваучера"""
        return Voucher(
            voucher_id="VOU001",
            booking_id="B001",
            voucher_code="DISCOUNT10",
            discount_amount=1000.0,
            valid_from=datetime.now(),
            valid_until=datetime.now() + timedelta(days=30),
            is_used=False
        )
    
    def test_init(self, voucher):
        """Тест инициализации"""
        assert voucher.voucher_id == "VOU001"
        assert voucher.booking_id == "B001"
        assert voucher.voucher_code == "DISCOUNT10"
        assert voucher.discount_amount == 1000.0
        assert voucher.is_used is False
        assert voucher.used_date is None
        assert voucher.discount_percentage == 0.0
    
    def test_validate_voucher_valid(self, voucher):
        """Тест валидации валидного ваучера"""
        result = voucher.validate_voucher()
        assert result is True
    
    def test_validate_voucher_used(self, voucher):
        """Тест валидации использованного ваучера"""
        voucher.is_used = True
        result = voucher.validate_voucher()
        assert result is False
    
    def test_validate_voucher_expired(self):
        """Тест валидации просроченного ваучера"""
        voucher = Voucher(
            voucher_id="VOU002",
            booking_id="B002",
            voucher_code="EXPIRED",
            discount_amount=500.0,
            valid_from=datetime.now() - timedelta(days=60),
            valid_until=datetime.now() - timedelta(days=30),
            is_used=False
        )
        result = voucher.validate_voucher()
        assert result is False
    
    def test_validate_voucher_not_started(self):
        """Тест валидации ваучера до начала действия"""
        voucher = Voucher(
            voucher_id="VOU003",
            booking_id="B003",
            voucher_code="FUTURE",
            discount_amount=500.0,
            valid_from=datetime.now() + timedelta(days=10),
            valid_until=datetime.now() + timedelta(days=40),
            is_used=False
        )
        result = voucher.validate_voucher()
        assert result is False
    
    def test_use_voucher_success(self, voucher):
        """Тест успешного использования ваучера"""
        voucher.use_voucher()
        assert voucher.is_used is True
        assert voucher.used_date is not None
    
    def test_use_voucher_invalid(self):
        """Тест использования невалидного ваучера"""
        voucher = Voucher(
            voucher_id="VOU004",
            booking_id="B004",
            voucher_code="INVALID",
            discount_amount=500.0,
            valid_from=datetime.now(),
            valid_until=datetime.now() + timedelta(days=30),
            is_used=True  # Уже использован
        )
        with pytest.raises(ValueError, match="Ваучер недействителен"):
            voucher.use_voucher()
    
    def test_calculate_discount_fixed_amount(self, voucher):
        """Тест вычисления скидки - фиксированная сумма"""
        total_amount = 10000.0
        discount = voucher.calculate_discount(total_amount)
        assert discount == 1000.0
    
    def test_calculate_discount_percentage(self, voucher):
        """Тест вычисления скидки - процентная"""
        voucher.set_percentage_discount(15.0)
        total_amount = 10000.0
        discount = voucher.calculate_discount(total_amount)
        assert discount == 10000.0 * 0.15
    
    def test_set_percentage_discount(self, voucher):
        """Тест установки процентной скидки"""
        voucher.set_percentage_discount(20.0)
        assert voucher.discount_percentage == 20.0
    
    def test_is_expired_false(self, voucher):
        """Тест проверки истечения - нет"""
        assert voucher.is_expired() is False
    
    def test_is_expired_true(self):
        """Тест проверки истечения - да"""
        voucher = Voucher(
            voucher_id="VOU005",
            booking_id="B005",
            voucher_code="EXPIRED",
            discount_amount=500.0,
            valid_from=datetime.now() - timedelta(days=60),
            valid_until=datetime.now() - timedelta(days=1),
            is_used=False
        )
        assert voucher.is_expired() is True



