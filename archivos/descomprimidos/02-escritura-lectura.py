from pathlib import Path

archivo = Path("archivo.txt")
texto = archivo.read_text("utf-8").split("\n")

texto.insert(0, "Hola mundo")
archivo.write_text("\n".join(texto), "utf-8")

print(texto)
