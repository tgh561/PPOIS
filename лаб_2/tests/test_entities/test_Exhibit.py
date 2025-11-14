# Тесты для класса Exhibit

from entities.Exhibit import Exhibit

class DummyArtist:
    def __init__(self, name):
        self.name = name
        self.paintings = []
    def add_painting(self, p):
        self.paintings.append(p)

class DummyHall:
    pass

def test_init_and_basic_info():
    artist = DummyArtist("Monet")
    exhibit = Exhibit(title="Water Lilies", artist=artist, accession_id="A001", description="Famous piece")
    assert exhibit.title == "Water Lilies"
    assert exhibit.artist.name == "Monet"
    assert exhibit.accession_id == "A001"
    assert exhibit.description == "Famous piece"
    assert exhibit.basic_info() == "Water Lilies by Monet (A001)"
    assert artist.paintings == [exhibit]

def test_auto_accession_id():
    artist = DummyArtist("Van Gogh")
    exhibit = Exhibit(title="Starry Night", artist=artist)
    assert exhibit.accession_id.startswith("ACC-")

def test_assign_location():
    artist = DummyArtist("Test")
    hall = DummyHall()
    exhibit = Exhibit("X", artist)
    exhibit.assign_location(hall)
    assert exhibit.location == hall
