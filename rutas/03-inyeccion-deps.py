from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "bases de datos",
    "api": "api",
    "graphql": "graphql",
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except AttributeError:
        print("el paquete no tiene init")


list(map(load, paths))
