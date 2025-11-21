"""Класс: Менеджер"""
from datetime import datetime
from typing import List


class Manager:
    """Класс представляющий менеджера"""
    
    def __init__(self, name: str, surname: str, employee_id: str, position: str, 
                 hire_date: datetime, salary: float, department: str):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.position = position
        self.hire_date = hire_date
        self.salary = salary
        self.department = department
        self.subordinates = []
        self.projects = []
        self.performance_rating = 0.0
        
    def add_subordinate(self, employee_id: str) -> None:
        """Добавление подчиненного"""
        if employee_id not in self.subordinates:
            self.subordinates.append(employee_id)
    
    def remove_subordinate(self, employee_id: str) -> None:
        """Удаление подчиненного"""
        if employee_id in self.subordinates:
            self.subordinates.remove(employee_id)
    
    def assign_project(self, project_name: str) -> None:
        """Назначение проекта"""
        if project_name not in self.projects:
            self.projects.append(project_name)
    
    def calculate_team_size(self) -> int:
        """Вычисление размера команды"""
        return len(self.subordinates)
    
    def update_performance_rating(self, rating: float) -> None:
        """Обновление рейтинга производительности"""
        self.performance_rating = rating


