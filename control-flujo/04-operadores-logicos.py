# and, or, not

gas = True
encendido = True
edad = 19

if gas ^ encendido:
    print("Puedes avanzar")

mensaje = "Puedes avanzar" if gas and encendido else "No puedes avanzar"
print(mensaje)

if gas and encendido and edad > 17:
    print("Puedes avanzar")
