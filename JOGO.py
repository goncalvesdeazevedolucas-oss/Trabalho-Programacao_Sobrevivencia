import random
import time
import math
import msvcrt #StackOverFlow
import unicodedata #Video Youtube
import os #Alisson 

def afk():
    xp_afk= 0
    print("Aperte Qualquer Tecla para Começar a Jornada")
    while True:
        xp_afk += random.randint(5,17)
        bolada_chance = random.randint(0, 150)
        time.sleep(1)
        if bolada_chance == 75:
            bolada= random.randint(300,750)
            xp_afk += bolada
            print(f"XP Acumulado {xp_afk} BOLADA!(+{bolada})!")
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
def normal(palavra):        #https://www.youtube.com/watch?v=ZPqb8k76sK4&t=437s
    nfdk_normalizacao= unicodedata.normalize('NFKD', palavra)
    return ''.join([x for x in nfdk_normalizacao if not unicodedata.combining(x)]).upper()
def limpar():
    time.sleep(0.1)
    os.system("cls")

inventario= list()
xp = 0
vida = random.randint(15,20)
sorte = random.randint(0,50)
dano= 10
level = 1

choose = start()
comeco= modo(choose)
if comeco == "AFK":
    xp += afk()
    comeco = "JORNADA"
    
if comeco == "JORNADA":
    nome = input("Insira o Nome do seu Personagem: ")
    if len(nome) == 0:
        nome = "???"
    while True:
        classe = input("Escolha sua Classe [1- Médico ], [ 2- Sobrevivente], [3- Idiota] :")
        
        if classe == "1" or normal(classe) == "MEDICO":
            classe = "MÉDICO"
            vida += 5
            print("Você recebeu +5 de vida")
            time.sleep(0.5)
            inventario.append("Medkit")
            print("Você recebeu um Medkit")
            jornada()
            break
        
        elif classe == "2" or normal(classe) == "SOBREVIVENTE":
            classe= "SOBREVIVENTE"
            vida += 25
            print(f"Você recebeu +25 de Vida, Vida Total({vida})")
            break
        
        elif classe == "3" or normal(classe) == "IDIOTA":
            confirm=input("""
                  Você tem certeza disso?
                      Sim | Não
                      Escolha:
                  """)
            if normal(confirm) == "SIM" or "S":
                classe = "IDIOTA"
                sorte += -20
                print(f"Perdeu 20 de Sorte, Sorte Atual ({sorte})")
                break
            elif normal(confirm) == "N" or "NAO":
                continue

        elif classe == "2026302743":
            classe= "ADMIM"
            vida = 2000000000
            dano = 2000000000
            sorte = 100
            level = 100
            break
        
        else:
            continue
    
print(nome)
print(classe)
print(inventario)  
chamar_status(xp,vida,sorte,dano,level)



# Médico +5 Vida , 1 medkit
# Sobrevivente +20 Vida
# Idiota -20 Sorte