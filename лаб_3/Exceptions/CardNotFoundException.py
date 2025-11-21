"""Исключение: Карта не найдена"""


class CardNotFoundException(Exception):
    """Вызывается когда банковская карта не найдена"""
    
    def __init__(self, card_number: str, message: str = None):
        self.card_number = card_number
        self.message = message or f"Карта с номером {card_number} не найдена"
        super().__init__(self.message)


