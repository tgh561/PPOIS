"""Исключение: Отель переполнен"""


class HotelFullException(Exception):
    """Вызывается когда в отеле нет свободных номеров"""
    
    def __init__(self, hotel_name: str, check_in_date: str, message: str = None):
        self.hotel_name = hotel_name
        self.check_in_date = check_in_date
        self.message = message or f"Отель '{hotel_name}' переполнен на дату {check_in_date}"
        super().__init__(self.message)


