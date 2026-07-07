import random
import time
import math
import msvcrt

def afk():
    xp_afk= 0
    print("Aperte Qualquer Tecla para Parar")
    while True:
        xp_afk += random.randint( 10, 20)
        time.sleep(1)
        print(f"XP Acumulado: {xp_afk}")
        if msvcrt.kbhit():
            msvcrt.getch()
            return xp_afk
            break

xp= 0
xp += afk()
