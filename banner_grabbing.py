import subprocess

# IP objetivo
ip_objetivo = "scanme.nmap.org"

print(f"[*] Iniciando enumeración de servicios y banners en: {ip_objetivo}...")

# Comando Nmap con detección de versión y script de banner
comando = ["nmap", "-sV", "-p-", "--script=banner", ip_objetivo]
resultado = subprocess.run(comando, capture_output=True, text=True)

# Guardar salida en archivo .log
nombre_archivo = "resultado_banner_grabbing.log"
with open(nombre_archivo, "w") as archivo:
    archivo.write(resultado.stdout)

print(f"[✓] Resultados guardados en: {nombre_archivo}")
