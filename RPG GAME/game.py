from random import *

Сила = 'strength'
# wiki = {
#     'armor': {
#         'Плащ шамана-гоблина': 'Плащ, пропитанный искусством чудодейства гоблинов. Если таковое существует.',
#         'Диадема лесной дриады': "Цветочная корона жестокой хранительницы леса.",
#         'Маска стеснительного орка': "Чёрная маска предводителя орков.",
#         'Накидка из шкуры оленя-перевёртыша': "От её вида немного жутко.",
#         'Пояс разбойника Первого': "Или Второго?",
#         'Перчатки разбойника Второго': "Ну точно Второго."
#     },
#     'accessory': ['Клык звёздной лисицы, Кулон лесной дриады, Рог оленя-перевёртыша, Серьга гоблина, Талисман Сияющей слизи,'],
#     'weapons': ['Орб-слизь, Ножи разбойника, Дубинка стеснительного орка, Плеть разбойника, Рыцарский меч, Посох шамана-гоблина, Клинок. Просто клинок.'],
#     'poison': ["Розовая слизь, Голубая слизь, Красная слизь, Кровь лесной дриады, Ягодный сок"],
# }
wiki = {
    'Плащ шамана-гоблина': ['Плащ, пропитанный искусством чудодейства гоблинов. Если оно у них есть?',
                            [["Магия", 4], ['Защита', 3]],
                            'armor'],
    'Диадема лесной дриады': ["Цветочная корона жестокой хранительницы леса.",
                              [['Магия', 6], ['Ловкость', 5]],
                              'armor'],
    'Маска стеснительного орка': ["Чёрная маска предводителя орков.",
                                  [['Защита', 7], ['Очки здоровья', 4]],
                                  'armor'],
    'Накидка из шкуры оленя-перевёртыша': ["От её вида немного жутко.",
                                           [['Сила', 5], ['Очки здоровья', 4], ['Защита', 5]],
                                           'armor'],
    'Пояс разбойника Первого': ["Или Второго?",
                                [['Сила', 6], ['Очки здоровья', 2], ['Защита', 6]],
                                'armor'],
    'Перчатки разбойника Второго': ["Ну точно Второго.",
                                    [['Сила', 5], ['Ловкость', 3], ['Защита', 6]],
                                    'armor'],
}
class Player:
    def __init__(self, name):
        self.name = name
        self.stats = []
        self.equipment = {
            'armor':'Диадема лесной дриады',
            'accessory': '-',
            'weapon': '-',
            'poison': '',
        }
        # self.inventory = {
        #     'armor': [],
        #     'weapons': ["Книга заклинателя"],
        #     'poisons': ['Ягодный сок'],
        # }
        self.inventory = ['Ягодный сок', 'Книга заклинателя', 'Плащ шамана-гоблина']
        # self.name = 'Chara'
    def get_stats(self, level):
        is_fit = 0
        while is_fit != 25 + level * 5:
            stats = {
                'Очки здоровья': randint(3, 10),
                'Сила': randint(2, 10),
                'Магия': randint(1, 10),
                'Ловкость': randint(1, 10),
                'Защита': randint(1, 5),
                'level': level
            }
            is_fit = sum(stats.values())
        self.stats = stats
        self.greet()
        # self.re_stats()
    def show_all(self):
        print(
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀  \n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀ \n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀    ・Очки здоровья: {self.stats["Очки здоровья"]}\n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀    ・Сила: {self.stats["Сила"]}\n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     ・Магия: {self.stats["Магия"]}\n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Ловкость: {self.stats["Ловкость"]}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Защита: {self.stats["Защита"]}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀ \n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀ \n"
        )
        print(f'Броня: {self.equipment['armor']}\n'
              f'Аксессуар: {self.equipment['accessory']}\n'
              f'Оружие: {self.equipment['weapon']}\n')
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(self.inventory):
            print(i + 1, '-', item)
    def greet(self):
        print(
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀  \n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀ \n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀    ・Очки здоровья: {self.stats["Очки здоровья"]}\n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀    ・Сила: {self.stats["Сила"]}\n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     ・Магия: {self.stats["Магия"]}\n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Ловкость: {self.stats["Ловкость"]}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Защита: {self.stats["Защита"]}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀ \n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀ \n"
        )
        # print(
        #     f'Хорошо, {self.name}... Судя по всему вы обладаете характеристиками:\n  '
        #     f'Очки здоровья: {self.stats["Очки здоровья"]}\n    '
        #     f'Сила: {self.stats["Сила"]}\n  '
        #     f'Магия: {self.stats["Магия"]}\n  '
        #     f'Ловкость: {self.stats["Ловкость"]}\n  '
        #     f'Защита: {self.stats["Защита"]}\n  '
        # )
    def re_stats(self):
        is_ok = int(input("Хотите переназначить? (0 - Нет, 1 - Да, 2 - Рандом)\n"))
        if is_ok == 1:
            print("Хорошо... У вас есть 25 очков души. Назначайте их как пожелаете в таком порядке: Очки здоровья, Сила, Магия, Ловкость, Защита.")
            stats_keys = [i for i in self.stats.keys()]
            soul_points = 25
            while soul_points != 0:
                try:
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
                except ValueError:
                    print("Что-то пошло не так... Повтори?")
                    self.re_stats()

        elif is_ok == 2:
            self.get_stats(0)
    def get_hurt(self, enemy):
        damage = max(0,(enemy.strength-self.stats['defense']))
        self.stats['health'] = max(self.stats['health'] - damage, 0)
        print(f'Существо {enemy.kind} атакует!')
        print(f"Вам нанесли {damage} урона. У вас осталось {self.stats['health']} ОЗ.")
    def show_inventory(self):
        print(
            f'⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀  \n'
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀ \n"
            f'⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀     Броня: {self.equipment['armor']}\n'
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀ \n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀      Аксессуар: {self.equipment['accessory']}\n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀ \n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀     Оружие: {self.equipment['weapon']}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀ \n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀ \n"
        )
        # print(f"В сумке лежит:", *[i + ',' if self.inventory[-1] != i else i for i in self.inventory])
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(self.inventory):
            print(i+1,'-', item)
    def unequip(self, item):
        print(f"\nВы сняли: {item}")
        self.equipment[wiki[item][-1]] = '-'
        self.inventory.append(item)
        for i in wiki[item][1]:
            print(f"Характеристика {i[0]} упала на {i[1]}")
            self.stats[i[0]] -= i[1]
    def equip(self, item):
        if self.equipment[wiki[item][-1]] == '-':
            self.equipment[wiki[item][-1]] = item
            self.inventory.remove(item)
            print(f"\nВы надели: {item}")
        elif self.equipment[wiki[item][-1]] != '-':
            yesno = 0
            while yesno not in ['1','2']:
                print(f"Эта категория уже занята: {self.equipment[wiki[item][-1]]}. Хотите сменить? (1 - Да, 2 - Нет)")
                yesno = input()
            if yesno == '1':
                self.unequip(self.equipment[wiki[item][-1]])
                return self.equip(item)
            else:
                return print("")
        for i in wiki[item][1]:
            print(f"Характеристика {i[0]} возросла на {i[1]}")
            self.stats[i[0]] += i[1]
name = 'Chara'
player = Player(name)
player.get_stats(0)
class Creature:
    def __init__(self, kind, health=(3,10), strength=(1,10), magic=(1,10), speed=(1,10), defense=(1,5), stats_base=25, level=0):
        self.kind = kind
        is_fit = 0
        while is_fit != stats_base + level * 5:
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
    def attack(self):
        player.get_hurt(self)
    def get_hurt(self, enemy):
        damage = max(0,(enemy.strength-self.stats['defense']))
        self.stats['health'] = max(self.stats['health'] - damage, 0)


# common_goblin = Creature('Гоблин',(3,6),(3,6),(0,0),(2,5),(2,5))
# mage_goblin = Creature("Гоблин-шаман",(3,6),(1,3),(4,7),(2,4),(2,5))
# deer_skinwalker = Creature("Олень-перевёртыш", (15,20), (8,14), (2,5), (7,10), (3,7), 30)
# mage_goblin.show_stats()
# player.examine(common_goblin)
# player.get_hurt(common_goblin)
# player.show_inventory()
# # deer_skinwalker.show_stats()
# # player.equip('Плащ шамана-гоблина')
# player.show_inventory()
player.show_all()
