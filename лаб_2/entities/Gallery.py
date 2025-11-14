from typing import List, TYPE_CHECKING
from typing import Optional
from entities.Painting import Painting


if TYPE_CHECKING:
    from entities.Exhibit import Exhibit
    from entities.Painting import Painting
    from entities.Address import Address
    from entities.GalleryBranch import GalleryBranch
    from entities.GalleryHall import GalleryHall
    from management.Employee import Employee


class Gallery:
    def __init__(self, name: str, address: "Address"):
        self.name = name
        self.address = address
        self.branches: List["GalleryBranch"] = []
        self.halls: List["GalleryHall"] = []
        self.employees: list["Employee"] = []
        self.collections: List["Exhibit"] = []

    def add_hall(self, hall: "GalleryHall") -> None:
        if hall not in self.halls:
            self.halls.append(hall)

    def add_branch(self, branch: "GalleryBranch") -> None:
        if branch not in self.branches:
            self.branches.append(branch)

    def add_employee(self, employee: "Employee") -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def find_painting(self, title: str) -> Optional["Painting"]:
        for hall in self.halls:
            found = hall.find_exhibit_by_title(title)
            if found and isinstance(found, Painting):
                return found
        for ex in self.collections:
            if ex.title == title and isinstance(ex, Painting):
                return ex
        return None

    def list_all_exhibits(self) -> List["Exhibit"]:
        all_ex = []
        for h in self.halls:
            all_ex.extend(h.exhibits)
        all_ex.extend(self.collections)
        return all_ex
