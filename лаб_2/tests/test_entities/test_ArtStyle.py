# Тесты для класса ArtStyle

from entities.ArtStyle import ArtStyle

def test_init_defaults():
    style = ArtStyle(name="Impressionism")
    assert style.name == "Impressionism"
    assert style.description == ""
    assert style.origin_year == 0
    assert style.typical_features == []

def test_init_full():
    features = ["light", "color", "movement"]
    style = ArtStyle(name="Cubism", description="Geometric abstraction", origin_year=1907, typical_features=features)
    assert style.origin_year == 1907
    assert style.typical_features == features

def test_short_description_truncates():
    desc = "A" * 100
    style = ArtStyle(name="Surrealism", description=desc)
    assert style.short_description() == f"Surrealism: {'A'*80}"
