class Human:
    def __init__(self, Name, Level, Strengh, hp, MP, Dexterity, IQ):
        self.Name = Name
        self.Level = Level
        self.Strengh = Strengh
        self.hp = hp
        self.MP = MP
        self.Dexterity = Dexterity
        self.IQ = IQ


    def print_info(self):
        print('Имя: {}. Уровень: {}. Сила: {}. ХП: {}. Мана: {}. Ловкость: {}. Интеллект: {}'.format(self.Name, self.Level, self.Strengh, self.hp, self.MP, self.Dexterity, self.IQ))

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Получено {damage} урона")


    def damage(self, target):
        target.take_damage




class leader(Human):
    pass

class funny(Human):
    pass

class playful(Human):
    pass


kevin = leader("Кевин, лидер нашей отважной группки миньонов.", 12, 100, 150, 0, 100, 25)
bob = funny("Боб, глупый, милый, симпатичный миньончик.", 15, 30, 200, 300, 50, 200)
stuart = playful("Стюарт, игривый интригант в мире миньонов.", 6, 55, 100, 0, 150, 50)



# print("Введите имя персонажа")
# imya = input()
# print("Введите его уровень")
# yroven = int(input())
# print("Введите его силу")
# sila= int(input())
# print("Введите значение его здоровья")
# hhp = int(input())
# print("Введите значение его маны")
# mana = int(input())
# print("Введите его ловкость")
# lovkost = int(input())
# print("Введите его интеллект")
# iqqq = int(input())
# character_1 = Human(imya, yroven, sila, hhp, mana, lovkost, iqqq)
# character_1.print_info()