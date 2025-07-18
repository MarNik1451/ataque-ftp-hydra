import subprocess

objetivo = "scanme.nmap.org"
print(f"[*] Iniciando escaneo rápido con Nmap en: {objetivo}")

# Comando de escaneo rápido
comando = ["nmap", "-F", objetivo]

try:
    resultado = subprocess.run(comando, capture_output=True, text=True, timeout=60)
    salida = resultado.stdout

    print("\n[✓] Resultado del escaneo:\n")
    print(salida)

    # Guardar resultado en archivo
    with open("resultado_nmap.log", "w") as f:
        f.write(salida)

    print("\n[✓] Resultado guardado en: resultado_nmap.log")

except subprocess.TimeoutExpired:
    print("[!] El escaneo tardó demasiado y fue cancelado.")
except KeyboardInterrupt:
    print("\n[!] Escaneo interrumpido por el usuario.")
except Exception as e:
    print(f"[!] Error inesperado: {e}")
