"""Класс: Страна"""
from datetime import datetime
from typing import List, Optional


class Country:
    """Класс представляющий страну"""
    
    def __init__(self, country_id: str, name: str, capital: str, population: int, 
                 currency: str, language: str, visa_required: bool, description: str):
        self.country_id = country_id
        self.name = name
        self.capital = capital
        self.population = population
        self.currency = currency
        self.language = language
        self.visa_required = visa_required
        self.description = description
        self.cities = []
        self.tourist_seasons = []
        self.safety_rating = 0.0
        
    def add_city(self, city_id: str) -> None:
        """Добавление города"""
        if city_id not in self.cities:
            self.cities.append(city_id)
    
    def add_tourist_season(self, season: str) -> None:
        """Добавление туристического сезона"""
        if season not in self.tourist_seasons:
            self.tourist_seasons.append(season)
    
    def check_visa_requirement(self) -> None:
        """Проверка требования визы"""
        from Exceptions.VisaRequiredException import VisaRequiredException
        if self.visa_required:
            raise VisaRequiredException(self.name)
    
    def update_safety_rating(self, rating: float) -> None:
        """Обновление рейтинга безопасности"""
        self.safety_rating = (self.safety_rating + rating) / 2
    
    def get_country_info(self) -> str:
        """Получение информации о стране"""
        return f"{self.name}, Столица: {self.capital}, Валюта: {self.currency}"
    
    def get_total_cities(self) -> int:
        """Получение общего количества городов"""
        return len(self.cities)


