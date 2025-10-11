from party import *
from species import *
from boss import *

first_text=  ("ВЫ В МИРЕ МУЛЬТФИЛЬМА ГАДКИЙ Я. НА ЭТОТ РАЗ МИНЬОНЫ СТАЛИ РАБОТАТЬ САМОСТОЯТЕЛЬНО, ВЫБРАВ ПУТЬ БОРЬБЫ СО ЗЛОДЕЯМИ, А НЕ РАБОТЫ С НИМИ.\nС ПОМОЩЬЮ ТРЁХ БРАВЫХ БОЙЦОВ ВЫ ДОЛЖНЫ ОДОЛЕТЬ АДОЛЬФА ГИТЛЕРА (любые совпадения случайны, персонажи вымышленные).\nИГРА ПРОИСХОДИТ ПО ХОДАМ, КАЖДЫЙ ХОД ВЫ ДОЛЖНЫ ВЫБРАТЬ ПЕРСОНАЖА, КОТОРЫМ ХОТИТЕ АТАКОВАТЬ, И ОДНУ ИЗ ДВУХ АТАК ЗА ЭТОГО ПЕРСОНАЖА.\nПОСТАРАЙТЕСЬ УБИТЬ БОССА ЗА КАК МОЖНО МЕНЬШЕЕ КОЛИЧЕСТВО ШАГОВ.\nУДАЧИ!")
print(first_text)
print("")
print("")
print(1)
kevin.print_info()
print("")
print(2)
bob.print_info()
print("")
print(3)
stuart.print_info()
print("")
print("")
print("Учтите, что на каждый удар с вашей стороны приходится по 2 удара со стороны босса.")
print("")
print("")
while hitler.alive():
    print(f"У вашего врага на данный момент {hitler.hp} хп")
    print("")
    print("Выберите миньона для хода")
    print("")
    a = input().lower()
    characters = {"1": "Кевин", "2": "Боб", "3": "Стюарт", "кевин": "Кевин", "боб": "Боб", "стюарт": "Стюарт"}
    if a in characters:
        print(f"Ваш персонаж - {characters[a]}")
        if a == "1" or "кевин":
            if kevin.zhiv():
                print(f"У Кевина сейчас {kevin.hp} хп")
                print("Выберите атаку из двух: 1. Удар кулаком 2. Удар пятой точкой. Напишите номер атаки")
                b = int(input())
                if b == 1:
                    kevin.hand(hitler, kevin.damage, kevin.strengh, kevin.stiffness)
                elif b == 2:
                    kevin.butt(hitler, kevin.damage, kevin.dexterity, kevin.stiffness)
                hitler.attacking(kevin, hitler.damage)
                if kevin.hp <= 0:
                    print("Кевин погиб")
                else:
                    print("У Кевина теперь {kevin.hp} хп")
            else:
                print("Кевин мертв, выберите другого персонажа")
    else:
        print("ПЕРСОНАЖА ПОД ТАКИМ НОМЕРОМ НЕТ.")

print("ура гитлер сдох")