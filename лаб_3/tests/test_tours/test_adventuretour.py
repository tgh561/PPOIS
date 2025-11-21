"""Тесты для класса AdventureTour"""
import pytest
from datetime import datetime, timedelta
from Tours.AdventureTour import AdventureTour


class TestAdventureTour:
    """Тесты для класса AdventureTour"""
    
    @pytest.fixture
    def adventure_tour(self):
        """Фикстура для создания приключенческого тура"""
        return AdventureTour(
            tour_id="AT001",
            name="Горный поход",
            location="Альпы",
            difficulty_level="hard",
            start_date=datetime(2024, 7, 1),
            duration_days=5,
            price=60000.0,
            min_age=18
        )
    
    def test_init(self, adventure_tour):
        """Тест инициализации"""
        assert adventure_tour.tour_id == "AT001"
        assert adventure_tour.name == "Горный поход"
        assert adventure_tour.location == "Альпы"
        assert adventure_tour.difficulty_level == "hard"
        assert adventure_tour.duration_days == 5
        assert adventure_tour.price == 60000.0
        assert adventure_tour.min_age == 18
        assert adventure_tour.max_participants == 15
        assert adventure_tour.current_participants == 0
        assert adventure_tour.safety_rating == 5.0
        assert isinstance(adventure_tour.equipment_required, list)
    
    def test_add_equipment(self, adventure_tour):
        """Тест добавления необходимого оборудования"""
        adventure_tour.add_equipment("Спальный мешок")
        assert "Спальный мешок" in adventure_tour.equipment_required
        
        adventure_tour.add_equipment("Палатка")
        assert len(adventure_tour.equipment_required) == 2
    
    def test_add_equipment_duplicate(self, adventure_tour):
        """Тест добавления дублирующегося оборудования"""
        adventure_tour.add_equipment("Оборудование")
        initial_count = len(adventure_tour.equipment_required)
        adventure_tour.add_equipment("Оборудование")
        assert len(adventure_tour.equipment_required) == initial_count
    
    def test_check_age_requirement_valid(self, adventure_tour):
        """Тест проверки возрастного требования - валидно"""
        assert adventure_tour.check_age_requirement(18) is True
        assert adventure_tour.check_age_requirement(25) is True
    
    def test_check_age_requirement_invalid(self, adventure_tour):
        """Тест проверки возрастного требования - невалидно"""
        assert adventure_tour.check_age_requirement(17) is False
        assert adventure_tour.check_age_requirement(15) is False
    
    def test_add_participant_success(self, adventure_tour):
        """Тест добавления участника - успех"""
        initial_count = adventure_tour.current_participants
        adventure_tour.add_participant(20)
        assert adventure_tour.current_participants == initial_count + 1
    
    def test_add_participant_age_invalid(self, adventure_tour):
        """Тест добавления участника - невалидный возраст"""
        with pytest.raises(ValueError, match="Минимальный возраст: 18"):
            adventure_tour.add_participant(16)
    
    def test_add_participant_full(self, adventure_tour):
        """Тест добавления участника - переполнен"""
        adventure_tour.current_participants = 15
        initial_count = adventure_tour.current_participants
        adventure_tour.add_participant(20)
        # Не добавляется, если переполнен
        assert adventure_tour.current_participants == initial_count
    
    def test_calculate_revenue(self, adventure_tour):
        """Тест вычисления выручки"""
        adventure_tour.add_participant(20)
        adventure_tour.add_participant(25)
        revenue = adventure_tour.calculate_revenue()
        assert revenue == 2 * 60000.0
    
    def test_update_safety_rating(self, adventure_tour):
        """Тест обновления рейтинга безопасности"""
        initial_rating = adventure_tour.safety_rating
        adventure_tour.update_safety_rating(4.5)
        assert adventure_tour.safety_rating == (initial_rating + 4.5) / 2



