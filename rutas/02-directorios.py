from pathlib import Path

path = Path("rutas")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("directorio-renombrado")

# for p in path.iterdir():
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos_python = [p for p in path.glob("**/*.py")]

print(archivos)
print(archivos_python)
