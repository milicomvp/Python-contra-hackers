
from pathlib import Path
from collections import Counter

archivo = Path(__file__).resolve().parents[1] / "datos" / "accesos.log"

# TODO: contar FAILED por IP y mostrar el ranking.

contador = Counter()

with archivo.open(encoding="utf-8") as f:
    for linea in f:
        if "FAILED" in linea:
            datos = linea.split()
            for dato in datos:
                if dato.startswith("ip="):
                    ip = dato.split("=", 1)[1]
                    contador[ip] += 1
                    break
                # funciona solo en el IPV4
                elif dato.count(".") == 3 and all(
                    parte.isdigit() and 0 <= int(parte) <= 255
                    for parte in dato.split(".")
                ):
                    contador[dato] += 1
                    break

print("RANKING DE INTENTOS FALLIDOS POR IP")
print("----------------------------------")

for ip, cantidad in contador.most_common():
    print(f"IP: {ip} - Intentos fallidos: {cantidad}")
# Sumar todos los intentos fallidos
total_fallidos = sum(contador.values())

print("----------------------------------")
print(f"TOTAL DE INTENTOS FALLIDOS: {total_fallidos}")