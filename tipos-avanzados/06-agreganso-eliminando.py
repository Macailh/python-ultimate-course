mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz", "Pulga"]

mascotas.insert(1, "Melvin")
mascotas.append("chanchito triste") # añadir elementos al final

mascotas.remove("Pulga") # solo elimina la primera ocurrencia
mascotas.pop(1)

del mascotas[0]
mascotas.clear()

print(mascotas)
