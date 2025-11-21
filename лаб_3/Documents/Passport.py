"""Класс: Паспорт"""
from datetime import datetime
from typing import List, Optional


class Passport:
    """Класс представляющий паспорт"""
    
    def __init__(self, passport_number: str, holder_name: str, surname: str, 
                 birth_date: datetime, nationality: str, issue_date: datetime, 
                 expiry_date: datetime, issuing_authority: str):
        self.passport_number = passport_number
        self.holder_name = holder_name
        self.surname = surname
        self.birth_date = birth_date
        self.nationality = nationality
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.issuing_authority = issuing_authority
        self.visas = []
        self.stamps = []
        self.is_valid = True
        
    def check_validity(self) -> bool:
        """Проверка действительности паспорта"""
        from Exceptions.PassportExpiredException import PassportExpiredException
        today = datetime.now()
        if today > self.expiry_date:
            self.is_valid = False
            raise PassportExpiredException(self.passport_number, str(self.expiry_date))
        return True
    
    def add_visa(self, visa_info: dict) -> None:
        """Добавление визы"""
        self.visas.append(visa_info)
    
    def add_stamp(self, country: str, date: datetime) -> None:
        """Добавление штампа"""
        self.stamps.append({"country": country, "date": date})
    
    def calculate_days_until_expiry(self) -> int:
        """Вычисление дней до истечения"""
        today = datetime.now()
        return (self.expiry_date - today).days
    
    def get_full_name(self) -> str:
        """Получение полного имени"""
        return f"{self.holder_name} {self.surname}"
    
    def is_expiring_soon(self, days_threshold: int = 180) -> bool:
        """Проверка скорого истечения"""
        days_left = self.calculate_days_until_expiry()
        return days_left < days_threshold
    
    def add_visa_object(self, visa) -> None:
        """Добавление объекта визы (ассоциация с Visa)"""
        from Documents.Visa import Visa
        if isinstance(visa, Visa):
            if visa.passport_number == self.passport_number:
                self.visas.append({
                    "visa_number": visa.visa_number,
                    "country": visa.country,
                    "type": visa.visa_type
                })
    
    def link_to_turist(self, turist) -> None:
        """Связь с туристом (ассоциация с Turist)"""
        from Users.Turist import Turist
        if isinstance(turist, Turist):
            if turist.name == self.holder_name and turist.surname == self.surname:
                self.turist_id = turist.email


