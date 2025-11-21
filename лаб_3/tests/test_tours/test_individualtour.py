"""Тесты для класса IndividualTour"""
import pytest
from datetime import datetime, timedelta
from Tours.IndividualTour import IndividualTour


class TestIndividualTour:
    """Тесты для класса IndividualTour"""
    
    @pytest.fixture
    def individual_tour(self):
        """Фикстура для создания индивидуального тура"""
        return IndividualTour(
            tour_id="IT001",
            name="Индивидуальный тур в Париж",
            destination="Париж",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 5),
            base_price=80000.0,
            participants_count=2,
            custom_services=["Персональный гид", "VIP трансфер"]
        )
    
    def test_init(self, individual_tour):
        """Тест инициализации"""
        assert individual_tour.tour_id == "IT001"
        assert individual_tour.name == "Индивидуальный тур в Париж"
        assert individual_tour.destination == "Париж"
        assert individual_tour.base_price == 80000.0
        assert individual_tour.participants_count == 2
        assert individual_tour.custom_services == ["Персональный гид", "VIP трансфер"]
        assert individual_tour.premium_price_multiplier == 1.5
        assert isinstance(individual_tour.additional_services, list)
    
    def test_add_custom_service(self, individual_tour):
        """Тест добавления индивидуальной услуги"""
        individual_tour.add_custom_service("Эксклюзивный ресторан")
        assert "Эксклюзивный ресторан" in individual_tour.custom_services
    
    def test_add_custom_service_duplicate(self, individual_tour):
        """Тест добавления дублирующейся услуги"""
        individual_tour.add_custom_service("Новая услуга")
        initial_count = len(individual_tour.custom_services)
        individual_tour.add_custom_service("Новая услуга")
        assert len(individual_tour.custom_services) == initial_count
    
    def test_add_additional_service(self, individual_tour):
        """Тест добавления дополнительной услуги"""
        individual_tour.add_additional_service("Спа-процедуры", 15000.0)
        assert len(individual_tour.additional_services) == 1
        assert individual_tour.additional_services[0]["service"] == "Спа-процедуры"
        assert individual_tour.additional_services[0]["price"] == 15000.0
    
    def test_calculate_total_price(self, individual_tour):
        """Тест вычисления общей цены"""
        individual_tour.add_additional_service("Доп. услуга", 5000.0)
        total = individual_tour.calculate_total_price()
        premium_price = 80000.0 * 1.5
        expected = premium_price * 2 + 5000.0
        assert total == expected
    
    def test_calculate_total_price_no_additional(self, individual_tour):
        """Тест вычисления общей цены без дополнительных услуг"""
        total = individual_tour.calculate_total_price()
        premium_price = 80000.0 * 1.5
        expected = premium_price * 2
        assert total == expected
    
    def test_get_duration_days(self, individual_tour):
        """Тест получения продолжительности"""
        duration = individual_tour.get_duration_days()
        assert duration == 4
    
    def test_customize_itinerary(self, individual_tour):
        """Тест настройки маршрута"""
        initial_count = len(individual_tour.custom_services)
        activities = ["Посещение музея", "Фотосессия"]
        individual_tour.customize_itinerary(activities)
        assert len(individual_tour.custom_services) == initial_count + 2



