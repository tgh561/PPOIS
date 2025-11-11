from __future__ import annotations
from typing import List

class Revenue:
    def __init__(self, source: str, amount: float, date: str):
        self.source = source
        self.amount = amount
        self.date = date
        self.records: List[float] = [amount]

    def record(self, additional: float) -> None:
        self.records.append(additional)
        self.amount += additional

    def summarize(self) -> float:
        return sum(self.records)
