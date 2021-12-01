cof = int(input("Выберите напиток (Espresso-1, Americano-2, DarkRoast-3): "))
mil = int(input("Добавить молоко (1-Да/2-Нет): "))
sug = input("Нужен ли сахар (1-Да/2-Нет): ")
whi = input("Нужен ли Whip (1-Да/2-Нет): ")


class Coffee():
    def getDescription(self):
        return self.name

    pass

    def getCost(self):
        return self.cost

    pass
    def s
    def __str__(self):
        return self.getCost()





class Espresso(Coffee):
    name = 'Espresso'
    cost = 2


class Americano(Coffee):
    name = 'Americano'
    cost = 2.5


class DarkRoast(Coffee):
    name = 'DarkRoast'
    cost = 3


class Milk(Coffee):
    name = 'Молоко'
    cost = 0.5


class Sugar(Coffee):
    name = 'Сахар'
    cost = 0.2


class Whip(Coffee):
    name = 'Whip'
    cost = 0.5


mil = Milk()
sug = Sugar()
whi = Whip()

if cof == 1 and mil==1:
    cof = Espresso()
    print(cof.getDescription())
    print(mil.getDescription())
    print(cof.__str__()+mil.__str__())
elif cof == 2:
    cof = Americano()
    cof.getDescription()
    cof.getCost()
else:
    cof = DarkRoast()
    cof.getDescription()
    cof.getCost()
