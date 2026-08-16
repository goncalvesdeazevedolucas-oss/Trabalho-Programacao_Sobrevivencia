import random
import time
import msvcrt #StackOverFlow
import unicodedata #Video Youtube
import os #Alisson 


def afk():
    xp_afk= 0
    print("Aperte Qualquer Tecla para Parar e Começar a Jornada")
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
def chamar_status(xp,vida,sorte,dano,level,nome,inventario,classe):
    print(f"Nome: {nome}")
    for idx, i in enumerate(inventario, start=1):
        print(idx, i)
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
def opcoes(sorte,dano,vida, inventario):
        print("""
            O que você irá fazer ??
    1-Buscar recursos | 2-Ver Perfil | 3-Esperar por um Animal
               4- Usar Item | 5- Parar o Jogo
            """)
        choose= input("Escolha: ")
        if choose == '1':
            return buscar_recursos(sorte)
        elif choose == '2':
            chamar_status(xp,vida,sorte,dano,level,nome,inventario,classe)
            print("Aperte Qualquer tecla para continuar")
            while not msvcrt.kbhit():
                time.sleep(0.1)
            msvcrt.getch()
            limpar()
            return opcoes(sorte,dano,vida,inventario)
        elif choose == '3':
            return animal(sorte, dano, vida)
        elif choose == '4':
                return 5, 0, None, 0
                
        elif choose == '5':
            limpar()
            return -1, 0, None, 0 #BREAK 
        else:
            limpar()
            print("Opção Inválida (Apenas Números São Válidos)")
            return 0 , 0, None, 0
def animal(sorte,dano,vida):
    while True:
        chance= random.randint(1,30)
        animal = random_animal()
        if chance in range(1,5):
            print(f"Você avistou um{animal}")
            print(".", end="", flush=True)
            time.sleep(1.5)

            print(".", end="", flush=True)
            time.sleep(1.5)

            print(".", flush=True)
            time.sleep(1.5)
            print(f"VOCÊ FOI VISTO CORRA OU BATALHE PELA SUA VIDA")
            while True:
                choose= input("""
                            O que você faz????
                            1 - Correr
                            2 - Batalhar
                            """)
                if normal(choose) == "1" or normal(choose) == "CORRER":
                    print("Você perde 2 de vida por cansaço")
                    return 0, -2, None,0
                elif normal(choose) =="2" or normal(choose) == "BATALHAR":
                    vida_e, item_e, xp_e = batalha(animal,dano,vida)
                    return 0, vida_e, item_e, xp_e
                else:
                    limpar()
                    continue
        elif chance in range(6,20):
            print("Nenhum animal apareceu")
            time.sleep(1.5)
            return 0,0,None,0
        elif chance in range(21,28):
            print(f"Um{animal} Apareceu mas você o Espantou")
            time.sleep(1.5)
            return 0,0,None, 50
        else:
            print(f"Nada Aparece e você é picado por Aranha")
            if sorte <= 20:
                return 1, -8, None, 10#-8 de vida
            elif sorte <= 40:
                return 2, -4, None, 10 #-4 de vida
            elif sorte >= 80:
                return 3, 0, None,10 # -0 de vida
            elif sorte >=41:
                return 4, -1, None,10 # -1 de vida
def random_animal():
    animal= random.randint(1,4)
    if animal == 1:
        return "a Ave"
    elif animal == 2:
        return " Javali"
    elif animal == 3:
        return " Cobra"
    elif animal == 4:
        return " Coelho"
def batalha(animal, dano, vida):
    vida_perdida= 0
    if animal == 'a Ave':
        animal = 'Ave'
        pron='a'
        item_e= "Carne"
        vida_animal= 20
        xp_e= 200
    elif animal == ' Javali':
        animal = 'Javali'
        pron='o'
        item_e= "Presa"
        vida_animal= 40
        xp_e= 700
    elif animal == ' Cobra':
        animal = 'Cobra'
        pron= 'a'
        item_e= "Carne"
        vida_animal= 30
        xp_e= 400
    elif animal == ' Coelho':
        animal = 'Coelho'
        pron='o'
        xp_e= 150
        vida_animal= 15
        ie= random.randint(1,7)
        if ie == 6:
            item_e= "Pé de Coelho"
        else:
            item_e= "Carne"
    while True:
        limpar()
        if vida_perdida + vida <= 0:
            return vida_perdida, None, xp_e
        if vida_animal <= 0.9999999999:
            return vida_perdida, item_e, xp_e
        print(f"Vida perdida: {vida_perdida}")
        print(f"Vida do Animal: {int(vida_animal)}")
        choose=input(""" O que você quer fazer??? 
                        1 - Atacar  2 - Fugir         
                    """)
        if choose == "2" or normal(choose) == "FUGIR":
            return vida_perdida, None,xp_e
        elif choose == "1" or normal(choose) == "ATACAR":
            chance= random.uniform(0,11)
            if chance <= 1:
                print("Ataque pegou + Contra-ataque de raspão")
                vida_animal += -dano
                vida_perdida+=-1
            elif chance <= 2:
                print("O Ataque pega de Raspão")
                vida_animal += -dano/2
            elif chance <= 3:
                print("Dano Crítico")
                vida_animal += -(dano*2)
            elif chance <= 4:
                print("Errou o Ataque")
                vida_animal += 0
            elif chance <= 5:
                print(f"Você erra o ataque e {pron} {animal} tem tempo de se recuperar")
                vida_animal+= dano/4
            elif chance <=6:
                print("Acerto em Cheio")
                vida_animal+= -(dano*1.5)
            elif chance <=7:
                print("Acerto")
                vida_animal += -dano
            elif chance <= 8:
                print("Errou e Recebeu um Contra Ataque")
                vida_perdida += -10
            elif chance <= 9:
                print("Acerto Fraco")
                vida_animal+= -(dano/3)
            elif chance <= 9.25:
                print("Dano Fatal")
                vida_animal += -(dano*5)
            elif chance <= 9.30:
                print("Contra-Ataque Fatal")
                vida_perdida += -9999
            else:
                print("Errou o Ataque")
        else:
            continue
