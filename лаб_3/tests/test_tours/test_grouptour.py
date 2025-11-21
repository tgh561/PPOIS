"""Тесты для класса GroupTour"""
import pytest
from datetime import datetime, timedelta
from Tours.GroupTour import GroupTour


class TestGroupTour:
    """Тесты для класса GroupTour"""
    
    @pytest.fixture
    def group_tour(self):
        """Фикстура для создания группового тура"""
        return GroupTour(
            tour_id="GT001",
            name="Групповой тур в Париж",
            destination="Париж",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price_per_person=45000.0,
            min_group_size=5,
            max_group_size=20
        )
    
    def test_init(self, group_tour):
        """Тест инициализации"""
        assert group_tour.tour_id == "GT001"
        assert group_tour.name == "Групповой тур в Париж"
        assert group_tour.destination == "Париж"
        assert group_tour.price_per_person == 45000.0
        assert group_tour.min_group_size == 5
        assert group_tour.max_group_size == 20
        assert group_tour.current_size == 0
        assert group_tour.group_discount == 0.0
        assert isinstance(group_tour.participants, list)
    
    def test_add_participant_success(self, group_tour):
        """Тест добавления участника - успех"""
        group_tour.add_participant("P001")
        assert group_tour.current_size == 1
        assert "P001" in group_tour.participants
    
    def test_add_participant_full(self, group_tour):
        """Тест добавления участника - переполнен"""
        group_tour.current_size = 20
        group_tour.add_participant("P021")
        # Не добавляется, если переполнен
        assert group_tour.current_size == 20
        assert "P021" not in group_tour.participants
    
    def test_calculate_group_discount_5_participants(self, group_tour):
        """Тест вычисления групповой скидки - 5 участников"""
        for i in range(5):
            group_tour.add_participant(f"P{i+1}")
        assert group_tour.group_discount == 0.05
    
    def test_calculate_group_discount_10_participants(self, group_tour):
        """Тест вычисления групповой скидки - 10 участников"""
        for i in range(10):
            group_tour.add_participant(f"P{i+1}")
        assert group_tour.group_discount == 0.10
    
    def test_calculate_group_discount_15_participants(self, group_tour):
        """Тест вычисления групповой скидки - 15 участников"""
        for i in range(15):
            group_tour.add_participant(f"P{i+1}")
        assert group_tour.group_discount == 0.15
    
    def test_calculate_group_discount_less_than_5(self, group_tour):
        """Тест вычисления групповой скидки - менее 5"""
        group_tour.add_participant("P001")
        assert group_tour.group_discount == 0.0
    
    def test_calculate_total_price_no_discount(self, group_tour):
        """Тест вычисления общей цены - без скидки"""
        group_tour.add_participant("P001")
        total = group_tour.calculate_total_price()
        assert total == 45000.0
    
    def test_calculate_total_price_with_discount(self, group_tour):
        """Тест вычисления общей цены - со скидкой"""
        for i in range(10):
            group_tour.add_participant(f"P{i+1}")
        total = group_tour.calculate_total_price()
        base_total = 10 * 45000.0
        expected = base_total * 0.9
        assert total == expected
    
    def test_is_minimum_met_true(self, group_tour):
        """Тест проверки минимального количества - да"""
        for i in range(5):
            group_tour.add_participant(f"P{i+1}")
        assert group_tour.is_minimum_met() is True
    
    def test_is_minimum_met_false(self, group_tour):
        """Тест проверки минимального количества - нет"""
        group_tour.add_participant("P001")
        assert group_tour.is_minimum_met() is False
    
    def test_get_duration_days(self, group_tour):
        """Тест получения продолжительности в днях"""
        duration = group_tour.get_duration_days()
        assert duration == 6



