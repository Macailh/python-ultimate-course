usuarios2 = [["Andres", 43], ["Rodrigo", 445], ["Lopen", 4]]

# nombres = []
# for usuario in usuarios2:
#     nombres.append(usuario[0])
#
#
# print(nombres)

# nombres = [expresion for item in items]
# filtrar y transformar

# map
# nombres = [usuario[0] for usuario in usuarios2]

# filter
# nombres = [usuario[0] for usuario in usuarios2 if usuario[1] > 7]

#nombres = list(map(lambda usuario: usuario[0], usuarios2)) # es lo mismo pero esta forma no se recomienda
menosUsuarios = list(filter(lambda usuario:usuario[1] > 7, usuarios2))
# print(nombres)
print(menosUsuarios)
