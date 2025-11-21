"""Исключение: Требуется виза"""


class VisaRequiredException(Exception):
    """Вызывается когда для направления требуется виза"""
    
    def __init__(self, destination: str, message: str = None):
        self.destination = destination
        self.message = message or f"Для направления {destination} требуется виза"
        super().__init__(self.message)


