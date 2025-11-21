"""Тесты для класса Turist"""
import pytest
from datetime import datetime
from Users.Turist import Turist
from Documents.Passport import Passport
from Bookings.Booking import Booking
from Finance.Card import Card
from Finance.Wallet import Wallet
from Documents.Insurance import Insurance
from Exceptions.InvalidPasswordException import InvalidPasswordException
from Exceptions.InvalidEmailException import InvalidEmailException


class TestTurist:
    """Тесты для класса Turist"""
    
    @pytest.fixture
    def turist(self):
        """Фикстура для создания туриста"""
        return Turist(
            name="Иван",
            surname="Иванов",
            email="ivan@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password123",
            registration_date=datetime.now(),
            loyalty_points=0
        )
    
    def test_init(self, turist):
        """Тест инициализации"""
        assert turist.name == "Иван"
        assert turist.surname == "Иванов"
        assert turist.email == "ivan@example.com"
        assert turist.phone == "+1234567890"
        assert turist.loyalty_points == 0
        assert turist.is_active is True
        assert turist.notifications_enabled is True
        assert isinstance(turist.password_hash, str)
    
    def test_verify_password_correct(self, turist):
        """Тест проверки верного пароля"""
        result = turist.verify_password("password123")
        assert result is True
    
    def test_verify_password_incorrect(self, turist):
        """Тест проверки неверного пароля"""
        with pytest.raises(InvalidPasswordException):
            turist.verify_password("wrong_password")
    
    def test_validate_email_valid(self, turist):
        """Тест валидации валидного email"""
        result = turist.validate_email()
        assert result is True
    
    def test_validate_email_invalid(self):
        """Тест валидации невалидного email"""
        turist = Turist(
            name="Test",
            surname="Test",
            email="invalid-email",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        with pytest.raises(InvalidEmailException):
            turist.validate_email()
    
    def test_add_loyalty_points(self, turist):
        """Тест добавления бонусных баллов"""
        initial_points = turist.loyalty_points
        turist.add_loyalty_points(100)
        assert turist.loyalty_points == initial_points + 100
        
        turist.add_loyalty_points(50)
        assert turist.loyalty_points == initial_points + 150
    
    def test_get_full_name(self, turist):
        """Тест получения полного имени"""
        assert turist.get_full_name() == "Иван Иванов"
    
    def test_calculate_age(self, turist):
        """Тест вычисления возраста"""
        age = turist.calculate_age()
        assert isinstance(age, int)
        assert age > 0
    
    def test_assign_passport(self, turist):
        """Тест назначения паспорта (ассоциация)"""
        passport = Passport(
            passport_number="123456789",
            holder_name="Иван",
            surname="Иванов",
            birth_date=datetime(1990, 1, 1),
            nationality="RU",
            issue_date=datetime(2010, 1, 1),
            expiry_date=datetime(2030, 1, 1),
            issuing_authority="МВД"
        )
        turist.assign_passport(passport)
        assert turist.passport_number == "123456789"
    
    def test_create_booking(self, turist):
        """Тест создания бронирования (ассоциация)"""
        booking = Booking(
            booking_id="B001",
            turist_id="",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime(2024, 6, 1),
            number_of_people=2,
            total_price=10000.0
        )
        turist.create_booking(booking)
        assert booking.turist_id == turist.email
    
    def test_add_card(self, turist):
        """Тест добавления карты (ассоциация)"""
        card = Card(
            card_number="1234567890123456",
            cardholder_name="Иван Иванов",
            expiry_date=datetime(2025, 12, 31),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        turist.add_card(card)
        assert turist.card_id == "1234567890123456"
    
    def test_link_to_wallet(self, turist):
        """Тест связи с кошельком (ассоциация)"""
        wallet = Wallet(
            wallet_id="W001",
            owner_id=turist.email,
            currency="USD",
            balance=500.0,
            creation_date=datetime.now()
        )
        turist.link_to_wallet(wallet)
        assert turist.wallet_id == "W001"
    
    def test_assign_insurance(self, turist):
        """Тест назначения страховки (ассоциация)"""
        insurance = Insurance(
            policy_number="POL001",
            holder_name=turist.get_full_name(),
            policy_type="travel",
            coverage_amount=10000.0,
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31),
            premium=500.0,
            insurance_company="Insurance Co"
        )
        turist.assign_insurance(insurance)
        assert turist.insurance_policy == "POL001"
    
    def test_hash_password(self, turist):
        """Тест хеширования пароля"""
        hash1 = turist._hash_password("test")
        hash2 = turist._hash_password("test")
        assert hash1 == hash2
        assert isinstance(hash1, str)



