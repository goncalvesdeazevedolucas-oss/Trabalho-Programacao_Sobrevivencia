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
def chamar_status(xp,vida,sorte,dano,level):
    print(xp)
    print(vida)
    print(sorte)
    print(dano)
    print(level)

start=input("""
      1 - Começar Modo Jornada
      2 - Começar Modo AFK
      
      Escolha:
      """)
if start == "2" or start.upper() == "AFK":
    xp = 0
    xp += afk()

print(xp)
# nome = input("Insira o Nome do seu Personagem: ")
# classe = input("Escolha sua Classe [1- Médico ], [ 2- Sobrevivente], [3- Idiota] :")
#Médico +5 Vida , 1 medkit
#Sobrevivente +20 Vida
#Idiota -20 Sorte 
