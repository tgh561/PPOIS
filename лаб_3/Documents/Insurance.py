"""Класс: Страховка"""
from datetime import datetime
from typing import List, Optional


class Insurance:
    """Класс представляющий страховой полис"""
    
    def __init__(self, policy_number: str, holder_name: str, policy_type: str, 
                 coverage_amount: float, start_date: datetime, end_date: datetime, 
                 premium: float, insurance_company: str):
        self.policy_number = policy_number
        self.holder_name = holder_name
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
        self.start_date = start_date
        self.end_date = end_date
        self.premium = premium
        self.insurance_company = insurance_company
        self.is_active = True
        self.claims = []
        self.coverage_details = {}
        
    def check_validity(self) -> bool:
        """Проверка действительности страховки"""
        today = datetime.now()
        if today < self.start_date or today > self.end_date:
            self.is_active = False
            return False
        return True
    
    def add_claim(self, claim_amount: float, description: str) -> None:
        """Добавление страхового случая"""
        self.claims.append({
            "amount": claim_amount,
            "description": description,
            "date": datetime.now()
        })
    
    def calculate_coverage_duration(self) -> int:
        """Вычисление продолжительности покрытия в днях"""
        return (self.end_date - self.start_date).days
    
    def calculate_total_claims(self) -> float:
        """Вычисление общей суммы страховых случаев"""
        return sum(claim["amount"] for claim in self.claims)
    
    def add_coverage_detail(self, detail_name: str, amount: float) -> None:
        """Добавление детали покрытия"""
        self.coverage_details[detail_name] = amount
    
    def get_total_coverage(self) -> float:
        """Получение общего покрытия"""
        return self.coverage_amount + sum(self.coverage_details.values())


