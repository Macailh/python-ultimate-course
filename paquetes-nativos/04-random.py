import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)

print(
    random.random(),
    random.randint(1, 13),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=2)
)

chars = string.ascii_letters
digits = string.digits

seleccion = random.choices(chars + digits, k=10)
print(seleccion)

constrasena = "".join(seleccion)
print(constrasena)
