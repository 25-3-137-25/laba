from party import *
from species import *
from boss import *

intro = (
    "ВЫ В МИРЕ МУЛЬТФИЛЬМА ГАДКИЙ Я. НА ЭТОТ РАЗ МИНЬОНЫ СТАЛИ РАБОТАТЬ САМОСТОЯТЕЛЬНО, ВЫБРАВ ПУТЬ БОРЬБЫ СО ЗЛОДЕЯМИ, А НЕ РАБОТЫ С НИМИ.\n"
    "С ПОМОЩЬЮ ТРЁХ БРАВЫХ БОЙЦОВ ВЫ ДОЛЖНЫ ОДОЛЕТЬ АДОЛЬФА ГИТЛЕРА (любые совпадения случайны, персонажи вымышленные).\n"
    "ИГРА ПРОИСХОДИТ ПО ХОДАМ, КАЖДЫЙ ХОД ВЫ ДОЛЖНЫ ВЫБРАТЬ ПЕРСОНАЖА, КОТОРЫМ ХОТИТЕ АТАКОВАТЬ, И ОДНУ ИЗ ДВУХ АТАК ЗА ЭТОГО ПЕРСОНАЖА.\n"
    "ПОСТАРАЙТЕСЬ УБИТЬ БОССА ЗА КАК МОЖНО МЕНЬШЕЕ КОЛИЧЕСТВО ШАГОВ.\n"
    "УДАЧИ!"
)
print(intro)
print()

minions = {
    "1": kevin,
    "2": bob,
    "3": stuart,
    "кевин": kevin,
    "боб": bob,
    "стюарт": stuart,
}

for i, minion in enumerate([kevin, bob, stuart], start=1):
    print(i)
    minion.print_info()
    print()



while hitler.alive():
    print(f"У вашего врага на данный момент {hitler.hp} хп\n")
    print("Выберите миньона для хода")

    choice = input().lower().strip()
    if choice not in minions:
        print("ПЕРСОНАЖА ПОД ТАКИМ НОМЕРОМ НЕТ.")
        continue

    minion = minions[choice]

    print(f"Ваш персонаж - {minion.name}")

    if not minion.zhiv():
        print(f"{minion.name} мертв, выберите другого персонажа")
        continue
    if minion.name == "Кевин":
        print(f"У {minion.name} сейчас {minion.hp} хп")
        print("Выберите атаку из двух: 1.1 Удар кулаком 1.2 Удар пятой точкой. Напишите номер атаки")
    elif minion.name == "Боб":
        print(f"У {minion.name} сейчас {minion.hp} хп")
        print("Выберите атаку из двух: 2.1 Крик ПАПАЙЯ 2.2 Вылизывание. Напишите номер атаки")
    elif minion.name == "Стюарт":
        print(f"У {minion.name} сейчас {minion.hp} хп")
        print("Выберите атаку из двух: 3.1 Сделать бобо 3.2 Сделать ауч. Напишите номер атаки")


    attack_choice = input()

    if attack_choice == "1.1":
        minion.hand(hitler, minion.damage, minion.strengh, minion.stiffness)
    elif attack_choice == "1.2":
        minion.butt(hitler, minion.damage, minion.dexterity, minion.stiffness)
    elif attack_choice == "2.1":
        minion.papaya(hitler, minion.damage, minion.idiocy)
    elif attack_choice == "2.2":
        minion.licking(hitler, minion.damage, minion.idiocy, minion.dexterity)
    elif attack_choice == "3.1":
        minion.bobo(hitler, stuart.damage, stuart.playfulness, stuart.strengh)
    elif attack_choice == "3.2":
        minion.augh(hitler, minion.damage, minion.playfulness)
    else:
        print("Неизвестная атака. Ход пропущен.")
        continue

    hitler.attacking(minion, hitler.damage)

    if minion.hp <= 0:
        print(f"{minion.name} погиб")
    else:
        print(f"У {minion.name} теперь {minion.hp} хп")

print("ура гитлер сдох")