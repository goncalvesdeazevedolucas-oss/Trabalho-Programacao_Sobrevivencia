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
            limpar()
            return xp_afk
            break
def chamar_status(xp,vida,sorte,dano,level,nome,inventario,classe):
    print(f"Nome: {nome}")
    print(f"Inventario: {"".join(inventario)}")
    print(f"Classe: {classe}")
    print(f"""
        Xp={xp}
        Vida={vida}
        Sorte={sorte}
        Dano={dano}
        Level={level}
        """)
def normal(palavra):        #https://www.youtube.com/watch?v=ZPqb8k76sK4&t=437s
    nfdk_normalizacao= unicodedata.normalize('NFKD', palavra)
    return ''.join([x for x in nfdk_normalizacao if not unicodedata.combining(x)]).upper()
def limpar():
    time.sleep(0.1)
    os.system("cls")
def basico():
    xp_e = 0
    choose=input("""
      1 - Começar Modo Jornada
      2 - Começar Modo AFK
      
      Escolha:""")
    limpar()
    if choose == "2" or normal(choose) == "AFK":
        comeco = "AFK"
    elif choose == "1" or normal(choose) == "JORNADA":
        comeco = "JORNADA"
    else:
        return basico()
    
    if comeco == "AFK":
        xp_e = 0
        xp_e += afk()
        comeco = "JORNADA"
    
    if comeco == "JORNADA":
        nome = input("Insira o Nome do seu Personagem: ")
        if len(nome) == 0:
            nome = "???"
        while True:
            classe = input("Seu personagem vai ser um(a)? [1- Médico(a) ], [2- Sobrevivente], [3- Idiota] :")
            
            if classe == "1" or normal(classe) == "MEDICO":
                classe = "MÉDICO"
                vida_e = 5
                item_e= "Medkit"
                sorte_e= 0
                dano_e = 0
                level_e =0
                break
            
            elif classe == "2" or normal(classe) == "SOBREVIVENTE":
                classe= "SOBREVIVENTE"
                vida_e = 25
                item_e= None
                sorte_e= 0
                dano_e = 5
                level_e =0
                break
            
            elif classe == "3" or normal(classe) == "IDIOTA":
                classe = "IDIOTA"
                sorte_e = 20
                vida_e = -5
                item_e= None
                dano_e = 2
                level_e =0
                break
                

            elif classe == "2026302743":
                classe= "?  ?  ?"
                vida_e = 2000000000
                dano_e = 2000000000
                sorte_e = 100
                level_e = 100
                item_e= None
                break
            
            else:
                continue
        limpar()
        return xp_e, vida_e, sorte_e, item_e, dano_e, level_e, nome, classe        
        

inventario= list()
xp = 0
vida = random.randint(15,25)
sorte = random.randint(0,50)
dano= 10
level = 1
fugiu = 0
batalhas = 0

xp_e, vida_e, sorte_e, item_e, dano_e, level_e, nome, classe = basico()

xp, vida, sorte, dano, level = xp_e + xp, vida_e + vida, sorte_e + sorte, dano_e + dano, level_e + level

if item_e == None:
    pass
else:
    inventario.append(item_e)

    

chamar_status(xp,vida,sorte,dano,level,nome,inventario,classe)



# Médico +5 Vida , 1 medkit
# Sobrevivente +20 Vida
# Idiota -20 Sorte