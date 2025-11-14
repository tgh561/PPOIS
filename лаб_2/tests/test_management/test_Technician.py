# Тесты для класса Technician

from management.Technician import Technician

def test_add_and_perform_task():
    tech = Technician("Tech", salary=1000.0)
    tech.add_task("Fix light")
    tech.add_task("Check AC")
    assert len(tech.maintenance_tasks) == 2
    out = tech.perform_task()
    assert "performed task" in out
    # perform second, then none
    tech.perform_task()
    out2 = tech.perform_task()
    assert "No tasks" in out2
