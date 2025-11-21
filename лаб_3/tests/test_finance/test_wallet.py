"""Тесты для класса Wallet"""
import pytest
from datetime import datetime, timedelta
from Finance.Wallet import Wallet
from Exceptions.InsufficientFundsException import InsufficientFundsException


class TestWallet:
    """Тесты для класса Wallet"""
    
    @pytest.fixture
    def wallet(self):
        """Фикстура для создания кошелька"""
        return Wallet(
            wallet_id="W001",
            owner_id="user001",
            currency="USD",
            balance=500.0,
            creation_date=datetime.now(),
            wallet_type="digital"
        )
    
    def test_init(self, wallet):
        """Тест инициализации"""
        assert wallet.wallet_id == "W001"
        assert wallet.owner_id == "user001"
        assert wallet.currency == "USD"
        assert wallet.balance == 500.0
        assert wallet.wallet_type == "digital"
        assert wallet.is_active is True
        assert isinstance(wallet.cards, list)
        assert isinstance(wallet.transaction_history, list)
    
    def test_add_card(self, wallet):
        """Тест добавления карты"""
        wallet.add_card("CARD001")
        assert "CARD001" in wallet.cards
        
        wallet.add_card("CARD002")
        assert len(wallet.cards) == 2
    
    def test_add_card_duplicate(self, wallet):
        """Тест добавления дублирующейся карты"""
        wallet.add_card("CARD001")
        wallet.add_card("CARD001")
        assert wallet.cards.count("CARD001") == 1
    
    def test_remove_card_success(self, wallet):
        """Тест удаления карты"""
        wallet.add_card("CARD001")
        wallet.remove_card("CARD001")
        assert "CARD001" not in wallet.cards
    
    def test_remove_card_not_exists(self, wallet):
        """Тест удаления несуществующей карты"""
        wallet.remove_card("CARD999")
        assert len(wallet.cards) == 0
    
    def test_add_funds_success(self, wallet):
        """Тест пополнения кошелька"""
        initial_balance = wallet.balance
        amount = 200.0
        wallet.add_funds(amount, "deposit")
        assert wallet.balance == initial_balance + amount
        assert len(wallet.transaction_history) == 1
        assert wallet.transaction_history[0]["type"] == "credit"
        assert wallet.transaction_history[0]["amount"] == amount
    
    def test_add_funds_invalid_amount_zero(self, wallet):
        """Тест пополнения нулевой суммой"""
        with pytest.raises(ValueError, match="Сумма должна быть положительной"):
            wallet.add_funds(0.0)
    
    def test_add_funds_invalid_amount_negative(self, wallet):
        """Тест пополнения отрицательной суммой"""
        with pytest.raises(ValueError, match="Сумма должна быть положительной"):
            wallet.add_funds(-100.0)
    
    def test_deduct_funds_success(self, wallet):
        """Тест списания средств"""
        initial_balance = wallet.balance
        amount = 200.0
        wallet.deduct_funds(amount, "Purchase")
        assert wallet.balance == initial_balance - amount
        assert len(wallet.transaction_history) == 1
        assert wallet.transaction_history[0]["type"] == "debit"
    
    def test_deduct_funds_insufficient(self, wallet):
        """Тест списания при недостатке средств"""
        with pytest.raises(InsufficientFundsException):
            wallet.deduct_funds(1000.0)
    
    def test_transfer_to_wallet_success(self, wallet):
        """Тест перевода между кошельками"""
        target_wallet = Wallet(
            wallet_id="W002",
            owner_id="user002",
            currency="USD",
            balance=300.0,
            creation_date=datetime.now()
        )
        
        initial_balance_source = wallet.balance
        initial_balance_target = target_wallet.balance
        transfer_amount = 200.0
        
        wallet.transfer_to_wallet(target_wallet, transfer_amount)
        
        assert wallet.balance == initial_balance_source - transfer_amount
        assert target_wallet.balance == initial_balance_target + transfer_amount
    
    def test_transfer_to_wallet_insufficient_funds(self, wallet):
        """Тест перевода при недостатке средств"""
        target_wallet = Wallet(
            wallet_id="W002",
            owner_id="user002",
            currency="USD",
            balance=300.0,
            creation_date=datetime.now()
        )
        
        with pytest.raises(InsufficientFundsException):
            wallet.transfer_to_wallet(target_wallet, 1000.0)
    
    def test_get_total_transactions(self, wallet):
        """Тест получения количества транзакций"""
        assert wallet.get_total_transactions() == 0
        wallet.add_funds(100.0)
        assert wallet.get_total_transactions() == 1
        wallet.deduct_funds(50.0)
        assert wallet.get_total_transactions() == 2
    
    def test_calculate_monthly_spending(self, wallet):
        """Тест вычисления месячных трат"""
        now = datetime.now()
        wallet.transaction_history.append({
            "type": "debit",
            "amount": 100.0,
            "date": datetime(now.year, now.month, 1)
        })
        wallet.transaction_history.append({
            "type": "debit",
            "amount": 200.0,
            "date": datetime(now.year, now.month, 15)
        })
        wallet.transaction_history.append({
            "type": "credit",
            "amount": 500.0,
            "date": datetime(now.year, now.month, 10)
        })
        
        spending = wallet.calculate_monthly_spending(now.month, now.year)
        assert spending == 300.0
    
    def test_calculate_monthly_spending_no_transactions(self, wallet):
        """Тест вычисления месячных трат без транзакций"""
        spending = wallet.calculate_monthly_spending(1, 2024)
        assert spending == 0.0



