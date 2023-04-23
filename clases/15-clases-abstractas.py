from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    def save(self):
        print(f"Saving {self.tabla} en BBDD")

    @classmethod
    def serch_for_id(self, _id):
        print(f"Searching for id: {_id} en la tabla {self.tabla}")


class User(Model):
    tabla = "user"


user = User()

user.save()
user.serch_for_id(13)
