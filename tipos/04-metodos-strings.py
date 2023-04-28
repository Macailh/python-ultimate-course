animal = " chanchito Feliz "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal[0].upper())

# Primera letra de cada palabra
print(animal.title())

# Eliminar espacios en blanco a la izquierda y derecha
print(animal.strip())
print(animal.strip().capitalize())
print(animal.lstrip())
print(animal.rstrip())

# Buscar
print(animal.find("che"))
print(animal.replace("Fe", "E"))
print("nCh" in animal)
print("nCh" not in animal)
