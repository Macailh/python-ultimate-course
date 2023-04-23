class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"{self.nombre} a dicho: Guau!")


mi_perro = Perro("Pelusa", 34)
mi_perro2 = Perro("And", 4)

print(mi_perro.patas)

mi_perro.patas = 5

print(mi_perro.patas)
print(mi_perro2.patas)
