"""Исключение: Тур переполнен"""


class TourFullException(Exception):
    """Вызывается когда в туре нет свободных мест"""
    
    def __init__(self, tour_name: str, message: str = None):
        self.tour_name = tour_name
        self.message = message or f"Тур '{tour_name}' переполнен, нет свободных мест"
        super().__init__(self.message)


