# usuarios2 = [["Andres", 43], ["Rodrigo", 445], ["Lopen", 4]]
#
# def ordena(elemento):
#     return elemento[1]
#
#
# usuarios2.sort(key=ordena)
# print(usuarios2)

usuarios2 = [["Andres", 43], ["Rodrigo", 445], ["Lopen", 4]]

usuarios2.sort(key=lambda el: el[1]) # uso de lambda
print(usuarios2)