"""Тесты для класса Consultant"""
import pytest
from datetime import datetime
from Users.Consultant import Consultant


class TestConsultant:
    """Тесты для класса Consultant"""
    
    @pytest.fixture
    def consultant(self):
        """Фикстура для создания консультанта"""
        return Consultant(
            name="Анна",
            surname="Смирнова",
            employee_id="CON001",
            expertise_area="Туры в Европу",
            hire_date=datetime(2019, 1, 1),
            salary=60000.0,
            consultations_count=0
        )
    
    def test_init(self, consultant):
        """Тест инициализации"""
        assert consultant.name == "Анна"
        assert consultant.surname == "Смирнова"
        assert consultant.employee_id == "CON001"
        assert consultant.expertise_area == "Туры в Европу"
        assert consultant.salary == 60000.0
        assert consultant.consultations_count == 0
        assert consultant.success_rate == 0.0
        assert consultant.client_satisfaction == 0.0
        assert isinstance(consultant.certifications, list)
    
    def test_provide_consultation(self, consultant):
        """Тест предоставления консультации"""
        initial_count = consultant.consultations_count
        result = consultant.provide_consultation("CLIENT001")
        
        assert consultant.consultations_count == initial_count + 1
        assert "Консультация для клиента CLIENT001 предоставлена" in result
    
    def test_update_success_rate(self, consultant):
        """Тест обновления процента успешности"""
        consultant.update_success_rate(85.5)
        assert consultant.success_rate == 85.5
        
        consultant.update_success_rate(90.0)
        assert consultant.success_rate == 90.0
    
    def test_add_certification(self, consultant):
        """Тест добавления сертификата"""
        consultant.add_certification("Сертификат турагента")
        assert "Сертификат турагента" in consultant.certifications
        
        consultant.add_certification("Сертификат менеджера по туризму")
        assert len(consultant.certifications) == 2
    
    def test_add_certification_duplicate(self, consultant):
        """Тест добавления дублирующегося сертификата"""
        consultant.add_certification("Сертификат")
        consultant.add_certification("Сертификат")
        assert consultant.certifications.count("Сертификат") == 1
    
    def test_calculate_experience_years(self, consultant):
        """Тест вычисления лет опыта"""
        years = consultant.calculate_experience_years()
        assert isinstance(years, int)
        assert years >= 0
    
    def test_update_client_satisfaction(self, consultant):
        """Тест обновления удовлетворенности клиентов"""
        consultant.update_client_satisfaction(4.5)
        assert consultant.client_satisfaction == 2.25
        
        consultant.update_client_satisfaction(5.0)
        assert consultant.client_satisfaction == pytest.approx(3.625, rel=0.01)



