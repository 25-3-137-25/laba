from party import *
from species import *

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

print("ВЫБЕРИТЕ СВОЕГО МИНЬОНА...")
print("")

a = input().lower()
characters = {"1": "Кевин", "2": "Боб", "3": "Стюарт", "кевин": "Кевин", "боб": "Боб", "стюарт": "Стюарт"}
if a in characters:
    print(f"ВАШ ПЕРСОНАЖ - {characters[a]}")
else:
    print("ПЕРСОНАЖА ПОД ТАКИМ НОМЕРОМ НЕТ.")
print(stuart.hp)
kevin.butt(stuart, kevin.damage, kevin.dexterity)
print(stuart.hp)
