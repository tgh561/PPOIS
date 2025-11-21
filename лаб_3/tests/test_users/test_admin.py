"""Тесты для класса Admin"""
import pytest
from datetime import datetime
from Users.Admin import Admin
from Exceptions.InvalidPasswordException import InvalidPasswordException


class TestAdmin:
    """Тесты для класса Admin"""
    
    @pytest.fixture
    def admin(self):
        """Фикстура для создания администратора"""
        password_hash = str(hash("admin123") % 1000000)
        return Admin(
            name="Админ",
            surname="Админов",
            admin_id="ADM001",
            email="admin@example.com",
            password_hash=password_hash,
            access_level="super",
            creation_date=datetime.now()
        )
    
    def test_init(self, admin):
        """Тест инициализации"""
        assert admin.name == "Админ"
        assert admin.surname == "Админов"
        assert admin.admin_id == "ADM001"
        assert admin.email == "admin@example.com"
        assert admin.access_level == "super"
        assert admin.last_login is None
        assert isinstance(admin.permissions, list)
        assert admin.login_attempts == 0
        assert admin.is_active is True
    
    def test_verify_password_correct(self, admin):
        """Тест проверки верного пароля"""
        result = admin.verify_password("admin123")
        assert result is True
    
    def test_verify_password_incorrect(self, admin):
        """Тест проверки неверного пароля"""
        with pytest.raises(InvalidPasswordException):
            admin.verify_password("wrong_password")
    
    def test_add_permission(self, admin):
        """Тест добавления разрешения"""
        admin.add_permission("read_users")
        assert "read_users" in admin.permissions
        
        admin.add_permission("write_users")
        assert len(admin.permissions) == 2
    
    def test_add_permission_duplicate(self, admin):
        """Тест добавления дублирующегося разрешения"""
        admin.add_permission("read_users")
        admin.add_permission("read_users")
        assert admin.permissions.count("read_users") == 1
    
    def test_remove_permission(self, admin):
        """Тест удаления разрешения"""
        admin.add_permission("read_users")
        admin.remove_permission("read_users")
        assert "read_users" not in admin.permissions
    
    def test_remove_permission_not_exists(self, admin):
        """Тест удаления несуществующего разрешения"""
        admin.remove_permission("nonexistent")
        assert len(admin.permissions) == 0
    
    def test_has_permission_true(self, admin):
        """Тест проверки наличия разрешения - да"""
        admin.add_permission("read_users")
        assert admin.has_permission("read_users") is True
    
    def test_has_permission_false(self, admin):
        """Тест проверки наличия разрешения - нет"""
        assert admin.has_permission("read_users") is False
    
    def test_update_last_login(self, admin):
        """Тест обновления времени последнего входа"""
        assert admin.last_login is None
        admin.update_last_login()
        assert admin.last_login is not None
        assert isinstance(admin.last_login, datetime)



