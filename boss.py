from party import *

class Boss:
    def __init__(self, name, level, hp, damage):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage

    def take_damage(self, damage):
        self.hp -= damage


class vrag(Boss):
    def __init__(self, name, level, hp, damage = 25):
        super().__init__(name, level, hp, damage)

    def attacking(self, cel, damage):
        if 200 <= self.hp <= 250:
            cel.take_damage((damage*2))
            print(f"Персонаж {cel.name} отхватил по бошке от босса В ПЕРВОЙ ФАЗЕ по имени {self.name} и получил {(damage*2)} урона")
        elif 100 <= self.hp <= 199:
            cel.take_damage((damage * 1.5))
            print(f"Персонаж {cel.name} отхватил по бошке от босса ВО ВТОРОЙ ФАЗЕ по имени {self.name} и получил {(damage * 1.5)} урона")
        elif self.hp < 100:
            cel.take_damage((damage * 1))
            print(f"Персонаж {cel.name} отхватил по бошке от босса В ТРЕТЬЕЙ ФАЗЕ по имени {self.name} и получил {(damage * 1)} урона")

    def alive(self):
        if self.hp > 0:
            return 1
        else:
            return 0