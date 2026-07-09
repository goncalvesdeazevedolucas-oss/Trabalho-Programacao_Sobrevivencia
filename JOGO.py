import random
import time
import math
import msvcrt

def afk():
    xp_afk= 0
    print("Aperte Qualquer Tecla para Começar a Jornada")
    while True:
        xp_afk += random.randint(5,17)
        bolada = random.randint(0, 150)
        time.sleep(1)
        if bolada == 75:
        xp_afk += random.randint(300,750)
        print(f"XP Acumulado", {xp_afk}, "BOLADA!!")
        else:
            print(f"XP Acumulado: {xp_afk}")
        if msvcrt.kbhit():
            msvcrt.getch()
            return xp_afk
            break
def jornada():
    print("Começa a jornada")
    chamar_status(xp,vida,sorte,dano,level)
def chamar_status(xp,vida,sorte,dano,level):
    print(F"""
        XP={xp}
        Vida={vida}
        Sorte={sorte}
        Dano={dano}
        Level={level}
        """)
def start():
    return input("""
      1 - Começar Modo Jornada
      2 - Começar Modo AFK
      
      Escolha:""")
def modo(choose):
    if choose == "2" or choose.upper() == "AFK":
        return "AFK"
    elif choose == "1" or choose.upper() == "JORNADA":
        return "JORNADA"
    else:
        choose = start()
        return modo(choose)
      

xp = 0
vida = random.randint(15,20)
sorte = random.randint(0,100)
dano= 10
level = 1

choose = start()
comeco= modo(choose)
if comeco == "AFK":
    xp += afk()
    jornada()
elif comeco == "JORNADA":
    jornada()



# nome = input("Insira o Nome do seu Personagem: ")
# classe = input("Escolha sua Classe [1- Médico ], [ 2- Sobrevivente], [3- Idiota] :")
#Médico +5 Vida , 1 medkit
#Sobrevivente +20 Vida
#Idiota -20 Sorte