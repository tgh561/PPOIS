"""Класс: Город"""
from datetime import datetime
from typing import List, Optional


class City:
    """Класс представляющий город"""
    
    def __init__(self, city_id: str, name: str, country: str, population: int, 
                 timezone: str, language: str, description: str, coordinates: tuple):
        self.city_id = city_id
        self.name = name
        self.country = country
        self.population = population
        self.timezone = timezone
        self.language = language
        self.description = description
        self.coordinates = coordinates
        self.attractions_list = []
        self.hotels_list = []
        self.restaurants_list = []
        self.tourism_rating = 0.0
        
    def add_attraction(self, attraction_id: str) -> None:
        """Добавление достопримечательности"""
        if attraction_id not in self.attractions_list:
            self.attractions_list.append(attraction_id)
    
    def add_hotel(self, hotel_id: str) -> None:
        """Добавление отеля"""
        if hotel_id not in self.hotels_list:
            self.hotels_list.append(hotel_id)
    
    def add_restaurant(self, restaurant_id: str) -> None:
        """Добавление ресторана"""
        if restaurant_id not in self.restaurants_list:
            self.restaurants_list.append(restaurant_id)
    
    def get_total_attractions(self) -> int:
        """Получение общего количества достопримечательностей"""
        return len(self.attractions_list)
    
    def update_tourism_rating(self, rating: float) -> None:
        """Обновление рейтинга туризма"""
        self.tourism_rating = (self.tourism_rating + rating) / 2
    
    def get_city_info(self) -> str:
        """Получение информации о городе"""
        return f"{self.name}, {self.country}, Население: {self.population}"


