def hola(nombre, apellido="Doe"):
    print(f"Hola {nombre} {apellido}")
    print(f"Bienvenido {nombre} {apellido}")


hola("Salvador", "German")
hola("Enrique")

hola(apellido="German", nombre="Salvador")
