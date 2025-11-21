"""Тесты для класса Agent"""
import pytest
from datetime import datetime, timedelta
from Users.Agent import Agent


class TestAgent:
    """Тесты для класса Agent"""
    
    @pytest.fixture
    def agent(self):
        """Фикстура для создания агента"""
        return Agent(
            name="Иван",
            surname="Иванов",
            employee_id="AG001",
            hire_date=datetime(2020, 1, 1),
            department="Sales",
            salary=50000.0,
            commission_rate=0.05
        )
    
    def test_init(self, agent):
        """Тест инициализации"""
        assert agent.name == "Иван"
        assert agent.surname == "Иванов"
        assert agent.employee_id == "AG001"
        assert agent.department == "Sales"
        assert agent.salary == 50000.0
        assert agent.commission_rate == 0.05
        assert agent.sales_count == 0
        assert agent.total_revenue == 0.0
        assert agent.is_active is True
        assert isinstance(agent.specializations, list)
    
    def test_calculate_commission(self, agent):
        """Тест вычисления комиссии"""
        sale_amount = 100000.0
        commission = agent.calculate_commission(sale_amount)
        assert commission == 100000.0 * 0.05
    
    def test_add_sale(self, agent):
        """Тест добавления продажи"""
        initial_count = agent.sales_count
        initial_revenue = agent.total_revenue
        
        agent.add_sale(50000.0)
        assert agent.sales_count == initial_count + 1
        assert agent.total_revenue == initial_revenue + 50000.0
        
        agent.add_sale(30000.0)
        assert agent.sales_count == initial_count + 2
        assert agent.total_revenue == initial_revenue + 80000.0
    
    def test_get_monthly_income(self, agent):
        """Тест получения месячного дохода"""
        agent.add_sale(100000.0)
        monthly_income = agent.get_monthly_income()
        expected = 50000.0 + (100000.0 * 0.05)
        assert monthly_income == expected
    
    def test_calculate_experience_years(self, agent):
        """Тест вычисления лет опыта"""
        years = agent.calculate_experience_years()
        assert isinstance(years, int)
        assert years >= 0
    
    def test_add_specialization(self, agent):
        """Тест добавления специализации"""
        agent.add_specialization("Туры в Европу")
        assert "Туры в Европу" in agent.specializations
        
        agent.add_specialization("Экскурсионные туры")
        assert len(agent.specializations) == 2
    
    def test_add_specialization_duplicate(self, agent):
        """Тест добавления дублирующейся специализации"""
        agent.add_specialization("Туры в Европу")
        agent.add_specialization("Туры в Европу")
        assert agent.specializations.count("Туры в Европу") == 1



