from management.Employee import Employee

class Technician(Employee):


    def __init__(self, name: str, position: str = "Technician", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.maintenance_tasks: list[str] = []

    def add_task(self, task: str) -> None:
        self.maintenance_tasks.append(task)

    def perform_task(self) -> str:
        if self.maintenance_tasks:
            task = self.maintenance_tasks.pop(0)
            return f"{self.name} performed task: {task}"
        return f"No tasks for {self.name}"
