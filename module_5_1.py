class House:
    def __init__(self,name,floor):
        self.name = name
        self.number_of_floors = floor
        # go_to(new_floor)

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i + 1)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)