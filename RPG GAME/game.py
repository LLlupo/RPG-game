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
        print(
            f'Хорошо, {name}... Судя по всему вы обладаете характеристиками:\n  '
            f'Очки здоровья: {stats["health"]}\n  '
            f'Физический урон: {stats["strength"]}\n  '
            f'Магический урон: {stats["magic"]}\n  '
            f'Ловкость: {stats["speed"]}\n  '
            f'Защита: {stats["defense"]}\n  '
        )
        # is_ok = int(input("Хотите переназначить? (0 - Нет, 1 - Да, 2 - Рандом)\n"))
        # if is_ok == 1:
        #     print("Хорошо... Т")
        # elif is_ok == 2:
        #     get_stats(0)
    get_stats(0)
new_player()
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
            f'{'-'*20}\n'
            f'Очки здоровья: {self.health}\n'
            f'Физический урон: {self.strength}\n'
            f'Магический урон: {self.magic}\n'
            f'Ловкость: {self.speed}\n'
            f'Защита: {self.defense}\n'
        )

common_goblin = Creature('Гоблин',(3,6),(3,6),(0,0),(2,5),(2,5))
mage_goblin = Creature("Гоблин-маг",(3,6),(1,3),(4,7),(2,4),(2,5))
# mage_goblin.show_stats()