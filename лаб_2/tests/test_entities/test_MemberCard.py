# Тесты для класса MemberCard

from entities.MemberCard import MemberCard
from entities.Visitor import Visitor

def test_discount_and_points():
    v = Visitor("Иван")
    card = MemberCard("C1", v, discount_rate=0.2)
    assert card.apply_discount(100) == 80
    card.add_points(10)
    assert card.points == 10
    assert card.redeem_points(5)
    assert card.points == 5
