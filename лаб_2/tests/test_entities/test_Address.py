# tests/test_entities/test_Address.py
import pytest
from entities.Address import Address

@pytest.mark.parametrize(
    "city, street, building, postal, expected",
    [
        ("Moscow", "Lenina", "10", "123456", "Moscow, Lenina 10, 123456"),
        ("Saint Petersburg", "Nevsky", "5", "", "Saint Petersburg, Nevsky 5, "),
        ("", "", "", "", ",  , "),
        ("Тест", "Улица", "№1", "00000", "Тест, Улица №1, 00000"),
    ],
)
def test_full_address_various(city, street, building, postal, expected):
    addr = Address(city=city, street=street, building=building, postal_code=postal)
    assert addr.city == city
    assert addr.street == street
    assert addr.building == building
    assert addr.postal_code == postal
    assert addr.full_address() == expected

def test_default_postal_code_is_empty():
    addr = Address(city="C", street="S", building="B")
    assert addr.postal_code == ""
    assert addr.full_address() == "C, S B, "

def test_mutation_and_repr_like_behavior():
    addr = Address(city="A", street="B", building="C", postal_code="1")
    # проверяем что можно изменить атрибуты и full_address отразит эти изменения
    addr.city = "X"
    addr.street = "Y"
    addr.building = "Z"
    addr.postal_code = "999"
    assert addr.full_address() == "X, Y Z, 999"

def test_non_string_inputs_are_stored_and_converted_by_fstring():
    # если передать числа, f-string приведёт их к строке — проверяем это поведение
    addr = Address(city=123, street=45.6, building=None, postal_code=0)
    # full_address использует f-string, поэтому None -> "None"
    assert addr.full_address() == "123, 45.6 None, 0"
