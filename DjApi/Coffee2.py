class Coffee:
    def __init__(self, name='Brazil black coffee', price=3):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


class Americano:
    def __init__(self, name='African black coffee', price=5):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


class DarkRoast:
    def __init__(self, name='black coffee iz banki', price=1):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


class Milk:
    def __init__(self, name='молоко 3,2%', price=0.5):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


class Sugar:
    def __init__(self, name='сахар', price=0.25):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


class Whip:
    def __init__(self, name='свежайшие сливки Альпийских коровок', price=0.7):
        self.price = price
        self.name = name

    def getCost(self):
        return f'{self.price}'

    def getDescription(self):
        return f'{self.name}'


c = Coffee()
a = Americano()
d = DarkRoast()
m = Milk()
s = Sugar()
w = Whip()

print(
    'Приветствую Вас в нашем виртуальном кафе "Рамонак". Я ва персональный оффициант робот Василий! Хотели бы ознакомиться с нашим меню? 1 - Да, 2 - Нет')
z = int(input())
if z == 1:
    price = 0
    cheak = []
    print('У нас в меню сегодня имеется:\n 1 - Coffee: 3.0 $ \n 2 - Americano: 5.0 $ \n 3 - DarkRoast: 1.0 $ \n Сделайте Ваш выбор пожалуйста:')
    k = int(input())
    while k != 0:
        print('Какое количество порций желаете?')
        n = input()
        if k == 1:
            price += float(c.getCost()) * float(n)
            cheak.append(c.getDescription() + ' - ' + n + ' порц.' + ': +' + str(float(c.getCost()) * float(n)) + '$')
        elif k == 2:
            price += float(a.getCost()) * float(n)
            cheak.append(a.getDescription() + ' - ' + n + ' порц.' + ': +' + str(float(a.getCost()) * float(n)) + '$')
        elif k == 3:
            price += float(d.getCost()) * float(n)
            cheak.append(d.getDescription() + ' - ' + n + ' порц.' + ': +' + str(float(d.getCost()) * float(n)) + '$')
        print('У нас в меню имеются добавки к кофе:\n 1 - Milk: 0.5 $ \n 2 - Sugar: 0.25 $ \n 3 - Whip: 0.7 $ \n 0 - Дальше  \n Сделайте Ваш выбор пожалуйста:')
        v = int(input())
        while v != 0:
            print('Какое количество порций желаете?')
            g = input()
            if v == 1:
                price += float(m.getCost()) * float(g)
                cheak.append(m.getDescription() + ' - ' + g + ' порц.' + ': +' + str(float(m.getCost()) * float(g)) + '$')
            elif v == 2:
                price += float(s.getCost()) * float(g)
                cheak.append(s.getDescription() + ' - ' + g + ' порц.' + ': +' + str(float(s.getCost()) * float(g)) + '$')
            elif v == 3:
                price += float(w.getCost()) * float(g)
                cheak.append(d.getDescription() + ' - ' + g + ' порц.' + ': +' + str(float(w.getCost()) * float(g)) + '$')
            print('Желаете ещё что-то добавить:\n 1 - Milk: 0.5 $ \n 2 - Sugar: 0.25 $ \n 3 - Whip: 0.7 $ \n 0 - Дальше  \n Сделайте Ваш выбор пожалуйста:')
            v = int(input())
        print('У нас в меню сегодня имеется:\n 1 - Coffee: 3.0 $ \n 2 - Americano: 5.0 $ \n 3 - DarkRoast: 1.0 $ \n 0 - Дальше \n Сделайте Ваш выбор пожалуйста:')
        k = int(input())

    print('...ПИ - ПИ - ПИ...ВНИМАНИЕ!!!....идёт печать чека....')
    print('**   **   **       **   **   **       **   **   **')
    print('  ** ** **           ** ** **           ** ** **')
    print('    ****               ****               ****')
    print('  ** ** **           ** ** **           ** ** **')
    print('**   **   **       **   **   **       **   **   **')
    print()
    print('____________________')
    print('ВАШ СЧЁТ:')
    for i in cheak:
        print(i, end='\n')
    print('____________________')
    print('Итого:', price, '$')
    print('--------------------')
    print('Интересный факт:')
    print(random.choice(hist))
    with open('1.txt', 'w') as cool:
        cool.write('ВАШ СЧЁТ:' + '\n' + '\n')
        for i in cheak:
            cool.write(str(i) + '\n')
        cool.write('\n' + '____________________' + '\n')
        cool.write('Итого:' + str(price) + '$')
        cool.write('\n' + str(random.choice(hist)))