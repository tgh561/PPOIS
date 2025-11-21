"""Класс: Администратор"""
from datetime import datetime
from typing import List


class Admin:
    """Класс представляющий администратора системы"""
    
    def __init__(self, name: str, surname: str, admin_id: str, email: str, 
                 password_hash: str, access_level: str, creation_date: datetime):
        self.name = name
        self.surname = surname
        self.admin_id = admin_id
        self.email = email
        self.password_hash = password_hash
        self.access_level = access_level
        self.creation_date = creation_date
        self.last_login = None
        self.permissions = []
        self.login_attempts = 0
        self.is_active = True
        
    def verify_password(self, password: str) -> bool:
        """Проверка пароля"""
        from Exceptions.InvalidPasswordException import InvalidPasswordException
        hashed = str(hash(password) % 1000000)
        if hashed != self.password_hash:
            raise InvalidPasswordException()
        return True
    
    def add_permission(self, permission: str) -> None:
        """Добавление разрешения"""
        if permission not in self.permissions:
            self.permissions.append(permission)
    
    def remove_permission(self, permission: str) -> None:
        """Удаление разрешения"""
        if permission in self.permissions:
            self.permissions.remove(permission)
    
    def has_permission(self, permission: str) -> bool:
        """Проверка наличия разрешения"""
        return permission in self.permissions
    
    def update_last_login(self) -> None:
        """Обновление времени последнего входа"""
        self.last_login = datetime.now()


