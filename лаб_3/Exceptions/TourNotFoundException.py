"""Исключение: Тур не найден"""


class TourNotFoundException(Exception):
    """Вызывается когда тур не найден в системе"""
    
    def __init__(self, tour_id: str, message: str = None):
        self.tour_id = tour_id
        self.message = message or f"Тур с ID {tour_id} не найден"
        super().__init__(self.message)


