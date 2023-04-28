import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("No se ha pasado ningún argumento")
        return

    if len(args) != 3:
        print("Se esperan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("Destino ya existe")

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")


cli(sys.argv)
