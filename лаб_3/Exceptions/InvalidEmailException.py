"""Исключение: Неверный email"""


class InvalidEmailException(Exception):
    """Вызывается когда email адрес невалиден"""
    
    def __init__(self, email: str, message: str = None):
        self.email = email
        self.message = message or f"Email адрес {email} невалиден"
        super().__init__(self.message)


