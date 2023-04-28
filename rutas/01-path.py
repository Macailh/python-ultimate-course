from pathlib import Path

# Path("/usr/bin")
# Path.home()

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.suffix,
    path.stem,
    path.parent,
    path.absolute(),
)

p = path.with_name("chanchito.py")

print(p)

p = path.with_suffix(".txt")

print(p)
