from pathlib import Path
from time import ctime

archivo = Path("archivo.txt")

print(archivo.exists())
print(archivo.stat().st_atime)

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
