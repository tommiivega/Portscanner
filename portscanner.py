import socket

ip = input("Ingrese la direccion IP a escanear: ")

for puerto in range(1, 65535):
    contador = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.)
    resultado = sock.connect_ex((ip, puerto))
    if resultado == 0:
        print(f"Puerto {puerto} está abierto.")
        contador += 1
        sock.close()
if contador == 0:
    print("No se encontraron puertos abiertos.")