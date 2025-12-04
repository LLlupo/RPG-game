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
#     'weapons': ['Орб-слизь, Ножи разбойника, Дубинка стеснительного орка, Плеть разбойника, Рыцарский меч, Посох шамана-гоблина, Клинок. Просто клинок., Книга заклинаний'],
#     'poison': ["Розовая слизь, Голубая слизь, Красная слизь, Кровь лесной дриады, Ягодный сок"],
# }
wiki = {
    'Плащ шамана-гоблина': ['ПлАщ, пРоПИТанНЫй ИСКусСТвоМ чуДОдейСТвА ГоБЛиНОв! ЕСЛи оНО У нИХ еСТь? ХыХЫ',
                            [["Магия", 4], ['Защита', 3]],
                            'Броня'],
    'Диадема лесной дриады': ["Цветочная корона жестокой хранительницы леса.",
                              [['Магия', 6], ['Ловкость', 5]],
                              'Броня'],
    'Маска стеснительного орка': ["Чёрная маска предводителя орков.",
                                  [['Защита', 7], ['Очки здоровья', 4]],
                                  'Броня'],
    'Накидка из шкуры оленя-перевёртыша': ["ОТ еЁ вида МНе нЕМНогО жУТкО...",
                                           [['Сила', 5], ['Очки здоровья', 4], ['Защита', 5]],
                                           'Броня'],
    'Пояс разбойника Первого': ["ИлИ ВТОРогО? ТЫ ПоМНиШЬ?",
                                [['Сила', 6], ['Очки здоровья', 2], ['Защита', 6]],
                                'Броня'],
    'Перчатки разбойника Второго': ["Ну тОЧНо ВтОрОГО.",
                                    [['Сила', 5], ['Ловкость', 3], ['Защита', 6]],
                                    'Броня'],
}
class Player:
    def __init__(self):
        self.name = ''
        self.stats = []
        self.equipment = {
            'Броня':'Диадема лесной дриады',
            'Аксессуар': '-',
            'Оружие': '-',
            'poison': '',
        }
        self.inventory = ['Ягодный сок', 'Книга заклинаний', 'Плащ шамана-гоблина']
    def get_stats(self):
        is_fit = 0
        while is_fit != 25:
            stats = {
                'Очки здоровья': randint(3, 10),
                'Сила': randint(2, 10),
                'Магия': randint(1, 10),
                'Ловкость': randint(1, 10),
                'Защита': randint(1, 5),
                'level': 0,
                'experience': 0
            }
            is_fit = sum(stats.values())
        self.stats = stats
        # print("     ЭТО ТЫ\n"
        #       "       |\n"
        #       "       v\n")
        # self.greet()
        # self.re_stats()
        # self.name = input("- КСтаТИ, А МЫ веДЬ С ИМенЕМ еЩЕ не ОПреДЕлиЛиь... КАк НАс ЗоВУт??\n")
        self.name = "CHARA"
        print(f"- КрУТо! {self.name}!")
    def show_all(self):
        self.stats['experience'] = 46
        print(
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀      Уровень: {self.stats['level']}\n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀     \n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀      {(self.stats['experience']//10)*"▓" + ((100 - self.stats['experience'])//10)*"░"} {self.stats['experience']}/{100}\n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀      \n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     ・Очки здоровья: {self.stats["Очки здоровья"]}\n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Сила: {self.stats["Сила"]}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Магия: {self.stats["Магия"]}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀    ・Ловкость: {self.stats["Ловкость"]}\n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀    ・Защита: {self.stats["Защита"]}\n"
        )
        print(f'▐ Броня: {self.equipment['Броня']}  '
              f'▐ Оружие: {self.equipment['Оружие']}  '
              f'▐ Аксессуар: {self.equipment['Аксессуар']}\n')
        print('     ✦ Инвентарь ✦')
        invent = [i for i in self.inventory] + ["Пусто" for j in range(15-len(self.inventory))]
        for i, item in enumerate(invent):
            print(i + 1, '-', item)
        print('\n')
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
    def re_stats(self):
        is_ok = ''
        while is_ok not in ['0','1','2']:
            is_ok = input("- кАК ТеБе ХАраКТЕрИсТИКи? ХоЧЕшь ПОмЕняТЬ? (0 - Сойдёт, 1 - Давай поменяем, 2 - Поменяй ты)\n")
        if is_ok == '1':
            print("- ЛАдНО! НАзНАЧаЙ в ТАкОМ ПОряДКе: ЗдОроВЬЕ, СИла, МаГИя, ЛОвкоСТь, ЗАЩиТа. СМоТри ТоЛЬКО, В СУмМЕ ДоЛЖно БыТь 25!")
            stats_keys = [i for i in self.stats.keys()]
            soul_points = 25
            while soul_points != 0:
                try:
                    planned_stats = input('- ВВодИ 5 ЗнаЧЕнИй. ЧеРЕз ПроБЕЛ!\n')
                    planned_stats = [int(i) for i in planned_stats.split()]
                    for i, key in enumerate(stats_keys[:-1]):
                        self.stats[key] = planned_stats[i]
                        soul_points -= planned_stats[i]
                    if soul_points != 0:
                        print(f"- ЕЩё ОСТАлОСь {soul_points}! ДАвАЙ ПО НОвОЙ.")
                        soul_points = 25
                    else:
                        self.greet()
                        self.re_stats()
                except:
                    print("- ЧТО-тО тЫ НАмуДрИл... ПоВТоРи?")
                    self.re_stats()

        elif is_ok == '2':
            print("\n- ЛАДНа! СмОТри!\n")
            self.get_stats(0)
        elif is_ok == '0':
            print('- МНЕ тОЖЕ ЭтИ НрАВятСЯ :D')
    def get_hurt(self, enemy):
        damage = max(0,(enemy.strength-self.stats['defense']))
        self.stats['health'] = max(self.stats['health'] - damage, 0)
        print(f'Существо {enemy.kind} атакует!')
        print(f"Вам нанесли {damage} урона. У вас осталось {self.stats['health']} ОЗ.")
    def show_inventory(self):
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
player = Player()
print("- ПРиВЕи! ДоБРо ПОжаЛоВать в МИр! КтО я? НУ... КтО-тО? БЕз ПОНЯтиЯ, КтО Я. ЗаТО ЗнАЮ, ЧТО ты - ЧеЛОвЕкоПоДОбнАя сЛИзЬ!\n")
player.get_stats()
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
player.show_all()
