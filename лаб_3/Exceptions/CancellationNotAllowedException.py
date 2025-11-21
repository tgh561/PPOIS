"""Исключение: Отмена не разрешена"""


class CancellationNotAllowedException(Exception):
    """Вызывается когда отмена бронирования не разрешена"""
    
    def __init__(self, booking_id: str, reason: str = None, message: str = None):
        self.booking_id = booking_id
        self.reason = reason
        self.message = message or f"Отмена бронирования {booking_id} не разрешена. Причина: {reason or 'Слишком близко к дате отправления'}"
        super().__init__(self.message)


