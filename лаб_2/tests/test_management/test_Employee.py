# Тесты для класса Employee

from management.Employee import Employee

def test_employee_basic_fields_and_methods():
    e = Employee("Иван", "Staff", 1000.0, employee_id="E-1")
    assert e.name == "Иван"
    assert e.position == "Staff"
    assert e.salary == 1000.0
    assert e.employee_id == "E-1"

    e.assign_to_hall("Hall-1")
    assert e.assigned_hall == "Hall-1"

    e.promote("Senior", 1500.0)
    assert e.position == "Senior"
    assert e.salary == 1500.0

    info = e.get_info()
    assert "Иван" in info and "Senior" in info
