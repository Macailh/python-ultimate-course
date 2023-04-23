class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Perro:
    def pasear(self):
        print("paseando al perro")


class Chancito(Animal, Perro):
    def programar(self):
        print("comiendo")


chanchito = Chancito()
chanchito.pasear()

perro = Perro()
perro.pasear()
