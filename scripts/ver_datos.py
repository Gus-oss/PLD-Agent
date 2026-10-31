from pathlib import Path

# Calculo la ruta desde la ubicación del script, para que funcione sin importar
# desde qué carpeta lo ejecute
RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "data" / "HI-Small_Trans.csv"

# Leo solo las primeras 3 líneas, sin cargar el archivo completo en memoria
with ARCHIVO.open(encoding="utf-8") as f:
    for _ in range(3):
        print(f.readline().rstrip())