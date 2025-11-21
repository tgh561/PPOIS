"""Тесты для класса Bank"""
import pytest
from datetime import datetime
from Finance.Bank import Bank


class TestBank:
    """Тесты для класса Bank"""
    
    @pytest.fixture
    def bank(self):
        """Фикстура для создания банка"""
        return Bank(
            bank_id="B001",
            bank_name="Test Bank",
            country="Russia",
            swift_code="TESTRUMM",
            establishment_date=datetime(2000, 1, 1),
            total_customers=1000,
            total_assets=1000000.0
        )
    
    def test_init(self, bank):
        """Тест инициализации"""
        assert bank.bank_id == "B001"
        assert bank.bank_name == "Test Bank"
        assert bank.country == "Russia"
        assert bank.swift_code == "TESTRUMM"
        assert bank.total_customers == 1000
        assert bank.total_assets == 1000000.0
        assert isinstance(bank.accounts, list)
        assert isinstance(bank.cards, list)
        assert isinstance(bank.branches, list)
        assert isinstance(bank.interest_rates, dict)
    
    def test_open_account(self, bank):
        """Тест открытия счета"""
        initial_customers = bank.total_customers
        initial_accounts = len(bank.accounts)
        
        bank.open_account("ACC001")
        assert "ACC001" in bank.accounts
        assert len(bank.accounts) == initial_accounts + 1
        assert bank.total_customers == initial_customers + 1
    
    def test_open_account_duplicate(self, bank):
        """Тест открытия дублирующегося счета"""
        bank.open_account("ACC001")
        initial_count = len(bank.accounts)
        bank.open_account("ACC001")
        assert len(bank.accounts) == initial_count
    
    def test_close_account(self, bank):
        """Тест закрытия счета"""
        bank.open_account("ACC001")
        bank.close_account("ACC001")
        assert "ACC001" not in bank.accounts
    
    def test_close_account_not_exists(self, bank):
        """Тест закрытия несуществующего счета"""
        bank.close_account("ACC999")
        assert len(bank.accounts) == 0
    
    def test_issue_card(self, bank):
        """Тест выдачи карты"""
        bank.issue_card("CARD001")
        assert "CARD001" in bank.cards
        
        bank.issue_card("CARD002")
        assert len(bank.cards) == 2
    
    def test_issue_card_duplicate(self, bank):
        """Тест выдачи дублирующейся карты"""
        bank.issue_card("CARD001")
        initial_count = len(bank.cards)
        bank.issue_card("CARD001")
        assert len(bank.cards) == initial_count
    
    def test_add_branch(self, bank):
        """Тест добавления филиала"""
        bank.add_branch("BRANCH001")
        assert "BRANCH001" in bank.branches
        
        bank.add_branch("BRANCH002")
        assert len(bank.branches) == 2
    
    def test_add_branch_duplicate(self, bank):
        """Тест добавления дублирующегося филиала"""
        bank.add_branch("BRANCH001")
        initial_count = len(bank.branches)
        bank.add_branch("BRANCH001")
        assert len(bank.branches) == initial_count
    
    def test_set_interest_rate(self, bank):
        """Тест установки процентной ставки"""
        bank.set_interest_rate("checking", 2.5)
        assert bank.interest_rates["checking"] == 2.5
        
        bank.set_interest_rate("savings", 5.0)
        assert bank.interest_rates["savings"] == 5.0
    
    def test_get_interest_rate_exists(self, bank):
        """Тест получения процентной ставки - существует"""
        bank.set_interest_rate("checking", 3.0)
        rate = bank.get_interest_rate("checking")
        assert rate == 3.0
    
    def test_get_interest_rate_not_exists(self, bank):
        """Тест получения процентной ставки - не существует"""
        rate = bank.get_interest_rate("nonexistent")
        assert rate == 0.0
    
    def test_calculate_total_accounts(self, bank):
        """Тест вычисления общего количества счетов"""
        assert bank.calculate_total_accounts() == 0
        
        bank.open_account("ACC001")
        bank.open_account("ACC002")
        assert bank.calculate_total_accounts() == 2
    
    def test_process_interbank_transfer(self, bank):
        """Тест обработки межбанковского перевода"""
        result = bank.process_interbank_transfer(10000.0, "TARGETRUMM")
        assert result is True



