import os

# Путь к папке с исходными классами
entities_path = "/mnt/windows_d/учёба/ppois/лаб_2/management"
# Папка, куда будут созданы тесты
test_path = "/mnt/windows_d/учёба/ppois/лаб_2/tests/test_management"

# Убедимся, что папка для тестов существует
os.makedirs(test_path, exist_ok=True)

# Перебираем все .py файлы в entities
for filename in os.listdir(entities_path):
    if filename.endswith(".py") and filename != "__init__.py":
        class_name = filename.replace(".py", "")
        test_filename = f"test_{class_name}.py"
        test_filepath = os.path.join(test_path, test_filename)

        # Создаём пустой файл, если он ещё не существует
        if not os.path.exists(test_filepath):
            with open(test_filepath, "w", encoding="utf-8") as f:
                f.write(f"# Тесты для класса {class_name}\n\n")
            print(f"Создан: {test_filename}")
        else:
            print(f"Уже существует: {test_filename}")
