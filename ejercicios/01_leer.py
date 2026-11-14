from pathlib import Path

archivo = Path(__file__).resolve().parents[1] / "datos" / "accesos.log"
with archivo.open(encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
