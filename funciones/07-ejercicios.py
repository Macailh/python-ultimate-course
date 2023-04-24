def es_palindrome(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


print(es_palindrome("Anita lava la tina"))
print(es_palindrome("Hola mundo"))
