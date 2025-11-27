from random import *
def new_player():
    #name = input("Добро пожаловать, Странник! Вы... Хм... Никогда не видел такой странной души. Кто вы?\n")
    name = 'Chara'
    def get_stats(level):
        is_fit = 33 + level*5
        while is_fit != 25+level*5:
            stats = {
                'health': randint(3, 10),
                'strength': randint(2, 10),
                'magic': randint(1, 10),
                'speed': randint(1, 10),
                'defense': randint(1, 5),
                'level': level
            }
            is_fit = sum(stats.values())
        def greet():
            print(
                f'Хорошо, {name}... Судя по всему вы обладаете характеристиками:\n  '
                f'Очки здоровья: {stats["health"]}\n  '
                f'Сила: {stats["strength"]}\n  '
                f'Магия: {stats["magic"]}\n  '
                f'Ловкость: {stats["speed"]}\n  '
                f'Защита: {stats["defense"]}\n  '
            )
        greet()
        is_ok = int(input("Хотите переназначить? (0 - Нет, 1 - Да, 2 - Рандом)\n"))
        if is_ok == 1:
            print("Хорошо... У вас есть 25 очков души. Назначайте их как пожелаете в таком порядке: Очки здоровья, Сила, Магия, Ловкость, Защита.")
            stats_keys = [i for i in stats.keys()]
            soul_points = 25
            while soul_points != 0:
                planned_stats = input('Введите 5 значений через пробел: ')
                planned_stats = [int(i) for i in planned_stats.split()]
                for i, key in enumerate(stats_keys[:-1]):
                    stats[key] = planned_stats[i]
                    soul_points -= planned_stats[i]
                if soul_points != 0:
                    print(f"Осталось очков: {soul_points}. Попробуй еще раз.")
                    soul_points = 25
                else:
                    greet()
        elif is_ok == 2:
            get_stats(0)
    get_stats(0)
new_player()
class Player:
    def __init__(self, name):
        self.name = name
        self.stats = []
        # self.name = 'Chara'
    def get_stats(self, level):
        is_fit = 33 + level * 5
        while is_fit != 25 + level * 5:
            stats = {
                'health': randint(3, 10),
                'strength': randint(2, 10),
                'magic': randint(1, 10),
                'speed': randint(1, 10),
                'defense': randint(1, 5),
                'level': level
            }
            is_fit = sum(stats.values())
        self.stats = stats
        self.greet()
        self.re_stats()
    def greet(self):
        print(
            f'Хорошо, {self.name}... Судя по всему вы обладаете характеристиками:\n  '
            f'Очки здоровья: {self.stats["health"]}\n  '
            f'Сила: {self.stats["strength"]}\n  '
            f'Магия: {self.stats["magic"]}\n  '
            f'Ловкость: {self.stats["speed"]}\n  '
            f'Защита: {self.stats["defense"]}\n  '
        )
    def re_stats(self):
        is_ok = int(input("Хотите переназначить? (0 - Нет, 1 - Да, 2 - Рандом)\n"))
        if is_ok == 1:
            print("Хорошо... У вас есть 25 очков души. Назначайте их как пожелаете в таком порядке: Очки здоровья, Сила, Магия, Ловкость, Защита.")
            stats_keys = [i for i in self.stats.keys()]
            soul_points = 25
            while soul_points != 0:
                planned_stats = input('Введите 5 значений через пробел: ')
                planned_stats = [int(i) for i in planned_stats.split()]
                for i, key in enumerate(stats_keys[:-1]):
                    self.stats[key] = planned_stats[i]
                    soul_points -= planned_stats[i]
                if soul_points != 0:
                    print(f"Осталось очков: {soul_points}. Попробуй еще раз.")
                    soul_points = 25
                else:
                    self.greet()
                    self.re_stats()
        elif is_ok == 2:
            self.get_stats(0)
name = 'Chara'
player = Player(name)
player.get_stats(0)
class Creature:
    def __init__(self, kind, health=(3,10), strength=(1,10), magic=(1,10), speed=(1,10), defense=(1,5), stats_base=25, level=0):
        self.kind = kind
        is_fit = stats_base + level * 5
        while is_fit+1 > stats_base + level * 5:
            self.health = randint(*health)
            self.strength = randint(*strength)
            self.magic = randint(*magic)
            self.speed = randint(*speed)
            self.defense = randint(*defense)
            is_fit = self.health+self.strength+self.magic+self.speed+self.defense
    def show_stats(self):
        print(
            f'Существо {self.kind}\n'
            f'{"-"*20}\n'
            f'Очки здоровья: {self.health}\n'
            f'Сила: {self.strength}\n'
            f'Магия: {self.magic}\n'
            f'Ловкость: {self.speed}\n'
            f'Защита: {self.defense}\n'
        )

common_goblin = Creature('Гоблин',(3,6),(3,6),(0,0),(2,5),(2,5))
mage_goblin = Creature("Гоблин-маг",(3,6),(1,3),(4,7),(2,4),(2,5))
# mage_goblin.show_stats()
