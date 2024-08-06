class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(f'ЖК {args[0]}')
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'ЖК {self.name} снесён, но он останется в истории')


h1 = House('Космос', 20)
print(House.houses_history)
h2 = House('Great Marble', 19)
print(House.houses_history)
h3 = House('Chesterfield', 54)
print(House.houses_history)
del h1
del h2
print(House.houses_history)

while True:
    ''