def usar_item(inventario):
    print("Inventário:")
    for i in inventario:
        idx= inventario.index(i)
        print(inventario.index(i)+1,  "".join(inventario[idx]))
    item_usado= None
    while True:
        print("Qual Item Deseja Usar")
        print("Digite CANCELAR para Cancelar")
        choose = input('Escolha:')
        if normal(choose) == "CANCELAR":
            return 0, 0, 0, None
        if choose.isdigit():
            idx = int(choose)
            if idx < 1 or idx > len(inventario):
                print("Opção inválida")
                continue
            choose = inventario[idx - 1]
        if normal(choose) == "CARNE":
            item_usado ="Carne"
            vida_e= 20
            dano_e= 0
            sorte_e= 0
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "PRESA":
            item_usado="Presa"
            vida_e= 0
            dano_e = 5
            sorte_e= 0
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "PE DE COELHO":
            item_usado="Pé de Coelho"
            vida_e= 0
            dano_e = 0
            sorte_e= 20
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "MEDKIT":
            item_usado="Medkit"
            vida_e = 0 
            dano_e = 0
            sorte_e= 0
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "AGUA":
            item_usado = "Água"
            vida_e = 10
            dano_e = 0
            sorte_e = 0
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "ERVAS MEDICINAIS":
            item_usado = "Ervas Medicinais"
            vida_e = 15
            dano_e = 0
            sorte_e = 0
            return vida_e, dano_e, sorte_e, item_usado
        elif normal(choose) == "FACA":
            item_usado = "Faca"
            vida_e = 0
            dano_e = 3
            sorte_e = 0
            return vida_e, dano_e, sorte_e, item_usado
        else:
            print("Opção inválida")
            continue
def random_recurso():
    item = random.randint(1,6)
    if item == 1:
        return "Carne"
    elif item == 2:
        return "Presa"
    elif item == 3:
        return "Pé de Coelho"
    elif item == 4:
        return "Água"
    elif item == 5:
        return "Ervas Medicinais"
    else:
        return "Faca"
def buscar_recursos(sorte):
    bonus_sorte = sorte // 10
    chance = random.randint(1,20) - bonus_sorte
    if chance < 1:
        chance = 1

    if chance in range(1,6):
        item = random_recurso()
        print(f"Você encontrou: {item}")
        return 0, 0, item, 30 + bonus_sorte
    elif chance in range(6,9):
        print("Você encontrou um pouco de comida no caminho")
        return 0, 0, "Carne", 20 + bonus_sorte
    elif chance in range(9,12):
        print("Você achou uma fonte de água")
        return 0, 0, "Água", 15 + bonus_sorte
    elif chance in range(12,15):
        print("Você achou algumas ervas medicinais")
        return 0, 0, "Ervas Medicinais", 20 + bonus_sorte
    elif chance in range(15,17):
        print("Você achou uma faca no chão")
        return 0, 0, "Faca", 40 + bonus_sorte
    elif chance in range(17,19):
        print("Você se machucou procurando recursos")
        return 0, -3, None, 10
    elif chance == 19:
        print("Você procurou mas não achou nada")
        return 0, 0, None, 5
    else:
        print("Você caiu numa armadilha e se feriu")
        return 0, -10, None, 0
    
inventario= list()
xp = 0
vida = random.randint(15,25)
sorte = random.randint(0,50)
dano= 10
level = 1

xp_e, vida_e, sorte_e, item_e, dano_e, level_e, nome, classe = basico()

xp, vida, sorte, dano, level = xp_e + xp, vida_e + vida, sorte_e + sorte, dano_e + dano, level_e + level
xp_e, vida_e, sorte_e, dano_e, level_e= 0, 0, 0, 0, 0
if item_e == None:
    pass
else:
    inventario.append(item_e)

item_e= None

while True:
    xp, vida, sorte, dano= xp_e + xp, vida_e + vida, sorte_e + sorte, dano_e + dano
    while xp >= 1000:
        level += 1
        dano += 1
        vida += 3
        xp -= 1000
    if item_e == None:
        pass
    else:
        inventario.append(item_e)
        
    item_e = None
    xp_e, vida_e, sorte_e, dano_e, level_e= 0,0,0,0,0
    if vida <= 0:
        limpar()
        print("Morreu")
        break
    
    escolhido, vida_e, item_e, xp_e= opcoes(sorte, dano, vida, inventario)
    
    if escolhido == -1:
        limpar()
        print("Jogo Encerrado")
        break
    elif escolhido == 1:
        print("Você perdeu -8 de Vida")
    elif escolhido == 2:
        print("Você perdeu -4 de Vida")
    elif escolhido == 3:
        print("Você não perdeu Vida, Que Sorte")
    elif escolhido == 4:
        print("Você perdeu -1 de Vida")
    elif escolhido == 0:
        continue
    elif escolhido == 5:
        vida_e,dano_e,sorte_e,item_usado=usar_item(inventario)
        if item_usado == None:
            pass
        elif item_usado == "Medkit":
            inventario.remove(item_usado)
            vida = 50
        else:
            inventario.remove(item_usado)

