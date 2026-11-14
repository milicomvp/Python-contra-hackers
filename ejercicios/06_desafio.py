
from pathlib import Path
from datetime import datetime, timedelta

archivo = Path(__file__).resolve().parents[1] / "datos" / "desafio.log"

# TODO: identificar IP con >=5 FAILED en 5 minutos.

intentos = {}

with archivo.open(encoding="utf-8") as f:
    for linea in f:
        if "FAILED" in linea:
            datos = linea.split()

            # Obtener fecha y hora
            fecha_hora = datetime.strptime(
                datos[0] + " " + datos[1],
                "%Y-%m-%d %H:%M:%S"
            )

            # Obtener dirección IP
            ip = datos[3].replace("ip=", "")

            # Agrupar los intentos por IP
            if ip not in intentos:
                intentos[ip] = []

            intentos[ip].append(fecha_hora)

print("ANÁLISIS DE SEGURIDAD - DESAFÍO FINAL")
print("------------------------------------")

total_sospechosas = 0

for ip, fechas in intentos.items():
    fechas.sort()

    for i in range(len(fechas) - 4):
        inicio = fechas[i]
        fin = fechas[i + 4]

        if fin - inicio <= timedelta(minutes=5):
            total_sospechosas += 1

            print(f"IP sospechosa: {ip}")
            print(f"Total de intentos fallidos: {len(fechas)}")
            print(f"Inicio de ventana: {inicio}")
            print(f"Fin de ventana: {fin}")
            print("------------------------------------")
            break

print(f"TOTAL DE IP SOSPECHOSAS: {total_sospechosas}")
print(f"TOTAL FAILED: {sum(len(fechas) for fechas in intentos.values())}")
