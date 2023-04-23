from io import open


# texto = "Hola mundo, esto es una prueba de escritura en un archivo"

# archivo = open("hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# archivo = open("hola-mundo.txt", "r")
# text = archivo.read()
# archivo.close()

# print(text)

# archivo = open("hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()

# print(texto)

# with open("hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())

#     archivo.seek(0)

#     for linea in archivo:
#         print(linea)

archivo = open("hola-mundo.txt", "a+")
archivo.write("Chao mundo")
