"""Тесты для класса Package"""
import pytest
from datetime import datetime
from Tours.Package import Package


class TestPackage:
    """Тесты для класса Package"""
    
    @pytest.fixture
    def package(self):
        """Фикстура для создания турпакета"""
        return Package(
            package_id="PKG001",
            name="Турпакет в Париж",
            description="Полный турпакет в Париж",
            duration_days=7,
            base_price=100000.0,
            includes_flight=True,
            includes_hotel=True,
            includes_meals=True
        )
    
    def test_init(self, package):
        """Тест инициализации"""
        assert package.package_id == "PKG001"
        assert package.name == "Турпакет в Париж"
        assert package.description == "Полный турпакет в Париж"
        assert package.duration_days == 7
        assert package.base_price == 100000.0
        assert package.includes_flight is True
        assert package.includes_hotel is True
        assert package.includes_meals is True
        assert isinstance(package.destinations, list)
        assert isinstance(package.services, list)
        assert package.bookings_count == 0
    
    def test_add_destination(self, package):
        """Тест добавления направления"""
        package.add_destination("Париж")
        assert "Париж" in package.destinations
        
        package.add_destination("Лондон")
        assert len(package.destinations) == 2
    
    def test_add_destination_duplicate(self, package):
        """Тест добавления дублирующегося направления"""
        package.add_destination("Париж")
        package.add_destination("Париж")
        assert package.destinations.count("Париж") == 1
    
    def test_add_service(self, package):
        """Тест добавления услуги"""
        package.add_service("Экскурсия")
        assert "Экскурсия" in package.services
        
        package.add_service("Трансфер")
        assert len(package.services) == 2
    
    def test_add_service_duplicate(self, package):
        """Тест добавления дублирующейся услуги"""
        package.add_service("Экскурсия")
        package.add_service("Экскурсия")
        assert package.services.count("Экскурсия") == 1
    
    def test_calculate_final_price_no_discount(self, package):
        """Тест вычисления финальной цены - без скидки"""
        final_price = package.calculate_final_price()
        assert final_price == 100000.0
    
    def test_calculate_final_price_with_discount(self, package):
        """Тест вычисления финальной цены - со скидкой"""
        discount = 0.1
        final_price = package.calculate_final_price(discount)
        assert final_price == 100000.0 * 0.9
    
    def test_get_inclusions_all(self, package):
        """Тест получения включенных услуг - все включено"""
        inclusions = package.get_inclusions()
        assert "Перелет" in inclusions
        assert "Отель" in inclusions
        assert "Питание" in inclusions
        assert len(inclusions) == 3
    
    def test_get_inclusions_partial(self):
        """Тест получения включенных услуг - частично"""
        package = Package(
            package_id="PKG002",
            name="Турпакет без питания",
            description="Description",
            duration_days=5,
            base_price=80000.0,
            includes_flight=True,
            includes_hotel=True,
            includes_meals=False
        )
        inclusions = package.get_inclusions()
        assert "Перелет" in inclusions
        assert "Отель" in inclusions
        assert "Питание" not in inclusions
        assert len(inclusions) == 2
    
    def test_increment_bookings(self, package):
        """Тест увеличения счетчика бронирований"""
        initial_count = package.bookings_count
        package.increment_bookings()
        assert package.bookings_count == initial_count + 1
        
        package.increment_bookings()
        assert package.bookings_count == initial_count + 2



