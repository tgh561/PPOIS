"""Тесты для класса InsufficientFundsException"""
import pytest
from Exceptions.InsufficientFundsException import InsufficientFundsException


class TestInsufficientFundsException:
    """Тесты для InsufficientFundsException"""
    
    def test_init_default_message(self):
        """Тест инициализации с сообщением по умолчанию"""
        exception = InsufficientFundsException(100.0, 200.0)
        assert exception.account_balance == 100.0
        assert exception.required_amount == 200.0
        assert "Недостаточно средств" in str(exception)
        assert "100.0" in str(exception)
        assert "200.0" in str(exception)
    
    def test_init_custom_message(self):
        """Тест инициализации с пользовательским сообщением"""
        custom_msg = "Custom insufficient funds message"
        exception = InsufficientFundsException(50.0, 100.0, custom_msg)
        assert exception.message == custom_msg
        assert str(exception) == custom_msg
    
    def test_raise_exception(self):
        """Тест вызова исключения"""
        with pytest.raises(InsufficientFundsException) as exc_info:
            raise InsufficientFundsException(100.0, 200.0)
        assert exc_info.value.account_balance == 100.0
        assert exc_info.value.required_amount == 200.0



