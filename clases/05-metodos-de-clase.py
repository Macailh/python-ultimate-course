class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def hablar(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Cuatemuc", 1)


Perro.hablar()
perrito = Perro.factory()
print(perrito.nombre, perrito.edad)