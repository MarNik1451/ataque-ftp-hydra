import subprocess

# Archivos de entrada y salida
usuarios = "usuarios.txt"
passwords = "passwords.txt"
host = "ftp://test.rebex.net"
log_file = "resultado_hydra.log"

# Comando Hydra
comando = [
    "hydra",
    "-L", usuarios,
    "-P", passwords,
    host,
    "-o", log_file
]

print("[*] Ejecutando ataque de fuerza bruta con Hydra...\n")
resultado = subprocess.run(comando, capture_output=True, text=True)

# Imprimir salida de Hydra
print("[*] Salida en consola:\n")
print(resultado.stdout)

# Analizar si encontró credenciales válidas
if "login:" in resultado.stdout:
    print("\n[✓] ¡Credenciales encontradas!\n")
    for linea in resultado.stdout.splitlines():
        if "login:" in linea:
            print("➜", linea)
else:
    print("\n[✗] No se encontraron credenciales válidas.")

# Guardar log completo
with open(log_file, "w") as archivo:
    archivo.write(resultado.stdout)
