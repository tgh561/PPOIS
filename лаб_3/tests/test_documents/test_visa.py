"""Тесты для класса Visa"""
import pytest
from datetime import datetime, timedelta
from Documents.Visa import Visa


class TestVisa:
    """Тесты для класса Visa"""
    
    @pytest.fixture
    def visa(self):
        """Фикстура для создания визы"""
        return Visa(
            visa_number="V001",
            passport_number="123456789",
            country="France",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=90),
            entries_allowed=1,
            current_entries=0
        )
    
    def test_init(self, visa):
        """Тест инициализации"""
        assert visa.visa_number == "V001"
        assert visa.passport_number == "123456789"
        assert visa.country == "France"
        assert visa.visa_type == "tourist"
        assert visa.entries_allowed == 1
        assert visa.current_entries == 0
        assert visa.is_valid is True
        assert visa.purpose == "tourism"
    
    def test_check_validity_success(self, visa):
        """Тест проверки действительности визы - успех"""
        result = visa.check_validity()
        assert result is True
        assert visa.is_valid is True
    
    def test_check_validity_expired(self):
        """Тест проверки просроченной визы"""
        visa = Visa(
            visa_number="V002",
            passport_number="999999999",
            country="Germany",
            visa_type="tourist",
            issue_date=datetime.now() - timedelta(days=100),
            expiry_date=datetime.now() - timedelta(days=1),
            entries_allowed=1
        )
        result = visa.check_validity()
        assert result is False
        assert visa.is_valid is False
    
    def test_check_validity_max_entries(self):
        """Тест проверки визы с максимальным количеством въездов"""
        visa = Visa(
            visa_number="V003",
            passport_number="888888888",
            country="Italy",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=90),
            entries_allowed=2,
            current_entries=2
        )
        result = visa.check_validity()
        assert result is False
        assert visa.is_valid is False
    
    def test_add_entry_success(self, visa):
        """Тест добавления въезда - успех"""
        initial_entries = visa.current_entries
        visa.add_entry()
        assert visa.current_entries == initial_entries + 1
    
    def test_add_entry_max_reached(self):
        """Тест добавления въезда - лимит исчерпан"""
        visa = Visa(
            visa_number="V004",
            passport_number="777777777",
            country="Spain",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=90),
            entries_allowed=1,
            current_entries=1
        )
        with pytest.raises(ValueError, match="Лимит въездов исчерпан"):
            visa.add_entry()
    
    def test_calculate_days_until_expiry(self, visa):
        """Тест вычисления дней до истечения"""
        days = visa.calculate_days_until_expiry()
        assert isinstance(days, int)
        assert days >= 0
    
    def test_get_remaining_entries(self, visa):
        """Тест получения оставшихся въездов"""
        assert visa.get_remaining_entries() == 1
        
        visa.add_entry()
        assert visa.get_remaining_entries() == 0
    
    def test_set_purpose(self, visa):
        """Тест установки цели поездки"""
        visa.set_purpose("business")
        assert visa.purpose == "business"
        
        visa.set_purpose("education")
        assert visa.purpose == "education"
    
    def test_is_multiple_entry_true(self):
        """Тест проверки множественного въезда - да"""
        visa = Visa(
            visa_number="V005",
            passport_number="666666666",
            country="UK",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=180),
            entries_allowed=5
        )
        assert visa.is_multiple_entry() is True
    
    def test_is_multiple_entry_false(self, visa):
        """Тест проверки множественного въезда - нет"""
        assert visa.is_multiple_entry() is False



