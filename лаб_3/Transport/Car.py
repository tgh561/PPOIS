"""Класс: Автомобиль"""
from datetime import datetime
from typing import List, Optional


class Car:
    """Класс представляющий автомобиль для аренды"""
    
    def __init__(self, car_id: str, make: str, model: str, year: int, 
                 license_plate: str, rental_price_per_day: float, fuel_type: str, 
                 seats: int, mileage: float):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.rental_price_per_day = rental_price_per_day
        self.fuel_type = fuel_type
        self.seats = seats
        self.mileage = mileage
        self.is_available = True
        self.current_renter = None
        self.insurance_included = False
        self.fuel_consumption = 0.0
        
    def rent_car(self, renter_id: str, start_date: datetime, end_date: datetime) -> float:
        """Аренда автомобиля"""
        if not self.is_available:
            raise ValueError("Автомобиль недоступен")
        self.is_available = False
        self.current_renter = renter_id
        days = (end_date - start_date).days
        return self.rental_price_per_day * days
    
    def return_car(self, new_mileage: float) -> None:
        """Возврат автомобиля"""
        self.is_available = True
        self.mileage = new_mileage
        self.current_renter = None
    
    def calculate_rental_cost(self, days: int) -> float:
        """Вычисление стоимости аренды"""
        return self.rental_price_per_day * days
    
    def add_insurance(self) -> None:
        """Добавление страховки"""
        self.insurance_included = True
    
    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """Вычисление стоимости топлива"""
        return (distance / 100) * self.fuel_consumption * fuel_price
    
    def set_fuel_consumption(self, consumption: float) -> None:
        """Установка расхода топлива"""
        self.fuel_consumption = consumption


