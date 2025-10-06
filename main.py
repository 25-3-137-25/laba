from party import *
from species import *

print("ВЫ В МИРЕ МУЛЬТФИЛЬМА ГАДКИЙ Я. НА ВЫБОР ЕСТЬ 3 НАИЛУЧШИХ БОЙЦА-МИНЬОНА:")
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

