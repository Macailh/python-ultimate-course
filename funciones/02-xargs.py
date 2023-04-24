def suma(*numeros): # se el pasa un iterable
    reultado = 0
    for numero in numeros:
        reultado += numero
    print(reultado)


suma(2, 4)
suma(2, 4, 5)
suma(2, 4, 5, 5, 7)
suma(2, 4, 5, 7, 9, 3)
