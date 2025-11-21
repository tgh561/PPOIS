"""Исключение: Неверный номер карты"""


class InvalidCardNumberException(Exception):
    """Вызывается когда номер карты невалиден"""
    
    def __init__(self, card_number: str, message: str = None):
        self.card_number = card_number
        self.message = message or f"Номер карты {card_number} невалиден"
        super().__init__(self.message)


