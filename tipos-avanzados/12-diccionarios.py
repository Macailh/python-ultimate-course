punto = {"x": 25, "y": 50}  # la llave debe ser un string pero el valor puede ser cualquier tipo de dato
print(punto)
print(punto["y"])

punto["z"] = 12

print(punto)
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto["x"])
print(punto.get("bayond", 89))

del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])


for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Salvador"},
    {"id": 2, "nombre": "Enrique"},
    {"id": 3, "nombre": "German"},
    {"id": 4, "nombre": "Gonzalo"}
]

for usuario in usuarios:
    print(usuario["nombre"])