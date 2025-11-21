"""Тесты для класса InvalidPasswordException"""
import pytest
from Exceptions.InvalidPasswordException import InvalidPasswordException


class TestInvalidPasswordException:
    """Тесты для InvalidPasswordException"""
    
    def test_init_default_message(self):
        """Тест инициализации с сообщением по умолчанию"""
        exception = InvalidPasswordException()
        assert exception.message == "Неверный пароль"
        assert str(exception) == "Неверный пароль"
    
    def test_init_custom_message(self):
        """Тест инициализации с пользовательским сообщением"""
        custom_msg = "Custom password error"
        exception = InvalidPasswordException(custom_msg)
        assert exception.message == custom_msg
        assert str(exception) == custom_msg
    
    def test_raise_exception(self):
        """Тест вызова исключения"""
        with pytest.raises(InvalidPasswordException) as exc_info:
            raise InvalidPasswordException("Wrong password")
        assert str(exc_info.value) == "Wrong password"



