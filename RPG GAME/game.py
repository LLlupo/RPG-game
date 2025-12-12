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
    'Плащ шамана-гоблина': ['- ПлАщ, пРоПИТанНЫй ИСКусСТвоМ чуДОдейСТвА ГоБЛиНОв! ЕСЛи оНО У нИХ еСТь? ХыХЫ\n',
                            [["Урон", 4], ['Защита', 3]],
                            'Броня'],
    'Диадема лесной дриады': ["- Цветочная корона жестокой хранительницы леса.\n",
                              [['Урон', 6], ['Ловкость', 5]],
                              'Броня'],
    'Маска стеснительного орка': ["- ЧёРнАЯ мАСкА пРеДВоДиТЕлЯ оРКоВ. И ГдЕ оН ТоЛьКО ТАкую вЗяЛ, ХмМ.\n",
                                  [['Защита', 7], ['Очки здоровья', 4]],
                                  'Броня'],
    'Накидка из шкуры оленя-перевёртыша': ["- ОТ еЁ вида МНе нЕМНогО жУТкО...\n",
                                           [['Урон', 5], ['Очки здоровья', 4], ['Защита', 5]],
                                           'Броня'],
    'Пояс разбойника Первого': ["- ИлИ ВТОРогО? ТЫ ПоМНиШЬ?\n",
                                [['Урон', 8], ['Очки здоровья', 2], ['Защита', 6]],
                                'Броня'],
    'Перчатки разбойника Второго': ["- Ну тОЧНо ВтОрОГО.\n",
                                    [['Урон', 10], ['Ловкость', 3], ['Защита', 6]],
                                    'Броня'],
    'Книга заклинаний': ['- КАкаЯ кНижкАа :З\n',
                         [['Урон', 6]],
                         'Орудие']
}
wiki_monsters = {
    "Гоблин": [(3,6), (3,6), (2,5), (2,5), (2,4), 15,
               ['Серьга гоблина', 'Ягодный сок', 'Посох шамана-гоблина']],
    "Гоблин-шаман": [(3,6), (4,7), (2,4), (2,5), (3,5), 20,
                     ['Плащ шамана-гоблина', 'Книга заклинаний', 'Ягодный сок']],
    "Орк": [(5,9), (6,8), (2,4), (4,6), (13,16), 25],
    "Стеснительный орк": [(10,16), (7,10), (2,4), (7,12), (22,30), 34],
    "Голубая слизь": [(5,8), (3,5), (13,18), (2,5), (8,15), 34],
    "Розовая слизь": [(13,16), (3,5), (2,5), (2,5), (8,15), 30],
    "Красная слизь": [(3,6), (8,10), (2,5), (2,5), (8,15), 25],
    "Олень-перевёртыш": [(15,20), (8,14), (7,10), (3,7), (13,20), 35],
    "Разбойник":[],
    "Разбойник Первый":[],
    "Разбойник Второй":[],
    "Дриада":[],
    "Шипастая Дриада":[],
    "???":[],
}
wiki_consume = {
    "Ягодный сок": [['Очки здоровья', 4], ['Ловкость', 1]]
}
class Player:
    def __init__(self):
        self.name = ''
        self.stats = []
        self.level, self.exp, self.free_points = -1, 0, 0
        self.equipment = {
            'Броня':'Диадема лесной дриады',
            'Аксессуар': '-',
            'Орудие': '-',
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
    def get_exp_bar(self):
        self.exp_bar = (self.exp // (self.exp_next//10))*'▓' + (10 - len((self.exp // (self.exp_next//10))*'▓'))*'░'
    def get_level(self):
        self.level += 1
        self.free_points += self.level * 5
        match self.level:
            case 0: self.exp_next = 10
            case 1: self.exp_next = 50
            case 2: self.exp_next = 100
            case 3: self.exp_next = 500
            case 4: self.exp_next = 1000
        self.get_exp_bar()
        # self.exp_bar = (self.experience // (self.exp_next//10))*'▓' + (10-len((self.experience // (self.exp_next//10))*'▓'))*'░'
    def show_all(self):
        print('\n'
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀      \n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀     Уровень: {self.level}\n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀      \n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀     {self.exp_bar} {self.exp}/{self.exp_next}\n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     \n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Очки здоровья: {self.stats['Очки здоровья']}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Урон: {self.stats['Урон']}\n"
            f"⠀⠀⠀⢸⠀⢰⠉⡆⠀⡇⠀⠀⠀⠀    ・Ловкость: {self.stats['Ловкость']}\n"
            f"⠀⠀⠀⠘⠶⠟⠀⠻⠶⠃⠀⠀⠀⠀    ・Защита: {self.stats['Защита']}\n"
        )
        print(f'▐ Броня: {self.equipment["Броня"]}  '
              f'▐ Орудие: {self.equipment["Орудие"]}  '
              f'▐ Аксессуар: {self.equipment["Аксессуар"]}\n')
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(self.inventory):
            print(i + 1, '-', item)
        print('\n')
    def greet(self):
        print(
            f"⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀  \n"
            f"⠀⠀⠀⣤⠿⠿⠿⠿⠿⣤⠀⠀⠀⠀ \n"
            f"⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀    ・Очки здоровья: {self.stats['Очки здоровья']}\n"
            f"⠸⣤⠀⠀⣿⠀⠀⠀⣿⠀⠀⣤⠇⠀    ・Сила: {self.stats['Сила']}\n"
            f"⠀ ⠈⠷⢦⠀⠀⠀⡶⠾⠁⠀⠀     ・Магия: {self.stats['Магия']}\n"
            f"⠀⠀⠀⣰⠛⠋⠉⠙⠛⣆⠀⠀⠀⠀    ・Ловкость: {self.stats['Ловкость']}\n"
            f"⠀⢠⡟⢰ ⠀⠀⠀ ⡆⢻⡄⠀⠀    ・Защита: {self.stats['Защита']}\n"
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
    def show_inventory(self, inventory):
        print('     ✦ Инвентарь ✦')
        for i, item in enumerate(inventory):
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
            yesno = ''
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
    def consume(self, item):
        yesno = ''
        while yesno not in ['1', '2']:
            yesno = input(f'- ТоЧнО МОжНо {item}? (1 - Да, 2 - Нет)\n')
        if yesno == "1":
            for i in wiki_consume[item]:
                print(f"- ХарАКтеРИстИКА {i[0]} ВоЗРОсЛа нА {i[1]}! :D")
                self.stats[i[0]] += i[1]
            self.inventory.remove(item)
player = Player()
print("- ПРиВЕи! ДоБРо ПОжаЛоВать в МИр! КтО я? НУ... КтО-тО? БЕз ПОНЯтиЯ, КтО Я. ЗаТО ЗнАЮ, ЧТО ты - ЧеЛОвЕкоПоДОбнАя сЛИзЬ!\n")
player.get_stats()
class Creature:
    def __init__(self, kind, health=(3,10), damage = (1,10), speed=(1,10), defense=(1,5), experience=(3,6), stats_base=25, loot = ['']):
        self.level = randint(player.level-1,player.level+1)
        self.level = 0
        self.exp = randint(*experience)
        self.kind = kind
        self.loot = choice(loot) if randint(0,1) == 0 else ''
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
        self.hurt = max(1,(enemy.stats['Урон']-self.defense))
        self.health = max(self.health - self.hurt, 0)

def menu(player):
    def mon_meet(amount = randint(1,3)):
        # g = '- Ой, НаПАдаЮТ!\n' if randint(0,1) == 0 else '- МонСтРЫ, моНсТры!\n'
        # print(g)
        # cur_mon = [choice(list(wiki_monsters.keys())[:-1]) for i in range(amount)]
        # print(cur_mon, amount, '\n')
        for i in cur_mon_code:
            i.show_stats()
        choice_menu()
    def choice_menu():
        player_choice = ''
        while player_choice not in ['1','2','3','4','5']:
            player_choice = input("- ЧтО дЕлАТь БуДЕм? (1 - Инвентарь, 2 - Атака, 3 - Уклонение, 4 - Побег, 5 - Отобразить монстров)\n")
        if player_choice == '1':
            inventory()
        elif player_choice == '2':
            attack()
        elif player_choice == '3':
            f = 0
        elif player_choice == '4':
            print("- БеЖИМ-БЕЖиМ!!\n" if randint(0,1) == 0 else "- БЫстРЫе НогИ ВРаГоВ Не БоЯтСЯ!\n")
            return 0
        elif player_choice == '5':
            mon_meet()
    def inventory():
        talk = "- ВОтаКвОТ" if randint(0,1)==0 else "- НУ ДавАЙ поСМОтРиМ"
        print(talk)
        player.show_all()
        player_inventory_choice = ''
        while player_inventory_choice not in ['1', '2', '3', '4']:
            player_inventory_choice = input("- ЧтО ТеПЕрЬ? (1 - Поглотить, 2 - Надеть, 3 - Ничего, 4 - Рассмотреть)\n")
        if player_inventory_choice == '1':
            print("- ЧТо КуШАеМ? :P\n")
            player.show_inventory(player.inventory)
            eat_item = ''
            while eat_item not in [str(i+1) for i in range(len(player.inventory))]:
                eat_item = input()
            player.consume(player.inventory[int(eat_item)-1])
            pause = input('НаЖми Для ПроДоЛжЕниЯ')
            return inventory()
        elif player_inventory_choice == "2":
            print("- ВОт наШ ГАрдЕроБ!! ЧТо НаДЕнЕм? :^\n")
            usable_inventory = [i for i in player.inventory if i in wiki.keys()]
            player.show_inventory(usable_inventory)
            puton_item = ''
            while puton_item not in [str(i+1) for i in range(len(usable_inventory))]:
                puton_item = input()
            player.equip(usable_inventory[int(puton_item)-1])
            pause = input()
            return inventory()
        elif player_inventory_choice == "4":
            print("- Я ПОбУдУ ТвОЕй СЛаЙМОпЕдиеЙ!! ЧТо тЫ ХоЧЕшь РаСсмОТрЕтЬ? (* v *)\n")
            player.show_inventory(player.inventory)
            examine_item = ''
            while examine_item not in [str(i + 1) for i in range(len(player.inventory))]:
                examine_item = input()
            examine_item = player.inventory[int(examine_item)-1]
            print(wiki.get(examine_item)[0])
            pause = input()
            return inventory()
        else:
            return choice_menu()
    def attack():
        for i, mon in enumerate(cur_mon_code):
            print(i + 1, '-', mon.kind)
        player_attack_choice = ''
        print('')
        while player_attack_choice not in [str(i+1) for i in range(len(cur_mon))]:
            player_attack_choice = input("- КОго БьЁм?\n")
        att_mon = cur_mon_code[int(player_attack_choice)-1]
        att_mon.get_hurt(player)
        print(f"- ВПерЁд!! СУщЕствУ {att_mon.kind} нАнЕСеНо {att_mon.hurt} еДинИЦ УрОНа >:D\n" if att_mon.hurt != 1
              else f'- БЛиИИнб, МОнСТр {att_mon.kind} ПоЧтИ нЕ ПОлуЧиЛ УРонА. ВсЕгО еДИниЧКа :((\n')
        if att_mon.health == 0:
            print("- ХЫхЫ!! ВРаГ ПоВЕрЖен!\n" if randint(0,1)==0 else f"- ХеХЕ! МиНУс {att_mon.kind}!\n")
            player.exp += att_mon.exp
            print(f"- Мы ПОлУЧилИ {att_mon.exp} ОчКоВ ОпЫТА!\n")
            if player.exp >= player.exp_next:
                player.exp -= player.exp_next
                player.get_level()
            else:
                player.get_exp_bar()
            cur_mon_code.pop(int(player_attack_choice)-1)
            if att_mon.loot != '':
                print(f"- ХАбР-ХАбАбр- Да тьФУ! ХаБАР1!! {att_mon.loot}\n" if randint(0,1) == 0
                      else f"- ХИХИ, СчАЧстьЯ прИвАлИло, СмОтрИ, {att_mon.loot} :DD\n")
                player.inventory.append(att_mon.loot)
            if not cur_mon_code:
                print('- МЫ вСЕХ ПобЕДиЛи!! (^ o ^)\n')
                pause = input()
                return 0
        choice_menu()
    if randint(1,30) in range(1,30):
        g = '- Ой, НаПАдаЮТ!\n' if randint(0, 1) == 0 else '- МонСтРЫ, моНсТры!\n'
        print(g)
        cur_mon = [choice(list(wiki_monsters.keys())[:-1]) for i in range(randint(1,3))]
        cur_mon_code = [Creature(i, *wiki_monsters[i]) for i in cur_mon]
        mon_meet()
    else:
        print('- СУнДУК!!!\n' if randint(0,1)==0 else '- СОкРовИща, УРа!\n')
        treasure = choice(list(wiki.keys()))
        print(f'- {treasure}! Всё В ДОм, ВСё в ДОмМ ХыхЫ\n')
        player.inventory.append(treasure)

player.show_all()
# menu(player)
while player.stats['Очки здоровья'] != 0:
    menu(player)
# for i in wiki_monsters.keys():
#     cr = Creature(i, *wiki_monsters[i])
#     cr.show_stats()
