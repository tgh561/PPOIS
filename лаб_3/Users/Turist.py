"""Класс: Турист"""
from datetime import datetime
from typing import List
import re


class Turist:
    """Класс представляющий туриста"""
    
    def __init__(self, name: str, surname: str, email: str, phone: str, birth_date: datetime, 
                 password: str, registration_date: datetime, loyalty_points: int = 0):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.password_hash = self._hash_password(password)
        self.registration_date = registration_date
        self.loyalty_points = loyalty_points
        self.is_active = True
        self.preferences = {}
        self.notifications_enabled = True
        
    def _hash_password(self, password: str) -> str:
        """Хеширование пароля"""
        # Упрощенная версия хеширования
        return str(hash(password) % 1000000)
    
    def verify_password(self, password: str) -> bool:
        """Проверка верного пароля"""
        from Exceptions.InvalidPasswordException import InvalidPasswordException
        hashed = self._hash_password(password)
        if hashed != self.password_hash:
            raise InvalidPasswordException()
        return True
    
    def validate_email(self) -> bool:
        """Валидация email адреса"""
        from Exceptions.InvalidEmailException import InvalidEmailException
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            raise InvalidEmailException(self.email)
        return True
    
    def add_loyalty_points(self, points: int) -> None:
        """Добавление бонусных баллов"""
        self.loyalty_points += points
    
    def get_full_name(self) -> str:
        """Получение полного имени"""
        return f"{self.name} {self.surname}"
    
    def calculate_age(self) -> int:
        """Вычисление возраста"""
        today = datetime.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    def assign_passport(self, passport) -> None:
        """Назначение паспорта (ассоциация с Passport)"""
        from Documents.Passport import Passport
        if isinstance(passport, Passport):
            self.passport_number = passport.passport_number
    
    def create_booking(self, booking) -> None:
        """Создание бронирования (ассоциация с Booking)"""
        from Bookings.Booking import Booking
        if isinstance(booking, Booking):
            booking.turist_id = self.email
    
    def add_card(self, card) -> None:
        """Добавление карты (ассоциация с Card)"""
        from Finance.Card import Card
        if isinstance(card, Card):
            self.card_id = card.card_number
    
    def link_to_wallet(self, wallet) -> None:
        """Связь с кошельком (ассоциация с Wallet)"""
        from Finance.Wallet import Wallet
        if isinstance(wallet, Wallet):
            if wallet.owner_id == self.email:
                self.wallet_id = wallet.wallet_id
    
    def assign_insurance(self, insurance) -> None:
        """Назначение страховки (ассоциация с Insurance)"""
        from Documents.Insurance import Insurance
        if isinstance(insurance, Insurance):
            if insurance.holder_name == self.get_full_name():
                self.insurance_policy = insurance.policy_number


