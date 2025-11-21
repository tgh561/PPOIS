"""Исключение: Недостаточно средств"""


class InsufficientFundsException(Exception):
    """Вызывается когда недостаточно средств для операции"""
    
    def __init__(self, account_balance: float, required_amount: float, message: str = None):
        self.account_balance = account_balance
        self.required_amount = required_amount
        self.message = message or f"Недостаточно средств. Текущий баланс: {account_balance}, требуется: {required_amount}"
        super().__init__(self.message)


