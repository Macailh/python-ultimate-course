from datetime import datetime

fecha = datetime(2019, 1, 1)
fecha3 = datetime(2019, 1, 1, 12, 30, 45)

ahora = datetime.now()

fechaStr = fecha.strptime("2019-01-01", "%Y-%m-%d")

print(fechaStr)

print(fecha)
print(fecha3)
print(ahora)
