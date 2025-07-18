import subprocess

# Paso 1: IP objetivo (ajústalo según tu red, ej. 192.168.1.0/24)
ip_objetivo = "172.17.0.0/16"


print(f"[*] Escaneando red local: {ip_objetivo}...")

# Paso 2: Ejecutar escaneo Nmap para detectar hosts activos y sus puertos abiertos
comando = ["nmap", "-sS", "-p-", "-T4", ip_objetivo]
resultado = subprocess.run(comando, capture_output=True, text=True)

# Paso 3: Guardar resultados en archivo .log
nombre_archivo = "resultado_red_local.log"
with open(nombre_archivo, "w") as archivo:
    archivo.write(resultado.stdout)

print(f"[✓] Resultados guardados en: {nombre_archivo}")
