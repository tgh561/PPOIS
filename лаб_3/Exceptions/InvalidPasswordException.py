"""Исключение: Неверный пароль"""


class InvalidPasswordException(Exception):
    """Вызывается когда введен неверный пароль"""
    
    def __init__(self, message: str = "Неверный пароль"):
        self.message = message
        super().__init__(self.message)


