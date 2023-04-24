saludo = "Hola global" #No usar varibales globales


def saludar():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)

saludar()
saludaChanchito()
saludar()

print(saludo)