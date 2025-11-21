"""Класс: Бухгалтер"""
from datetime import datetime
from typing import List


class Accountant:
    """Класс представляющий бухгалтера"""
    
    def __init__(self, name: str, surname: str, employee_id: str, certification: str, 
                 hire_date: datetime, salary: float, department: str):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.certification = certification
        self.hire_date = hire_date
        self.salary = salary
        self.department = department
        self.processed_transactions = 0
        self.reports_generated = 0
        self.specializations = []
        
    def process_transaction(self, amount: float) -> None:
        """Обработка транзакции"""
        self.processed_transactions += 1
    
    def generate_report(self, report_type: str) -> str:
        """Генерация отчета"""
        self.reports_generated += 1
        return f"Отчет типа {report_type} сгенерирован"
    
    def calculate_tax(self, amount: float, tax_rate: float) -> float:
        """Вычисление налога"""
        return amount * tax_rate
    
    def verify_balance(self, expected: float, actual: float) -> bool:
        """Проверка баланса"""
        return abs(expected - actual) < 0.01
    
    def add_specialization(self, specialization: str) -> None:
        """Добавление специализации"""
        if specialization not in self.specializations:
            self.specializations.append(specialization)


