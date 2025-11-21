"""Тесты для класса Restaurant"""
import pytest
from datetime import datetime
from Destinations.Restaurant import Restaurant


class TestRestaurant:
    """Тесты для класса Restaurant"""
    
    @pytest.fixture
    def restaurant(self):
        """Фикстура для создания ресторана"""
        return Restaurant(
            restaurant_id="RES001",
            name="Grand Restaurant",
            location="Париж",
            cuisine_type="Французская",
            price_range="высокий",
            rating=4.5,
            capacity=50,
            opening_hours="12:00-23:00"
        )
    
    def test_init(self, restaurant):
        """Тест инициализации"""
        assert restaurant.restaurant_id == "RES001"
        assert restaurant.name == "Grand Restaurant"
        assert restaurant.location == "Париж"
        assert restaurant.cuisine_type == "Французская"
        assert restaurant.price_range == "высокий"
        assert restaurant.rating == 4.5
        assert restaurant.capacity == 50
        assert restaurant.current_guests == 0
        assert isinstance(restaurant.menu_items, list)
        assert isinstance(restaurant.reservations, list)
    
    def test_make_reservation_success(self, restaurant):
        """Тест бронирования столика - успех"""
        restaurant.make_reservation(4)
        assert restaurant.current_guests == 4
        
        restaurant.make_reservation(2)
        assert restaurant.current_guests == 6
    
    def test_make_reservation_full(self, restaurant):
        """Тест бронирования столика - переполнен"""
        restaurant.current_guests = 48
        with pytest.raises(ValueError, match="Ресторан переполнен"):
            restaurant.make_reservation(5)
    
    def test_cancel_reservation(self, restaurant):
        """Тест отмены бронирования"""
        restaurant.make_reservation(10)
        restaurant.cancel_reservation(5)
        assert restaurant.current_guests == 5
    
    def test_cancel_reservation_more_than_current(self, restaurant):
        """Тест отмены большего количества, чем есть"""
        restaurant.make_reservation(5)
        restaurant.cancel_reservation(10)
        assert restaurant.current_guests == 0
    
    def test_add_menu_item(self, restaurant):
        """Тест добавления позиции в меню"""
        restaurant.add_menu_item("Борщ", 500.0)
        assert len(restaurant.menu_items) == 1
        assert restaurant.menu_items[0]["name"] == "Борщ"
        assert restaurant.menu_items[0]["price"] == 500.0
    
    def test_calculate_average_price(self, restaurant):
        """Тест вычисления средней цены"""
        restaurant.add_menu_item("Блюдо 1", 1000.0)
        restaurant.add_menu_item("Блюдо 2", 2000.0)
        avg = restaurant.calculate_average_price()
        assert avg == 1500.0
    
    def test_calculate_average_price_empty(self, restaurant):
        """Тест вычисления средней цены - пустое меню"""
        avg = restaurant.calculate_average_price()
        assert avg == 0.0
    
    def test_update_rating(self, restaurant):
        """Тест обновления рейтинга"""
        initial_rating = restaurant.rating
        restaurant.update_rating(5.0)
        assert restaurant.rating == (initial_rating + 5.0) / 2
    
    def test_is_available_true(self, restaurant):
        """Тест проверки доступности - да"""
        assert restaurant.is_available() is True
    
    def test_is_available_false(self, restaurant):
        """Тест проверки доступности - нет"""
        restaurant.current_guests = 50
        assert restaurant.is_available() is False
