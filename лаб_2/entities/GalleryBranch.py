from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Address import Address
    from management.Employee import Employee
from Gallery import Gallery
class GalleryBranch(Gallery):
    def __init__(self, name: str, address: "Address", parent_gallery: "Gallery"):
        super().__init__(name, address)
        self.parent_gallery = parent_gallery
        self.branch_manager: "Employee" | None = None

    def get_parent_info(self) -> str:
        return f"Branch of {self.parent_gallery.name}"
