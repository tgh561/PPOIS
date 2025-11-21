"""Тесты для класса Account"""
import pytest
from datetime import datetime, timedelta
from Finance.Account import Account
from Finance.Bank import Bank
from Finance.Card import Card
from Exceptions.InsufficientFundsException import InsufficientFundsException


class TestAccount:
    """Тесты для класса Account"""
    
    @pytest.fixture
    def account(self):
        """Фикстура для создания счета"""
        return Account(
            account_id="ACC001",
            account_number="1234567890",
            account_type="checking",
            balance=1000.0,
            currency="USD",
            owner_id="user001",
            opening_date=datetime.now(),
            interest_rate=2.5
        )
    
    def test_init(self, account):
        """Тест инициализации"""
        assert account.account_id == "ACC001"
        assert account.account_number == "1234567890"
        assert account.account_type == "checking"
        assert account.balance == 1000.0
        assert account.currency == "USD"
        assert account.owner_id == "user001"
        assert account.interest_rate == 2.5
        assert account.is_active is True
        assert account.overdraft_limit == 0.0
        assert isinstance(account.transactions, list)
    
    def test_deposit_success(self, account):
        """Тест успешного пополнения"""
        initial_balance = account.balance
        amount = 500.0
        account.deposit(amount)
        assert account.balance == initial_balance + amount
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "deposit"
        assert account.transactions[0]["amount"] == amount
    
    def test_deposit_invalid_amount_zero(self, account):
        """Тест пополнения нулевой суммой"""
        with pytest.raises(ValueError, match="Сумма должна быть положительной"):
            account.deposit(0.0)
    
    def test_deposit_invalid_amount_negative(self, account):
        """Тест пополнения отрицательной суммой"""
        with pytest.raises(ValueError, match="Сумма должна быть положительной"):
            account.deposit(-100.0)
    
    def test_withdraw_success(self, account):
        """Тест успешного снятия"""
        initial_balance = account.balance
        amount = 300.0
        account.withdraw(amount)
        assert account.balance == initial_balance - amount
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "withdrawal"
    
    def test_withdraw_insufficient_funds(self, account):
        """Тест снятия при недостатке средств"""
        with pytest.raises(InsufficientFundsException):
            account.withdraw(2000.0)
    
    def test_withdraw_with_overdraft(self, account):
        """Тест снятия с использованием овердрафта"""
        account.overdraft_limit = 500.0
        initial_balance = account.balance
        amount = 1200.0
        account.withdraw(amount)
        assert account.balance == initial_balance - amount
    
    def test_transfer_to_account_success(self, account):
        """Тест перевода на другой счет"""
        target_account = Account(
            account_id="ACC002",
            account_number="0987654321",
            account_type="checking",
            balance=500.0,
            currency="USD",
            owner_id="user002",
            opening_date=datetime.now()
        )
        
        initial_balance_source = account.balance
        initial_balance_target = target_account.balance
        transfer_amount = 200.0
        
        account.transfer_to_account(target_account, transfer_amount)
        
        assert account.balance == initial_balance_source - transfer_amount
        assert target_account.balance == initial_balance_target + transfer_amount
    
    def test_transfer_to_account_insufficient_funds(self, account):
        """Тест перевода при недостатке средств"""
        target_account = Account(
            account_id="ACC002",
            account_number="0987654321",
            account_type="checking",
            balance=500.0,
            currency="USD",
            owner_id="user002",
            opening_date=datetime.now()
        )
        
        with pytest.raises(InsufficientFundsException):
            account.transfer_to_account(target_account, 2000.0)
    
    def test_calculate_interest(self, account):
        """Тест вычисления процентов"""
        account.balance = 10000.0
        account.interest_rate = 5.0
        interest = account.calculate_interest(12)  # 12 месяцев
        expected = 10000.0 * (5.0 / 100) * 12
        assert interest == expected
    
    def test_get_transaction_count(self, account):
        """Тест получения количества транзакций"""
        assert account.get_transaction_count() == 0
        account.deposit(100.0)
        assert account.get_transaction_count() == 1
        account.withdraw(50.0)
        assert account.get_transaction_count() == 2
    
    def test_close_account_success(self, account):
        """Тест закрытия счета с нулевым балансом"""
        account.balance = 0.0
        account.close_account()
        assert account.is_active is False
    
    def test_close_account_with_balance(self, account):
        """Тест закрытия счета с ненулевым балансом"""
        account.balance = 100.0
        with pytest.raises(ValueError, match="Баланс должен быть нулевым"):
            account.close_account()
    
    def test_link_to_bank(self, account):
        """Тест связи с банком (ассоциация)"""
        bank = Bank(
            bank_id="B001",
            bank_name="Test Bank",
            country="Russia",
            swift_code="TESTRUMM",
            establishment_date=datetime(2000, 1, 1),
            total_customers=1000,
            total_assets=1000000.0
        )
        account.link_to_bank(bank)
        assert account.bank_id == "B001"
    
    def test_add_card(self, account):
        """Тест добавления карты (ассоциация)"""
        card = Card(
            card_number="1234567890123456",
            cardholder_name="Test",
            expiry_date=datetime.now() + timedelta(days=365),
            cvv="123",
            card_type="Visa",
            balance=1000.0,
            bank_name="Bank"
        )
        account.add_card(card)
        assert hasattr(account, 'cards')
        assert "1234567890123456" in account.cards



