class House:
    houses_history = []  # Атрибут класса для хранения истории названий домов

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю сразу при создании объекта
        instance = super().__new__(cls)  # Создаем новый экземпляр
        cls.houses_history.append(args[0])  # args[0] содержит название дома
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Вывод: ЖК Акация снесён, но он останется в истории
del h3  # Вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление последнего объекта
del h1  # Вывод: ЖК Эльбрус снесён, но он останется в истории