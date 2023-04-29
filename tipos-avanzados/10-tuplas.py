# es una lista pero unmutable, se usa cuando no queremos modificar los elementos que se encuentran dentro de un listado
numeros = (1, 2, 3, 4, 5, 6)
print(numeros)

punto = tuple([1, 2, 3])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, tercero, *otros = numeros
print(primero, segundo, tercero, otros)

for n in numeros:
    print(n)

