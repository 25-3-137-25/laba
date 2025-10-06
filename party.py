class Human:
    def __init__(self, name, level, strengh, hp, mp, dexterity, iq):
        self.name = name
        self.level = level
        self.strengh = strengh
        self.hp = hp
        self.mp = mp
        self.dexterity = dexterity
        self.iq = iq


    def print_info(self):
        print('Имя: {}. Уровень: {}. Сила: {}. ХП: {}. Мана: {}. Ловкость: {}. Интеллект: {}'.format(self.name, self.level, self.strengh, self.hp, self.mp, self.dexterity, self.iq))

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Получено {damage} урона")

    def attack(self, target, amount):
        target.take_damage(amount)
        print(f"Персонажу {target} нанесено {amount} урона")



class leader(Human):
    pass

class funny(Human):
    pass

class playful(Human):
    pass

class Boss:
    def __init__(self, name, hp, ):