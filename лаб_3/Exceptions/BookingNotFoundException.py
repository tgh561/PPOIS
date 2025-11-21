"""Исключение: Бронирование не найдено"""


class BookingNotFoundException(Exception):
    """Вызывается когда бронирование не найдено"""
    
    def __init__(self, booking_id: str, message: str = None):
        self.booking_id = booking_id
        self.message = message or f"Бронирование с ID {booking_id} не найдено"
        super().__init__(self.message)


