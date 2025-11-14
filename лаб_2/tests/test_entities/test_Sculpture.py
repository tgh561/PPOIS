# Тесты для класса Sculpture

from entities.Sculpture import Sculpture
from entities.Artist import Artist

def test_install_uninstall_and_value():
    artist = Artist("Роден", 1840)
    s = Sculpture("Мыслитель", artist, material="бронза", weight=50, height=2)
    s.install("Hall")
    assert s.is_installed
    s.uninstall()
    assert not s.is_installed
    assert s.estimate_insurance_value() > 0
