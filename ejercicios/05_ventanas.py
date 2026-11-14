
from pathlib import Path
from datetime import datetime, timedelta

# TODO: detectar 5 o más fallos de una IP dentro de 5 minutos.
# Pista: agrupa por IP y ordena sus marcas de tiempo.

archivo = Path(__file__).resolve().parents[1] / "datos" / "accesos.log"

# Diccionario para almacenar los intentos por IP
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

            # Agrupar intentos por IP
            if ip not in intentos:
                intentos[ip] = []

            intentos[ip].append(fecha_hora)

# Analizar intentos por IP
print("DETECCIÓN DE INTENTOS SOSPECHOSOS")
print("--------------------------------")

for ip, fechas in intentos.items():

    fechas.sort()

    for i in range(len(fechas) - 4):
        inicio = fechas[i]
        fin = fechas[i + 4]

        if fin - inicio <= timedelta(minutes=5):
            print(f"IP sospechosa: {ip}")
            print("5 intentos fallidos en 5 minutos")
            print(f"Inicio: {inicio}")
            print(f"Fin: {fin}")
            print("--------------------------------")
            break
