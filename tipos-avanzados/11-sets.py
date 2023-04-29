# set significa grupo o conjunto
# no tiene datos duplicados
primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)
segundo = [3, 4, 5, 5, 5]
segundo = set(segundo)

print(primer | segundo) # operador union
print(primer & segundo) # operador interseccion
print(primer - segundo) # calcula la diferencia con respecto al primer set, es decir los elementos que estan en el primero que no estan en el segundo
print(segundo - primer)
print(primer ^ segundo) # diferencia simetrica, devuelve los elementos que no estan el otro conjunto de ambos lados

if 5 in segundo:
    print("si tiene el 5")