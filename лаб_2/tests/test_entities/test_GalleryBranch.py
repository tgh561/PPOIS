# Тесты для класса GalleryBranch

from entities.GalleryBranch import GalleryBranch
from entities.Address import Address
from entities.Gallery import Gallery

def test_branch_info():
    parent = Gallery("Main", Address("Минск", "Ленина", "10"))
    branch = GalleryBranch("Branch", Address("Минск", "Победы", "5"), parent)
    assert "Main" in branch.get_parent_info()
