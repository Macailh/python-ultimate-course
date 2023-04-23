class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nomber(self, nombre):
        self.__nombre = nombre

    def hablar(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Cuatemuc", 1)


perro1 = Perro.factory()
perro1.hablar()
perro1.set_nomber("lopex")
print(perro1._Perro__nombre)
