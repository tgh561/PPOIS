"""Тесты для класса CulturalTour"""
import pytest
from datetime import datetime, timedelta
from Tours.CulturalTour import CulturalTour


class TestCulturalTour:
    """Тесты для класса CulturalTour"""
    
    @pytest.fixture
    def cultural_tour(self):
        """Фикстура для создания культурного тура"""
        return CulturalTour(
            tour_id="CT001",
            name="Культурный тур по Парижу",
            city="Париж",
            start_date=datetime(2024, 6, 1),
            duration_days=5,
            price=55000.0,
            max_participants=15,
            languages=["Русский", "Английский"]
        )
    
    def test_init(self, cultural_tour):
        """Тест инициализации"""
        assert cultural_tour.tour_id == "CT001"
        assert cultural_tour.name == "Культурный тур по Парижу"
        assert cultural_tour.city == "Париж"
        assert cultural_tour.duration_days == 5
        assert cultural_tour.price == 55000.0
        assert cultural_tour.max_participants == 15
        assert cultural_tour.languages == ["Русский", "Английский"]
        assert cultural_tour.current_participants == 0
        assert isinstance(cultural_tour.museums_visited, list)
        assert isinstance(cultural_tour.cultural_sites, list)
    
    def test_add_museum(self, cultural_tour):
        """Тест добавления музея в маршрут"""
        cultural_tour.add_museum("Лувр")
        assert "Лувр" in cultural_tour.museums_visited
        
        cultural_tour.add_museum("Музей Орсе")
        assert len(cultural_tour.museums_visited) == 2
    
    def test_add_museum_duplicate(self, cultural_tour):
        """Тест добавления дублирующегося музея"""
        cultural_tour.add_museum("Лувр")
        cultural_tour.add_museum("Лувр")
        assert cultural_tour.museums_visited.count("Лувр") == 1
    
    def test_add_cultural_site(self, cultural_tour):
        """Тест добавления культурного объекта"""
        cultural_tour.add_cultural_site("Эйфелева башня")
        assert "Эйфелева башня" in cultural_tour.cultural_sites
        
        cultural_tour.add_cultural_site("Нотр-Дам")
        assert len(cultural_tour.cultural_sites) == 2
    
    def test_add_cultural_site_duplicate(self, cultural_tour):
        """Тест добавления дублирующегося культурного объекта"""
        cultural_tour.add_cultural_site("Сайт")
        cultural_tour.add_cultural_site("Сайт")
        assert cultural_tour.cultural_sites.count("Сайт") == 1
    
    def test_add_participant_success(self, cultural_tour):
        """Тест добавления участника - успех"""
        initial_count = cultural_tour.current_participants
        cultural_tour.add_participant()
        assert cultural_tour.current_participants == initial_count + 1
    
    def test_add_participant_full(self, cultural_tour):
        """Тест добавления участника - переполнен"""
        cultural_tour.current_participants = 15
        initial_count = cultural_tour.current_participants
        cultural_tour.add_participant()
        assert cultural_tour.current_participants == initial_count
    
    def test_calculate_revenue(self, cultural_tour):
        """Тест вычисления выручки"""
        cultural_tour.add_participant()
        cultural_tour.add_participant()
        revenue = cultural_tour.calculate_revenue()
        assert revenue == 2 * 55000.0
    
    def test_get_total_sites(self, cultural_tour):
        """Тест получения общего количества мест"""
        cultural_tour.add_museum("Музей 1")
        cultural_tour.add_cultural_site("Сайт 1")
        total = cultural_tour.get_total_sites()
        assert total == 2
