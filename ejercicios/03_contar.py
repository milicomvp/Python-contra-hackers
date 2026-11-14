from pathlib import Path
archivo = Path(__file__).resolve().parents[1] / "datos" / "accesos.log"
# TODO: contar cuántos intentos FAILED aparecen.
contador = 0
with archivo.open(encoding="utf-8") as f:
    for linea in f:
        if "FAILED" in linea:
            contador += 1

print(f"Total de intentos FAILED: {contador}")