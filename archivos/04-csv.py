import csv

# with open("archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["Nombre", "Apellido", "Edad"])
#     writer.writerow(["Salvador", "German", 12])
#     writer.writerow(["Adrain", "Groman", 20])


with open("archivo.csv") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)
