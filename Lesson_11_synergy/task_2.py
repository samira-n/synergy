import collections

# Исходная база данных
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    """Возвращает правильный суффикс для возраста"""
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    """Возвращает информацию о питомце по ID или False если не найден"""
    return pets[ID] if ID in pets else False

def pets_list():
    """Выводит список всех питомцев"""
    print("\nСписок всех питомцев:")
    for ID, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        print(f"ID: {ID}, Кличка: {pet_name}")

def create():
    """Добавляет новую запись о питомце"""
    try:
        last = collections.deque(pets, maxlen=1)[0] if pets else 0
        new_id = last + 1
        
        pet_name = input("Введите кличку питомца: ")
        pet_type = input("Введите вид питомца: ")
        pet_age = int(input("Введите возраст питомца: "))
        owner_name = input("Введите имя владельца: ")
        
        pets[new_id] = {
            pet_name: {
                "Вид питомца": pet_type,
                "Возраст питомца": pet_age,
                "Имя владельца": owner_name
            }
        }
        print(f"\nЗапись добавлена под ID: {new_id}")
    except ValueError:
        print("Ошибка: Возраст должен быть числом")

def read():
    """Выводит информацию о питомце"""
    try:
        ID = int(input("Введите ID питомца: "))
        pet_info = get_pet(ID)
        
        if pet_info:
            pet_name = list(pet_info.keys())[0]
            pet_data = pet_info[pet_name]
            age = pet_data["Возраст питомца"]
            suffix = get_suffix(age)
            
            print(f'\nЭто {pet_data["Вид питомца"]} по кличке "{pet_name}". '
                  f'Возраст питомца: {age} {suffix}. '
                  f'Имя владельца: {pet_data["Имя владельца"]}')
        else:
            print("\nПитомец с таким ID не найден")
    except ValueError:
        print("Ошибка: ID должен быть числом")

def update():
    """Обновляет информацию о питомце"""
    try:
        ID = int(input("Введите ID питомца для обновления: "))
        pet_info = get_pet(ID)
        
        if pet_info:
            pet_name = list(pet_info.keys())[0]
            print("\nВведите новые данные (оставьте пустым, чтобы не изменять):")
            
            new_name = input(f"Кличка ({pet_name}): ") or pet_name
            new_type = input(f"Вид ({pet_info[pet_name]['Вид питомца']}): ") or pet_info[pet_name]['Вид питомца']
            new_age = input(f"Возраст ({pet_info[pet_name]['Возраст питомца']}): ") or pet_info[pet_name]['Возраст питомца']
            new_owner = input(f"Владелец ({pet_info[pet_name]['Имя владельца']}): ") or pet_info[pet_name]['Имя владельца']
            
            # Удаляем старую запись и добавляем обновленную
            del pets[ID]
            pets[ID] = {
                new_name: {
                    "Вид питомца": new_type,
                    "Возраст питомца": int(new_age),
                    "Имя владельца": new_owner
                }
            }
            print("\nЗапись обновлена")
        else:
            print("\nПитомец с таким ID не найден")
    except ValueError:
        print("Ошибка: Возраст должен быть числом")

def delete():
    """Удаляет запись о питомце"""
    try:
        ID = int(input("Введите ID питомца для удаления: "))
        if ID in pets:
            del pets[ID]
            print("\nЗапись удалена")
        else:
            print("\nПитомец с таким ID не найден")
    except ValueError:
        print("Ошибка: ID должен быть числом")

# Основной цикл программы
def main():
    print("Добро пожаловать в базу данных ветеринарной клиники!")
    print("Доступные команды: create, read, update, delete, list, stop")
    
    command = ""
    while command != "stop":
        command = input("\nВведите команду: ").lower()
        
        if command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        elif command == "stop":
            print("Работа с базой данных завершена")
        else:
            print("Неизвестная команда. Попробуйте снова")

if __name__ == "__main__":
    main()