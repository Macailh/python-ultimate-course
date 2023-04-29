from collections import deque

fila = deque([1, 2, 3])
fila.append(4)
fila.append(5)
print(fila)
lista = [1, 2, 3, 4]
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
print(fila)

if not fila:
    print("La fila esta vacia")