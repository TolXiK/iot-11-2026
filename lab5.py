from enum import Enum

class Type(Enum):
    bar = 1
    chocolate = 2
    popcorn = 3
    bubblegum = 4

print(Type.bar)    # вивід сам тип
print(Type.bar.value) # вивести саме значення


class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.candy_type = candy_type

    def check_mass(self):
        if self.mass * self.amount > 2000:
            print("You're on a diet!")
        else:
            print("What delicious candies!")

    def text(self):
        print(f'{self.name} | {self.mass} g | {self.amount} pcs | {self.price} UAH')


class Dinner:
    def __init__(self, day, time):
        self.day = day
        self.time = time
        self.candy_dinner = [] # створення списку куди ми будемо зберігати обєкти класу кенді

    def add_candy(self, candy):
        self.candy_dinner.append(candy)

    def check_dinner(self):
        print(f'Dinner: {self.day} at {self.time}')

        for candy in self.candy_dinner:
            candy.text()


def find_expensive(candy_dinner, name=''):
    found = []

    for candy in candy_dinner:
        if name == '' or candy.name == name:
            found.append(candy)

    for i in range(len(found)):
        for j in range(i + 1, len(found)):
            if found[i].price < found[j].price:
                found[i], found[j] = found[j], found[i]

    print("Top 3 most expensive candies:")

    for i in range(min(3, len(found))):
        found[i].text()


c1 = Candy("Snickers", 50, 5, 35, Type.bar)
c2 = Candy("Mars", 45, 3, 30, Type.bar)
c3 = Candy("Orbit", 14, 2, 25, Type.bubblegum)
c4 = Candy("Popcorn", 100, 4, 60, Type.popcorn)
c5 = Candy("Chocolate", 250, 10, 80, Type.chocolate)

candy_dinner = [c1, c2, c3, c4, c5]
dinner = Dinner('Monday', '15:00')

dinner.add_candy(c1)
dinner.add_candy(c2)
dinner.add_candy(c3)

dinner.check_dinner()

print()

c4.check_mass()
c5.check_mass()

print()

find_expensive(candy_dinner)



dinner2 = Dinner('Today','15:00')
dinner2.add_candy(c4)
dinner2.add_candy(c5)

for candy in dinner2.candy_dinner:
    print(f'name candy:{candy.name} {candy.price} grn')