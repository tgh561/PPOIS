"""Тесты для класса Passport"""
import pytest
from datetime import datetime, timedelta
from Documents.Passport import Passport
from Documents.Visa import Visa
from Users.Turist import Turist
from Exceptions.PassportExpiredException import PassportExpiredException


class TestPassport:
    """Тесты для класса Passport"""
    
    @pytest.fixture
    def passport(self):
        """Фикстура для создания паспорта"""
        return Passport(
            passport_number="123456789",
            holder_name="Иван",
            surname="Иванов",
            birth_date=datetime(1990, 1, 1),
            nationality="RU",
            issue_date=datetime(2010, 1, 1),
            expiry_date=datetime.now() + timedelta(days=365),
            issuing_authority="МВД"
        )
    
    def test_init(self, passport):
        """Тест инициализации"""
        assert passport.passport_number == "123456789"
        assert passport.holder_name == "Иван"
        assert passport.surname == "Иванов"
        assert passport.nationality == "RU"
        assert passport.issuing_authority == "МВД"
        assert passport.is_valid is True
        assert isinstance(passport.visas, list)
        assert isinstance(passport.stamps, list)
    
    def test_check_validity_success(self, passport):
        """Тест проверки действительности паспорта - успех"""
        result = passport.check_validity()
        assert result is True
        assert passport.is_valid is True
    
    def test_check_validity_expired(self):
        """Тест проверки просроченного паспорта"""
        passport = Passport(
            passport_number="123456789",
            holder_name="Иван",
            surname="Иванов",
            birth_date=datetime(1990, 1, 1),
            nationality="RU",
            issue_date=datetime(2010, 1, 1),
            expiry_date=datetime.now() - timedelta(days=1),
            issuing_authority="МВД"
        )
        with pytest.raises(PassportExpiredException):
            passport.check_validity()
        assert passport.is_valid is False
    
    def test_add_visa(self, passport):
        """Тест добавления визы"""
        visa_info = {"country": "France", "type": "tourist", "number": "V123"}
        passport.add_visa(visa_info)
        assert len(passport.visas) == 1
        assert passport.visas[0] == visa_info
    
    def test_add_stamp(self, passport):
        """Тест добавления штампа"""
        country = "France"
        stamp_date = datetime.now()
        passport.add_stamp(country, stamp_date)
        assert len(passport.stamps) == 1
        assert passport.stamps[0]["country"] == country
        assert passport.stamps[0]["date"] == stamp_date
    
    def test_calculate_days_until_expiry(self, passport):
        """Тест вычисления дней до истечения"""
        days = passport.calculate_days_until_expiry()
        assert isinstance(days, int)
        assert days > 0
    
    def test_get_full_name(self, passport):
        """Тест получения полного имени"""
        full_name = passport.get_full_name()
        assert full_name == "Иван Иванов"
    
    def test_is_expiring_soon_true(self, passport):
        """Тест проверки скорого истечения - да"""
        passport.expiry_date = datetime.now() + timedelta(days=100)
        assert passport.is_expiring_soon(180) is True
    
    def test_is_expiring_soon_false(self, passport):
        """Тест проверки скорого истечения - нет"""
        passport.expiry_date = datetime.now() + timedelta(days=200)
        assert passport.is_expiring_soon(180) is False
    
    def test_add_visa_object_success(self, passport):
        """Тест добавления объекта визы (ассоциация)"""
        visa = Visa(
            visa_number="V001",
            passport_number="123456789",
            country="France",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=90),
            entries_allowed=1
        )
        passport.add_visa_object(visa)
        assert len(passport.visas) == 1
        assert passport.visas[0]["visa_number"] == "V001"
        assert passport.visas[0]["country"] == "France"
    
    def test_add_visa_object_different_passport(self, passport):
        """Тест добавления визы для другого паспорта"""
        visa = Visa(
            visa_number="V001",
            passport_number="999999999",
            country="France",
            visa_type="tourist",
            issue_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=90),
            entries_allowed=1
        )
        initial_count = len(passport.visas)
        passport.add_visa_object(visa)
        assert len(passport.visas) == initial_count
    
    def test_link_to_turist_success(self, passport):
        """Тест связи с туристом (ассоциация)"""
        turist = Turist(
            name="Иван",
            surname="Иванов",
            email="ivan@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        passport.link_to_turist(turist)
        assert passport.turist_id == "ivan@example.com"
    
    def test_link_to_turist_different_name(self, passport):
        """Тест связи с туристом с другим именем"""
        turist = Turist(
            name="Петр",
            surname="Петров",
            email="petr@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        passport.link_to_turist(turist)
        assert not hasattr(passport, 'turist_id') or getattr(passport, 'turist_id', None) != "petr@example.com"



