class Human:
    def __init__(self, name, dexterity, level, strengh, hp, iq, damage):
        self.name = name
        self.level = level
        self.strengh = strengh
        self.hp = hp
        self.dexterity = dexterity
        self.iq = iq
        self.damage = damage

    @property
    def zhiv(self):
        if self.hp > 0:
            return "Персонаж всё ещё жив."
        else:
            return "Персонаж мёртв."

    def print_info(self):
        print('Имя: {}. Уровень: {}. Сила: {}. ХП: {}. Ловкость: {}. Интеллект: {}.'.format(self.name, self.level, self.strengh, self.hp, self.dexterity, self.iq))
    def take_damage(self, damage):
        self.hp -= damage



class leader(Human):
    def __init__(self, name, dexterity, level = 19, strengh = 100, hp = 150, iq = 140, damage = 50):
        super().__init__(name, dexterity, level, strengh, hp, iq, damage)
    def hand(self, target, damage, strengh, iq):
        target.take_damage((damage + (strengh*0.2) + (iq/50)))
        print(f"Персонаж {self.name} ударил кулаком персонажа {target.name}, нанеся {(damage + (strengh*0.2))} урона")
    def butt(self, target, damage, dexterity):
        target.take_damage((damage + (dexterity*0.2)))
        print(f"Персонаж {self.name}, толкнул своей пятой точкой персонажа {target.name}, нанеся {(damage + (dexterity*0.2))} урона")

class funny(Human):
    def __init__(self, name, level, strengh, hp, dexterity, iq, damage):
        super().__init__(name, level, strengh, hp, dexterity, iq, damage)

class playful(Human):
    pass