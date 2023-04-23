print("""
Bienvenido a la calculadora
Para salir escribe salir
Las operaciones son suma, resta, multi y div

""")
num1 = input("Ingresa número: ")
resultado = int(num1)


while True:
    operacion = input("Ingresa la operación: ")

    if operacion.strip().lower() == "salir":
        print("Saliendo...")
        break

    num2 = input("Ingresa el siguiente número: ")

    if operacion.strip().lower() == "suma":
        resultado += int(num2)
        print("El resultado es ", resultado)
        continue
    elif operacion.strip().lower() == "resta":
        resultado -= int(num2)
        print("El resultado es ", resultado)
        continue
    elif operacion.strip().lower() == "multi":
        resultado *= int(num2)
        print("El resultado es ", resultado)
        continue
    elif operacion.strip().lower() == "div":
        resultado /= int(num2)
        print("El resultado es ", resultado)
        continue
    else:
        print("Ingrese una operación valida")
        continue
