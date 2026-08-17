import unicodedata, time, random
def normal(palavra):        #https://www.youtube.com/watch?v=ZPqb8k76sK4&t=437s
    nfdk_normalizacao= unicodedata.normalize('NFKD', palavra)
    return ''.join([x for x in nfdk_normalizacao if not unicodedata.combining(x)]).upper()
# # def noacent(palavra):        #https://www.youtube.com/watch?v=ZPqb8k76sK4&t=437s
# #     nfdk_normalizacao= unicodedata.normalize('NFKD', palavra)
# #     return ''.join([x for x in nfdk_normalizacao if not unicodedata.combining(x)]).upper()

# # print(noacent("médiCO23"))
# import time
# import os

# print("LASJHBHUBYGHNCUHTJ$RSVBH DN")
# time.sleep(2)
# os.system("cls")

# def modo():
#     return "m"

# inventario = list()
# item_e = modo()
# if item_e == None:
#     pass
# else:
#     inventario.append(item_e)
inventario= ["batata","pao"]
xp = 0
vida = random.randint(15,25)
sorte = random.randint(0,50)
dano= 10
level = 1
fugiu = 0
batalhas = 0
nome= 'teste'
classe= 'teste'
# chamar_status(xp,vida,sorte,dano,level,nome,inventario,classe)
# # print(inventario.index("batata")+1)
# vida_animal= 100
# vida_animal += -(dano*2)
# print(vida_animal)
# print(random.uniform(1,10))
# a=2
# a -= 1
# print(a)
# for i in inventario:
#     idx= inventario.index(i)
#     print(inventario.index(i)+1,  "".join(inventario[idx]))
# # 
# print("Inventário:")
# for i in inventario:
#     idx = inventario.index(i)
#     print(inventario.index(i)+1, "".join(inventario[idx]))

# while True:
#     print("Qual Item Deseja Usar")
#     print("Digite CANCELAR para Cancelar")
#     choose = input('Escolha:')
#     if normal(choose) == "CANCELAR":
#         break
#     if choose.isdigit():
#         idx = int(choose)
#         if idx < 1 or idx > len(inventario):
#             print("Opção inválida")
#             continue
#         choose = inventario[idx - 1]
#     if normal(choose) == "PAO":
#         item_usado = "pao"
#         break
#     elif normal(choose) == "BATATA":
#         item_usado = "batata"
#         break
#     else:
#         continue

# print(item_usado)
# for idx, i in enumerate(inventario, start=1):
#     print(idx, i)
print(normal("ç"))