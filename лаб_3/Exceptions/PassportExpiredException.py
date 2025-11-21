"""Исключение: Паспорт истек"""


class PassportExpiredException(Exception):
    """Вызывается когда паспорт истек"""
    
    def __init__(self, passport_number: str, expiry_date: str, message: str = None):
        self.passport_number = passport_number
        self.expiry_date = expiry_date
        self.message = message or f"Паспорт {passport_number} истек. Дата истечения: {expiry_date}"
        super().__init__(self.message)


