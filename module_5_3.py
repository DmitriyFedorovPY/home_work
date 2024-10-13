from idna import valid_label_length


class House:
    def __init__(self,name,floor):
        self.name = name
        self.number_of_floors = floor

    def __str__(self):
        str = (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return str

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors == sc

    def __len__(self):
        return self.number_of_floor

    def __lt__(self,other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self,other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self,other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self,other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self,other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        res = self.number_of_floors + value
        return res

    def __radd__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

#почему при запросе print h1 после других операций, выводится не метод __str__ полностью, а только цифра?