"""Класс: Консультант"""
from datetime import datetime
from typing import List


class Consultant:
    """Класс представляющий консультанта"""
    
    def __init__(self, name: str, surname: str, employee_id: str, expertise_area: str, 
                 hire_date: datetime, salary: float, consultations_count: int):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.expertise_area = expertise_area
        self.hire_date = hire_date
        self.salary = salary
        self.consultations_count = consultations_count
        self.success_rate = 0.0
        self.client_satisfaction = 0.0
        self.certifications = []
        
    def provide_consultation(self, client_id: str) -> str:
        """Предоставление консультации"""
        self.consultations_count += 1
        return f"Консультация для клиента {client_id} предоставлена"
    
    def update_success_rate(self, rate: float) -> None:
        """Обновление процента успешности"""
        self.success_rate = rate
    
    def add_certification(self, certification: str) -> None:
        """Добавление сертификата"""
        if certification not in self.certifications:
            self.certifications.append(certification)
    
    def calculate_experience_years(self) -> int:
        """Вычисление лет опыта"""
        today = datetime.now()
        return today.year - self.hire_date.year
    
    def update_client_satisfaction(self, rating: float) -> None:
        """Обновление удовлетворенности клиентов"""
        self.client_satisfaction = (self.client_satisfaction + rating) / 2


