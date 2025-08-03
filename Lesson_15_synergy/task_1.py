class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Класс наследует всё от Transport без изменений

# Создаём объект Autobus с указанными параметрами
bus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию в требуемом формате
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")