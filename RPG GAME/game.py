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
                            [["Урон", 4], ['Защита', 3]],
                            'Броня'],
    'Диадема лесной дриады': ["Цветочная корона жестокой хранительницы леса.",
                              [['Урон', 6], ['Ловкость', 5]],
                              'Броня'],
    'Маска стеснительного орка': ["Чёрная маска предводителя орков.",
                                  [['Защита', 7], ['Очки здоровья', 4]],
                                  'Броня'],
    'Накидка из шкуры оленя-перевёртыша': ["ОТ еЁ вида МНе нЕМНогО жУТкО...",
                                           [['Урон', 5], ['Очки здоровья', 4], ['Защита', 5]],
                                           'Броня'],
    'Пояс разбойника Первого': ["ИлИ ВТОРогО? ТЫ ПоМНиШЬ?",
                                [['Урон', 6], ['Очки здоровья', 2], ['Защита', 6]],
                                'Броня'],
    'Перчатки разбойника Второго': ["Ну тОЧНо ВтОрОГО.",
                                    [['Урон', 5], ['Ловкость', 3], ['Защита', 6]],
                                    'Броня'],
}
wiki_monsters = {
    "Гоблин":[(3,6), (3,6), (2,5), (2,5), (2,4), 15],
    "Гоблин-шаман":[(3,6), (4,7), (2,4), (2,5), (3,5), 20],
    "Орк":[(5,9), (6,8), (2,4), (4,6), (13,16), 25],
    "Стеснительный орк":[(10,16), (7,10), (2,4), (7,12), (22,30), 34],
    "Голубая слизь":[(5,8), (3,5), (13,18), (2,5), (8,15), 34],
    "Розовая слизь":[(13,16), (3,5), (2,5), (2,5), (8,15), 30],
    "Красная слизь":[(3,6), (8,10), (2,5), (2,5), (8,15), 25],
    "Олень-перевёртыш":[(15,20), (8,14), (7,10), (3,7), (13,20), 35],
    "Разбойник":[],
    "Разбойник Первый":[],
    "Разбойник Второй":[],
    "Дриада":[],
    "Шипастая Дриада":[],
    "???":[],
}
class Player:
    def __init__(self):
        self.name = ''
        self.stats = []
        self.level, self.experience, self.free_points = -1, 0, 0
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
                'Урон': randint(2, 10),
                'Ловкость': randint(1, 10),
                'Защита': randint(1, 5),
            }
            is_fit = sum(stats.values())
        self.stats = stats
        self.get_level()
        # print("     ЭТО ТЫ\n"
        #       "       |\n"
        #       "       v\n")
        # self.greet()
        # self.re_stats()
        # self.name = input("- КСтаТИ, А МЫ веДЬ С ИМенЕМ еЩЕ не ОПреДЕлиЛиь... КАк НАс ЗоВУт??\n")
        self.name = "CHARA"
        print(f"- КрУТо! {self.name}!")
    def get_level(self):
        self.level += 1
        self.free_points += self.level * 5
        match self.level:
            case 0: self.exp_next = 10
            case 1: self.exp_next = 50
            case 2: self.exp_next = 100
            case 3: self.exp_next = 500
            case 4: self.exp_next = 1000
        self.exp_bar = (self.experience // (self.exp_next//10))*'▓' + (10-len((self.experience // (self.exp_next//10))*'▓'))*'░'
    def show_all(self):
        print('\n'
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀      \n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀     Уровень: {self.level}\n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀      \n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀     {self.exp_bar} {self.experience}/{self.exp_next}\n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     \n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Очки здоровья: {self.stats['Очки здоровья']}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Урон: {self.stats['Урон']}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀    ・Ловкость: {self.stats['Ловкость']}\n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀    ・Защита: {self.stats['Защита']}\n"
        )
        print(f'▐ Броня: {self.equipment["Броня"]}  '
              f'▐ Оружие: {self.equipment["Оружие"]}  '
              f'▐ Аксессуар: {self.equipment["Аксессуар"]}\n')
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(self.inventory):
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
                        if soul_points < 0:
                            print(f'- Да, В МиНУС ПОшлО!')
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
        damage = max(0,(enemy.damage-self.stats['defense']))
        self.stats['health'] = max(self.stats['health'] - damage, 0)
        print(f'Существо {enemy.kind} атакует!')
        print(f"Вам нанесли {damage} урона. У вас осталось {self.stats['health']} ОЗ.")
    def show_inventory(self):
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(self.inventory):
            print(i+1,'-', item)
    def unequip(self, item):
        print(f"\n- Мы СнЯЛиИ: {item}")
        self.equipment[wiki[item][-1]] = '-'
        self.inventory.append(item)
        for i in wiki[item][1]:
            print(f"- оЙ! ХАрАКТЕриСТиКа {i[0]} уПАлА на {i[1]} D:")
            self.stats[i[0]] -= i[1]
    def equip(self, item):
        if self.equipment[wiki[item][-1]] == '-':
            self.equipment[wiki[item][-1]] = item
            self.inventory.remove(item)
            print(f"\n- ОБнОВка!! {item}")
        elif self.equipment[wiki[item][-1]] != '-':
            yesno = 0
            while yesno not in ['1','2']:
                print(f"- ЭтА каТЕгОРИя уЖЕ зАНЯтА: {self.equipment[wiki[item][-1]]}. ПОмЕнЯеМ? (1 - Да, 2 - Нет)")
                yesno = input()
            if yesno == '1':
                self.unequip(self.equipment[wiki[item][-1]])
                return self.equip(item)
            else:
                return print("")
        for i in wiki[item][1]:
            print(f"- ХарАКтеРИстИКА {i[0]} ВоЗРОсЛа нА {i[1]}! :D")
            self.stats[i[0]] += i[1]
player = Player()
print("- ПРиВЕи! ДоБРо ПОжаЛоВать в МИр! КтО я? НУ... КтО-тО? БЕз ПОНЯтиЯ, КтО Я. ЗаТО ЗнАЮ, ЧТО ты - ЧеЛОвЕкоПоДОбнАя сЛИзЬ!\n")
player.get_stats()
class Creature:
    def __init__(self, kind, health=(3,10), damage = (1,10), speed=(1,10), defense=(1,5), experience=(3,6), stats_base=25):
        self.level = randint(player.level-1,player.level+1)
        self.level = 0
        self.kind = kind
        is_fit = 0
        while is_fit != (stats_base + self.level * 5):
            self.health = randint(*health)
            self.damage = randint(*damage)
            self.speed = randint(*speed)
            self.defense = randint(*defense)
            is_fit = self.health+self.damage+self.speed+self.defense
    def show_stats(self):
        print(
            f'Существо {self.kind}\n'
            f'{"-"*20}\n'
            f'Очки здоровья: {self.health}\n'
            f'Урон: {self.damage}\n'
            f'Ловкость: {self.speed}\n'
            f'Защита: {self.defense}\n'
        )
    def attack(self):
        player.get_hurt(self)
    def get_hurt(self, enemy):
        hurt = max(0,(enemy.damage-self.stats['defense']))
        self.stats['health'] = max(self.stats['health'] - hurt, 0)

def menu(player):
    def mon_meet(amount = randint(1,3)):
        g = '- Ой, НаПАдаЮТ!' if randint(0,1) == 0 else '- МонСтРЫ, моНсТры!'
        print(g)
        cur_mon = [choice(list(wiki_monsters.keys())[:-1]) for i in range(amount)]
        print(cur_mon, amount, '\n')
        cur_mon = [Creature(i, *wiki_monsters[i]) for i in cur_mon]
        for i in cur_mon:
            i.show_stats()
    mon_meet()
menu(player)

# common_goblin = Creature('Гоблин',(3,6),(3,6),(2,5),(2,5),(3,5),15)
# mage_goblin = Creature("Гоблин-шаман",(3,6),(4,7),(2,4),(2,5), (4,6),20)
# magge = Creature("Стеснительный орк", *wiki_monsters['Стеснительный орк'])
# magge.show_stats()
# deer_skinwalker = Creature("Олень-перевёртыш", (15,20), (8,14), (7,10), (3,7), 30)
# mage_goblin.show_stats()
# player.examine(common_goblin)
player.show_all()
# for i in wiki_monsters.keys():
#     cr = Creature(i, *wiki_monsters[i])
#     cr.show_stats()
