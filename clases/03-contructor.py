class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guaa!")


mi_perro = Perro("Pelusa", 23)
mi_perro2 = Perro("dos", 32)
mi_perro2.habla()
print(mi_perro.nombre)
print(mi_perro2.nombre)