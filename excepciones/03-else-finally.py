try:
    n1 = int(input("Ingresa un numero: "))
    print(n1)
except Exception as e:
    print("Ha ocurrido un error ):")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")
