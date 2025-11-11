from __future__ import annotations

class TransactionInvalid(Exception):
    def __init__(self, message: str = "Transaction is invalid"):
        super().__init__(message)