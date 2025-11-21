"""Тесты для класса Insurance"""
import pytest
from datetime import datetime, timedelta
from Documents.Insurance import Insurance


class TestInsurance:
    """Тесты для класса Insurance"""
    
    @pytest.fixture
    def insurance(self):
        """Фикстура для создания страховки"""
        return Insurance(
            policy_number="POL001",
            holder_name="Иван Иванов",
            policy_type="travel",
            coverage_amount=50000.0,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=365),
            premium=5000.0,
            insurance_company="Insurance Co"
        )
    
    def test_init(self, insurance):
        """Тест инициализации"""
        assert insurance.policy_number == "POL001"
        assert insurance.holder_name == "Иван Иванов"
        assert insurance.policy_type == "travel"
        assert insurance.coverage_amount == 50000.0
        assert insurance.premium == 5000.0
        assert insurance.insurance_company == "Insurance Co"
        assert insurance.is_active is True
        assert isinstance(insurance.claims, list)
        assert isinstance(insurance.coverage_details, dict)
    
    def test_check_validity_success(self, insurance):
        """Тест проверки действительности страховки - успех"""
        result = insurance.check_validity()
        assert result is True
        assert insurance.is_active is True
    
    def test_check_validity_before_start(self):
        """Тест проверки страховки до начала действия"""
        insurance = Insurance(
            policy_number="POL002",
            holder_name="Test",
            policy_type="travel",
            coverage_amount=10000.0,
            start_date=datetime.now() + timedelta(days=10),
            end_date=datetime.now() + timedelta(days=375),
            premium=1000.0,
            insurance_company="Test Co"
        )
        result = insurance.check_validity()
        assert result is False
        assert insurance.is_active is False
    
    def test_check_validity_expired(self):
        """Тест проверки просроченной страховки"""
        insurance = Insurance(
            policy_number="POL003",
            holder_name="Test",
            policy_type="travel",
            coverage_amount=10000.0,
            start_date=datetime.now() - timedelta(days=400),
            end_date=datetime.now() - timedelta(days=35),
            premium=1000.0,
            insurance_company="Test Co"
        )
        result = insurance.check_validity()
        assert result is False
        assert insurance.is_active is False
    
    def test_add_claim(self, insurance):
        """Тест добавления страхового случая"""
        insurance.add_claim(5000.0, "Медицинские расходы")
        assert len(insurance.claims) == 1
        assert insurance.claims[0]["amount"] == 5000.0
        assert insurance.claims[0]["description"] == "Медицинские расходы"
        
        insurance.add_claim(2000.0, "Отмена поездки")
        assert len(insurance.claims) == 2
    
    def test_calculate_coverage_duration(self, insurance):
        """Тест вычисления продолжительности покрытия"""
        duration = insurance.calculate_coverage_duration()
        assert duration == 365
    
    def test_calculate_total_claims(self, insurance):
        """Тест вычисления общей суммы страховых случаев"""
        assert insurance.calculate_total_claims() == 0.0
        
        insurance.add_claim(5000.0, "Claim 1")
        insurance.add_claim(3000.0, "Claim 2")
        total = insurance.calculate_total_claims()
        assert total == 8000.0
    
    def test_add_coverage_detail(self, insurance):
        """Тест добавления детали покрытия"""
        insurance.add_coverage_detail("Медицина", 30000.0)
        assert insurance.coverage_details["Медицина"] == 30000.0
        
        insurance.add_coverage_detail("Отмена поездки", 20000.0)
        assert len(insurance.coverage_details) == 2
    
    def test_get_total_coverage(self, insurance):
        """Тест получения общего покрытия"""
        base_coverage = insurance.get_total_coverage()
        assert base_coverage == 50000.0
        
        insurance.add_coverage_detail("Медицина", 30000.0)
        total = insurance.get_total_coverage()
        assert total == 80000.0



