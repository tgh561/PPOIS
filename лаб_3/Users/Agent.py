"""Класс: Агент туристической компании"""
from datetime import datetime
from typing import List


class Agent:
    """Класс представляющий агента компании"""
    
    def __init__(self, name: str, surname: str, employee_id: str, hire_date: datetime, 
                 department: str, salary: float, commission_rate: float):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.hire_date = hire_date
        self.department = department
        self.salary = salary
        self.commission_rate = commission_rate
        self.sales_count = 0
        self.total_revenue = 0.0
        self.is_active = True
        self.specializations = []
        
    def calculate_commission(self, sale_amount: float) -> float:
        """Вычисление комиссии от продажи"""
        return sale_amount * self.commission_rate
    
    def add_sale(self, amount: float) -> None:
        """Добавление продажи"""
        self.sales_count += 1
        self.total_revenue += amount
    
    def get_monthly_income(self) -> float:
        """Получение месячного дохода"""
        return self.salary + self.calculate_commission(self.total_revenue)
    
    def calculate_experience_years(self) -> int:
        """Вычисление лет опыта"""
        today = datetime.now()
        return today.year - self.hire_date.year
    
    def add_specialization(self, specialization: str) -> None:
        """Добавление специализации"""
        if specialization not in self.specializations:
            self.specializations.append(specialization)


