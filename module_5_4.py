class House:
    houses_history = []

    def __new__(cls, name,floor):
        cls.houses_history.append(name)
        return super(House, cls).__new__(cls)


    def __init__(self,name,floor):
        self.name = name
        self.number_of_floors = floor

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    # def __str__(self):
    #     str = (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    #     return str


    # def __eq__(self, other):
    #     if not isinstance(other, (int, House)):
    #         raise TypeError("Операнд справа должен иметь тип int или Clock")
    #
    #     sc = other if isinstance(other, int) else other.number_of_floors
    #     return self.number_of_floors == sc
    #
    # def __len__(self):
    #     return self.number_of_floor
    #
    # def __lt__(self,other):
    #     return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self,other):
    #     return self.number_of_floors <= other.number_of_floors
    #
    # def __gt__(self,other):
    #     return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self,other):
    #     return self.number_of_floors >= other.number_of_floors
    #
    # def __ne__(self,other):
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, value):
    #     res = self.number_of_floors + value
    #     return res
    #
    # def __radd__(self, value):
    #     return self.number_of_floors + value
    #
    # def __iadd__(self, value):
    #     return self.number_of_floors + value



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)