class Ave:
    def __init__(self):
        self.volador = "Es volador"

    def vuela(self):
        print("Vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nadador = "Es nadador"

    def vuela(self):
        super().vuela()
        print("Vuela pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)
