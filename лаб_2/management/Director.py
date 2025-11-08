from typing import List
from Employee import Employee
from Employee import Employee
from Curator import Curator

class Director(Employee):
    def __init__(self, name: str, position: str = "Director", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.managed_curators: List["Curator"] = []

    def add_curator(self, curator: "Curator") -> None:
        if curator not in self.managed_curators:
            self.managed_curators.append(curator)

    def overview_gallery(self) -> str:
        return f"Director {self.name} manages {len(self.managed_curators)} curators."
