import json
from pathlib import Path


# escribit json
# productos = [
#     {"id": 1, "nombre": "producto 1", "precio": 100},
#     {"id": 2, "nombre": "producto 2", "precio": 200},
#     {"id": 3, "nombre": "producto 3", "precio": 300},
#     {"id": 4, "nombre": "producto 4", "precio": 400},
# ]

# data = json.dumps(productos)
# Path("productos.json").write_text(data)
# print(data)

data = Path("productos.json").read_bytes()
productos = json.loads(data)
print(productos)

productos[0]["name"] = "Chanchito feliz"
Path("productos.json").write_text(json.dumps(productos))
