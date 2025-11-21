"""Класс: Культурный тур"""
from datetime import datetime
from typing import List, Optional


class CulturalTour:
    """Класс представляющий культурный тур"""
    
    def __init__(self, tour_id: str, name: str, city: str, start_date: datetime, 
                 duration_days: int, price: float, max_participants: int, 
                 languages: List[str]):
        self.tour_id = tour_id
        self.name = name
        self.city = city
        self.start_date = start_date
        self.duration_days = duration_days
        self.price = price
        self.max_participants = max_participants
        self.languages = languages
        self.current_participants = 0
        self.museums_visited = []
        self.cultural_sites = []
        
    def add_museum(self, museum_name: str) -> None:
        """Добавление музея в маршрут"""
        if museum_name not in self.museums_visited:
            self.museums_visited.append(museum_name)
    
    def add_cultural_site(self, site_name: str) -> None:
        """Добавление культурного объекта"""
        if site_name not in self.cultural_sites:
            self.cultural_sites.append(site_name)
    
    def add_participant(self) -> None:
        """Добавление участника"""
        if self.current_participants < self.max_participants:
            self.current_participants += 1
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.current_participants * self.price
    
    def get_total_sites(self) -> int:
        """Получение общего количества мест"""
        return len(self.museums_visited) + len(self.cultural_sites)


