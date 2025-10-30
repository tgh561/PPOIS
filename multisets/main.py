from Multiset import Multiset

def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

def main():
    registry = {}         
    next_id = 1

    menu = (
        "Доступные действия:\n"
        "1 - Создать мультимножество\n"
        "2 - Показать список мультимножеств\n"
        "3 - Показать мультимножество по номеру\n"
        "4 - Редактировать мультимножество по номеру\n"
        "5 - Удалить мультимножество по номеру\n"
        "6 - Объединение A + B (по номерам)\n"
        "7 - Пересечение A * B (по номерам)\n"
        "8 - Разность A - B (по номерам)\n"
        "9 - Выйти\n"
    )

    while True:
        print()
        print(menu)
        choice = input_int("Выберите действие: ")
        if choice is None:
            print("Неверный ввод, введите номер пункта.")
            continue

        if choice == 1:
            s = input("Введите мультимножество (пример {a,a,b,{c,d}}): ").strip()
            m = Multiset(s)
            registry[next_id] = m
            print(f"Создано под номером {next_id}")
            next_id += 1

        elif choice == 2:
            if not registry:
                print("Реестр пуст.")
            else:
                for k, v in registry.items():
                    print(f"{k}: {v.string}")

        elif choice == 3:
            idx = input_int("Номер мультимножества: ")
            if idx is None or idx not in registry:
                print("Мультимножество с таким номером не найдено.")
            else:
                print(f"{idx}: {registry[idx].string}")
                registry[idx].output()

        elif choice == 4:
            idx = input_int("Номер мультимножества для редактирования: ")
            if idx is None or idx not in registry:
                print("Мультимножество с таким номером не найдено.")
            else:
                registry[idx].edit(registry=registry, key=idx)

        elif choice == 5:
            idx = input_int("Номер мультимножества для удаления: ")
            if idx is None or idx not in registry:
                print("Мультимножество с таким номером не найдено.")
            else:
                del registry[idx]
                print(f"Мультимножество {idx} удалено.")

        elif choice in (6, 7, 8):
            a = input_int("Номер первого мультимножества: ")
            b = input_int("Номер второго мультимножества: ")
            if a is None or b is None or a not in registry or b not in registry:
                print("Один или оба номера не найдены в реестре.")
                continue
            A = registry[a]
            B = registry[b]
            if choice == 6:
                R = A.union(B)
                print("Результат объединения:")
                R.output()
            elif choice == 7:
                R = A.intersection(B)
                print("Результат пересечения:")
                R.output()
            else:
                R = A.difference(B)
                print("Результат разности:")
                R.output()

        elif choice == 9:
            print("Выход.")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
