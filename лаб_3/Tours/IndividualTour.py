"""Класс: Индивидуальный тур"""
from datetime import datetime
from typing import List, Optional


class IndividualTour:
    """Класс представляющий индивидуальный тур"""
    
    def __init__(self, tour_id: str, name: str, destination: str, start_date: datetime, 
                 end_date: datetime, base_price: float, participants_count: int, 
                 custom_services: List[str]):
        self.tour_id = tour_id
        self.name = name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.base_price = base_price
        self.participants_count = participants_count
        self.custom_services = custom_services
        self.premium_price_multiplier = 1.5
        self.additional_services = []
        
    def add_custom_service(self, service: str) -> None:
        """Добавление индивидуальной услуги"""
        if service not in self.custom_services:
            self.custom_services.append(service)
    
    def add_additional_service(self, service: str, price: float) -> None:
        """Добавление дополнительной услуги"""
        self.additional_services.append({"service": service, "price": price})
    
    def calculate_total_price(self) -> float:
        """Вычисление общей цены"""
        premium_price = self.base_price * self.premium_price_multiplier
        additional = sum(s["price"] for s in self.additional_services)
        return premium_price * self.participants_count + additional
    
    def get_duration_days(self) -> int:
        """Получение продолжительности"""
        return (self.end_date - self.start_date).days
    
    def customize_itinerary(self, activities: List[str]) -> None:
        """Настройка маршрута"""
        self.custom_services.extend(activities)


