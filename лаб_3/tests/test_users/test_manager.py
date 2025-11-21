"""Тесты для класса Manager"""
import pytest
from datetime import datetime
from Users.Manager import Manager


class TestManager:
    """Тесты для класса Manager"""
    
    @pytest.fixture
    def manager(self):
        """Фикстура для создания менеджера"""
        return Manager(
            name="Александр",
            surname="Смирнов",
            employee_id="MGR001",
            position="Менеджер по продажам",
            hire_date=datetime(2018, 1, 1),
            salary=70000.0,
            department="Sales"
        )
    
    def test_init(self, manager):
        """Тест инициализации"""
        assert manager.name == "Александр"
        assert manager.surname == "Смирнов"
        assert manager.employee_id == "MGR001"
        assert manager.position == "Менеджер по продажам"
        assert manager.salary == 70000.0
        assert manager.department == "Sales"
        assert isinstance(manager.subordinates, list)
        assert isinstance(manager.projects, list)
        assert manager.performance_rating == 0.0
    
    def test_add_subordinate(self, manager):
        """Тест добавления подчиненного"""
        manager.add_subordinate("EMP001")
        assert "EMP001" in manager.subordinates
        
        manager.add_subordinate("EMP002")
        assert len(manager.subordinates) == 2
    
    def test_add_subordinate_duplicate(self, manager):
        """Тест добавления дублирующегося подчиненного"""
        manager.add_subordinate("EMP001")
        manager.add_subordinate("EMP001")
        assert manager.subordinates.count("EMP001") == 1
    
    def test_remove_subordinate(self, manager):
        """Тест удаления подчиненного"""
        manager.add_subordinate("EMP001")
        manager.remove_subordinate("EMP001")
        assert "EMP001" not in manager.subordinates
    
    def test_remove_subordinate_not_exists(self, manager):
        """Тест удаления несуществующего подчиненного"""
        manager.remove_subordinate("EMP999")
        assert len(manager.subordinates) == 0
    
    def test_assign_project(self, manager):
        """Тест назначения проекта"""
        manager.assign_project("Проект А")
        assert "Проект А" in manager.projects
        
        manager.assign_project("Проект Б")
        assert len(manager.projects) == 2
    
    def test_assign_project_duplicate(self, manager):
        """Тест назначения дублирующегося проекта"""
        manager.assign_project("Проект А")
        manager.assign_project("Проект А")
        assert manager.projects.count("Проект А") == 1
    
    def test_calculate_team_size(self, manager):
        """Тест вычисления размера команды"""
        assert manager.calculate_team_size() == 0
        
        manager.add_subordinate("EMP001")
        assert manager.calculate_team_size() == 1
        
        manager.add_subordinate("EMP002")
        assert manager.calculate_team_size() == 2
    
    def test_update_performance_rating(self, manager):
        """Тест обновления рейтинга производительности"""
        manager.update_performance_rating(4.5)
        assert manager.performance_rating == 4.5
        
        manager.update_performance_rating(5.0)
        assert manager.performance_rating == 5.0



