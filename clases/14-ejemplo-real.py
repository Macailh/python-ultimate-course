class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, do you have to definen a table")

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
