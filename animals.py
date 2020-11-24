# Задача №1 "Ферма Дядюшки Джо"
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
#
# Со всеми животными вам необходимо как-то взаимодействовать:

# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)

# Задание 1:
# Нужно реализовать классы животных и определить методы взаимодействия с животными.
# Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
#
# Задание 2:
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

from operator import attrgetter

class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eating(self):
        print('Я животное! И меня сейчас накормили!')

    def voice(self):
        print('Я животное! И я говорю что-то!')


# коза
class Goat(Animals):

    def get_milk(self):
        print('Я коза и я дам вам молока!')

    def eating(self):
        print('Я коза! И меня сейчас накормили!')

    def voice(self):
        print('Меееееее-еее')


# корова
class Cow(Animals):

    def get_milk(self):
        print('Я корова и я дам вам молока!')

    def eating(self):
        print('Я корова! И меня сейчас накормили!')

    def voice(self):
        print('Муууууууу-ууу')


# гусь
class Goose(Animals):

    def get_eggs(self):
        print('Я гусь и снес вам свежие яйца!')

    def eating(self):
        print('Я гусь! И меня сейчас накормили!')

    def voice(self):
        print('Га-га-га-га')


# утка
class Duck(Animals):

    def get_eggs(self):
        print('Я утка и снесла вам свежие яйца!')

    def eating(self):
        print('Я утка! И меня сейчас накормили!')

    def voice(self):
        print('Кря-кря-кря-кря')


# овца
class Sheep(Animals):

    def to_cut(self):
        print('Быстро подстригли мою шерсть!')

    def eating(self):
        print('Я овца! И меня сейчас накормили!')

    def voice(self):
        print('Бееееееее-еее')


# курица
class Chicken(Animals):

    def get_eggs(self):
        print('Я курица и снесла вам свежие яйца!')

    def eating(self):
        print('Я курица! И меня сейчас накормили!')

    def voice(self):
        print('Куд-кудах')


#поиск животного с максимальным весом
def max_weight(list):
        return max(list, key=attrgetter('weight'))


if __name__ == '__main__':

    goose_gray = Goose('Гусь серый', 7)
    goose_white = Goose('Гусь белый', 4)
    cow = Cow('Манька', 100)
    sheep_barashek = Sheep('Овца барашка', 74)
    sheep_kudr = Sheep('Овца кудрявая', 65)
    chicken_ko = Chicken('Ко-ко', 4)
    chicken_ku = Chicken('Кукареку', 8)
    goat_roga = Goat('Коза рога', 28)
    goat_kopyta = Goat('Коза копыта', 23)
    duck = Duck('Утка Кряква', 13)

    ferma = [goose_gray, goose_white, cow, sheep_kudr, sheep_barashek, chicken_ku,
             chicken_ko, goat_roga, goat_kopyta, duck]

    animal_max_weight = max_weight(ferma).name
    print(f'Максимальный вес у {animal_max_weight}')

    sum_weight = 0
    for animal in ferma:
        sum_weight += animal.weight

    print(f'Вес всех животных на ферме {sum_weight} кг')