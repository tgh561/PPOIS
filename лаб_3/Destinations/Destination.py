"""Класс: Направление"""
from datetime import datetime
from typing import List, Optional


class Destination:
    """Класс представляющий туристическое направление"""
    
    def __init__(self, destination_id: str, name: str, country: str, city: str, 
                 description: str, climate: str, currency: str, visa_required: bool):
        self.destination_id = destination_id
        self.name = name
        self.country = country
        self.city = city
        self.description = description
        self.climate = climate
        self.currency = currency
        self.visa_required = visa_required
        self.popularity_rating = 0.0
        self.attractions = []
        self.hotels = []
        
    def add_attraction(self, attraction_name: str) -> None:
        """Добавление достопримечательности"""
        if attraction_name not in self.attractions:
            self.attractions.append(attraction_name)
    
    def check_visa_requirement(self) -> None:
        """Проверка требования визы"""
        from Exceptions.VisaRequiredException import VisaRequiredException
        if self.visa_required:
            raise VisaRequiredException(self.name)
    
    def add_hotel(self, hotel_name: str) -> None:
        """Добавление отеля"""
        if hotel_name not in self.hotels:
            self.hotels.append(hotel_name)
    
    def update_popularity(self, rating: float) -> None:
        """Обновление рейтинга популярности"""
        self.popularity_rating = (self.popularity_rating + rating) / 2
    
    def get_location_info(self) -> str:
        """Получение информации о местоположении"""
        return f"{self.city}, {self.country}"
    
    def add_hotel_object(self, hotel) -> None:
        """Добавление объекта отеля (ассоциация с Hotel)"""
        from Destinations.Hotel import Hotel
        if isinstance(hotel, Hotel):
            if hotel.location == self.city:
                self.hotels.append(hotel.hotel_id)
    
    def add_attraction_object(self, attraction) -> None:
        """Добавление объекта достопримечательности (ассоциация с Attraction)"""
        from Destinations.Attraction import Attraction
        if isinstance(attraction, Attraction):
            if attraction.location == self.city:
                self.attractions.append(attraction.attraction_id)
    
    def assign_to_city(self, city) -> None:
        """Назначение города (ассоциация с City)"""
        from Destinations.City import City
        if isinstance(city, City):
            self.city = city.name
            self.country = city.country
    
    def link_to_country(self, country) -> None:
        """Связь со страной (ассоциация с Country)"""
        from Destinations.Country import Country
        if isinstance(country, Country):
            self.country = country.name


