# Тесты для класса Director

from management.Director import Director
from management.Curator import Curator

def test_add_curator_and_overview():
    director = Director("Dir", salary=3000.0)
    c1 = Curator("C1")
    c2 = Curator("C2")
    director.add_curator(c1)
    director.add_curator(c2)
    director.add_curator(c1)  # duplicate ignored
    assert c1 in director.managed_curators and c2 in director.managed_curators
    overview = director.overview_gallery()
    assert "manages 2 curators" in overview or "2" in overview
