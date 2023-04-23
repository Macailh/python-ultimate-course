class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Chancito(Perro):
    def programar(self):
        print("comiendo")


perro = Perro()
perro.comer()

chanchito = Chancito()
chanchito.comer()
