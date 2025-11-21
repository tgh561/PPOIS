"""Тесты для класса Car"""
import pytest
from datetime import datetime, timedelta
from Transport.Car import Car


class TestCar:
    """Тесты для класса Car"""
    
    @pytest.fixture
    def car(self):
        """Фикстура для создания автомобиля"""
        return Car(
            car_id="CAR001",
            make="Toyota",
            model="Camry",
            year=2020,
            license_plate="А123БВ777",
            rental_price_per_day=5000.0,
            fuel_type="petrol",
            seats=5,
            mileage=50000.0
        )
    
    def test_init(self, car):
        """Тест инициализации"""
        assert car.car_id == "CAR001"
        assert car.make == "Toyota"
        assert car.model == "Camry"
        assert car.year == 2020
        assert car.license_plate == "А123БВ777"
        assert car.rental_price_per_day == 5000.0
        assert car.fuel_type == "petrol"
        assert car.seats == 5
        assert car.mileage == 50000.0
        assert car.is_available is True
        assert car.current_renter is None
        assert car.insurance_included is False
    
    def test_rent_car_success(self, car):
        """Тест аренды автомобиля - успех"""
        start_date = datetime.now()
        end_date = datetime.now() + timedelta(days=3)
        cost = car.rent_car("RENTER001", start_date, end_date)
        assert car.is_available is False
        assert car.current_renter == "RENTER001"
        assert cost == 5000.0 * 3
    
    def test_rent_car_unavailable(self, car):
        """Тест аренды недоступного автомобиля"""
        car.is_available = False
        with pytest.raises(ValueError, match="Автомобиль недоступен"):
            car.rent_car("RENTER002", datetime.now(), datetime.now() + timedelta(days=1))
    
    def test_return_car(self, car):
        """Тест возврата автомобиля"""
        car.is_available = False
        car.current_renter = "RENTER001"
        car.return_car(51000.0)
        assert car.is_available is True
        assert car.current_renter is None
        assert car.mileage == 51000.0
    
    def test_calculate_rental_cost(self, car):
        """Тест вычисления стоимости аренды"""
        cost = car.calculate_rental_cost(5)
        assert cost == 5000.0 * 5
    
    def test_add_insurance(self, car):
        """Тест добавления страховки"""
        car.add_insurance()
        assert car.insurance_included is True
    
    def test_calculate_fuel_cost(self, car):
        """Тест вычисления стоимости топлива"""
        car.set_fuel_consumption(8.0)  # 8 литров на 100 км
        fuel_cost = car.calculate_fuel_cost(200.0, 50.0)  # 200 км, 50 руб/литр
        assert fuel_cost == (200.0 / 100) * 8.0 * 50.0
    
    def test_set_fuel_consumption(self, car):
        """Тест установки расхода топлива"""
        car.set_fuel_consumption(10.0)
        assert car.fuel_consumption == 10.0
