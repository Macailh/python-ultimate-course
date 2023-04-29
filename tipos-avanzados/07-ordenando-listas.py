numeros = [1, 2, 3, 34, 4, 5, 67]
#numeros.sort(reverse=True) # ordena la lista original

numeros2 = sorted(numeros, reverse=True) # devuelve una nueva lista en lugar de alterar la lista original
print(numeros)
print(numeros2)

usuarios = [[23, "Andres"], [5, "Rodrigo"], [6, "Lopen"]]
usuarios.sort()
print(usuarios)

usuarios2 = [["Andres", 43], ["Rodrigo", 445], ["Lopen", 4]]

def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios2)