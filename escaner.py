import socket
from concurrent.futures import ThreadPoolExecutor


def escanear_puertos(ip, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        rs = s.connect_ex((ip, puerto))
        if rs == 0:
            print(f"[+] Puerto {puerto} abierto!")


ip_user = input("Ip > ")
puertos = range(1, 1045)
print("Escaneando...")

try:
    with ThreadPoolExecutor(max_workers=100) as exe:
        for p in puertos:
            exe.submit(escanear_puertos, ip_user, p)
except KeyboardInterrupt:
    print("\n[x]Acción Interrumpida por el Usuario")
