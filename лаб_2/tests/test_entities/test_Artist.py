import pytest
from entities.Artist import Artist

# Заглушки для ArtStyle и Painting
class DummyStyle:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, DummyStyle) and self.name == other.name

class DummyPainting:
    def __init__(self, title):
        self.title = title
    def __eq__(self, other):
        return isinstance(other, DummyPainting) and self.title == other.title

def test_init_minimal():
    artist = Artist(name="Van Gogh", birth_year=1853)
    assert artist.name == "Van Gogh"
    assert artist.birth_year == 1853
    assert artist.death_year is None
    assert artist.bio == ""
    assert artist.styles == []
    assert artist.paintings == []
    assert not artist.is_deceased()
    assert artist.summary() == "Van Gogh (1853)"

def test_init_full():
    artist = Artist(name="Da Vinci", birth_year=1452, death_year=1519, bio="Renaissance genius")
    assert artist.name == "Da Vinci"
    assert artist.death_year == 1519
    assert artist.bio == "Renaissance genius"
    assert artist.is_deceased()
    assert artist.summary() == "Da Vinci (1452–1519)"

def test_add_style_once():
    artist = Artist(name="Test", birth_year=1900)
    style = DummyStyle("Impressionism")
    artist.add_style(style)
    assert artist.styles == [style]

def test_add_style_duplicate():
    artist = Artist(name="Test", birth_year=1900)
    style = DummyStyle("Surrealism")
    artist.add_style(style)
    artist.add_style(style)  # повторно
    assert artist.styles == [style]

def test_add_painting_once():
    artist = Artist(name="Test", birth_year=1900)
    painting = DummyPainting("Starry Night")
    artist.add_painting(painting)
    assert artist.paintings == [painting]

def test_add_painting_duplicate():
    artist = Artist(name="Test", birth_year=1900)
    painting = DummyPainting("Mona Lisa")
    artist.add_painting(painting)
    artist.add_painting(painting)  # повторно
    assert artist.paintings == [painting]

def test_summary_edge_case_empty_name():
    artist = Artist(name="", birth_year=0)
    assert artist.summary() == " (0)"
