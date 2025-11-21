"""Тесты для класса Accountant"""
import pytest
from datetime import datetime
from Users.Accountant import Accountant


class TestAccountant:
    """Тесты для класса Accountant"""
    
    @pytest.fixture
    def accountant(self):
        """Фикстура для создания бухгалтера"""
        return Accountant(
            name="Елена",
            surname="Козлова",
            employee_id="ACC001",
            certification="CPA",
            hire_date=datetime(2017, 1, 1),
            salary=65000.0,
            department="Finance"
        )
    
    def test_init(self, accountant):
        """Тест инициализации"""
        assert accountant.name == "Елена"
        assert accountant.surname == "Козлова"
        assert accountant.employee_id == "ACC001"
        assert accountant.certification == "CPA"
        assert accountant.salary == 65000.0
        assert accountant.department == "Finance"
        assert accountant.processed_transactions == 0
        assert accountant.reports_generated == 0
        assert isinstance(accountant.specializations, list)
    
    def test_process_transaction(self, accountant):
        """Тест обработки транзакции"""
        initial_count = accountant.processed_transactions
        accountant.process_transaction(1000.0)
        assert accountant.processed_transactions == initial_count + 1
        
        accountant.process_transaction(2000.0)
        assert accountant.processed_transactions == initial_count + 2
    
    def test_generate_report(self, accountant):
        """Тест генерации отчета"""
        initial_count = accountant.reports_generated
        result = accountant.generate_report("monthly")
        
        assert accountant.reports_generated == initial_count + 1
        assert "Отчет типа monthly сгенерирован" in result
    
    def test_calculate_tax(self, accountant):
        """Тест вычисления налога"""
        amount = 10000.0
        tax_rate = 0.13
        tax = accountant.calculate_tax(amount, tax_rate)
        assert tax == 10000.0 * 0.13
    
    def test_verify_balance_true(self, accountant):
        """Тест проверки баланса - совпадает"""
        assert accountant.verify_balance(1000.0, 1000.0) is True
        assert accountant.verify_balance(1000.0, 1000.005) is True
    
    def test_verify_balance_false(self, accountant):
        """Тест проверки баланса - не совпадает"""
        assert accountant.verify_balance(1000.0, 1000.1) is False
        assert accountant.verify_balance(1000.0, 999.9) is False
    
    def test_add_specialization(self, accountant):
        """Тест добавления специализации"""
        accountant.add_specialization("Налоговое планирование")
        assert "Налоговое планирование" in accountant.specializations
        
        accountant.add_specialization("Финансовая отчетность")
        assert len(accountant.specializations) == 2
    
    def test_add_specialization_duplicate(self, accountant):
        """Тест добавления дублирующейся специализации"""
        accountant.add_specialization("Налоги")
        accountant.add_specialization("Налоги")
        assert accountant.specializations.count("Налоги") == 1



