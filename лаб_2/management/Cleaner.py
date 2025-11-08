from Employee import Employee
from entities.GalleryHall import GalleryHall
class Cleaner(Employee):

    def __init__(self, name: str, position: str = "Cleaner", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.assigned_halls: list["GalleryHall"] = []

    def assign_hall(self, hall: "GalleryHall") -> None:
        if hall not in self.assigned_halls:
            self.assigned_halls.append(hall)

    def clean_hall(self, hall: "GalleryHall") -> str:
        if hall in self.assigned_halls:
            return f"{self.name} cleaned {hall.name}"
        return f"{self.name} is not assigned to {hall.name}"
