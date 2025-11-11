from __future__ import annotations

class PaymentFailed(Exception):
    def __init__(self, message: str = "Payment failed"):
        super().__init__(message)