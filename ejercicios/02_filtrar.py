from pathlib import Path
archivo = Path(__file__).resolve().parents[1] / "datos" / "accesos.log"
# TODO: mostrar solo las líneas que contienen FAILED.
with archivo.open(encoding="utf-8") as f:
    for linea in f:
        if "FAILED" in linea:
            print(linea.strip())
