#Introducción
import time
tienda = True
import random
cliente = False
dineroTOT = 1000
inventario = []
pedidos = []
pociones = ["Poción de resistencia", "Poción de fuerza", "Poción de velocidad", "Poción de invisibilidad", "Poción de curación"]
name = []

#Bienvenida
print("Bienvenido a la tienda de pocionesRPG")
print("Hecho por TCF_Gabo8209")
print("Contexto: Eres el dueño de una tienda de pociones, donde vendran una serie de clientes qu estarán pidiendo pociones o ingredientes")
print("Tu objetivo es vender la mayor cantidad de pociones posibles, para eso debes tener un buen stock de ingredientes y pociones")

#Inicio del programa
while tienda == True:
   opción = input(f">----------Bienvenido a tu tienda----------< \n¿Qué quieres hacer? \nTienes un presupuesto de  {dineroTOT}  de oro. \n1.Abrir tu inventario \n2.Abrir lista de pedidos \n3.Preparar una poción \n4.Comprar ingredientes \n5.Atender un nuevo clienteb \n7. Terminar programa \nQué harás?// ").strip().lower()
   if opción == ("1"):
        inventarioON = True
        while inventarioON == True:
            print(">..................Inventario..................<")
            ingCont = []
            for ingrediente in inventario:
                if ingrediente not in ingCont:
                    cantidad = inventario.count(ingrediente)
                    print(f"{ingrediente} {cantidad}")
                    ingCont.append(ingrediente)
            print("_______________________________________")
            respt = True
            while respt == True:
                resp = input("¿Terminaste de revisar tu inventario?(y/n)// ").strip().lower()
                if resp == ("y"):
                    print("<<<Regresando al menú principal>>>")
                    respt = False
                    inventarioON = False
                elif resp == ("n"):
                    print("Bien")
                    for i in range (10, 0, -1):
                        segundos = i
                        print("Quedan", segundos, " segundos restantes")
                        time.sleep (1)
                else:
                    print("¡ERROR! Tienes que poner (y) o (n) para realizar una operación")
                    time.sleep (1)
                    print("Elige bien una opción")
                    time.sleep (1)
   elif opción == ("2"):
       pocionesON = True
       while pocionesON ==True:
            print(">..................Lista de pedidos..................<")
            if len(pedidos) == 0:
                print("No tienes pedidos en cola. Puedes descansar de momento")
                pocionesON = False
            else:
                print(f"Tienes {len(pedidos)} pedidos en cola. Atiéndelos rápido")
                for i in range(len(pedidos)):
                    print(f"Tienes a {name[i]} que pidió una {pedidos[i]}")
                time.sleep (3)
                respt = input("¿Terminaste de revisar a esperantes?(y/n)// ").strip().lower()
                if respt == "y":
                    print("¡Muy bien! regresando al menú principal")
                    for i in range (3, 0, -1):
                        segundos = i
                        print("!", segundos, " segundos restantes!")
                        time.sleep (1)
                    pocionesON = False
   elif opción == ("3"):
       prepararON = True
       while prepararON == True:
           print(">..................Estante de pociones..................<\nBienvenido a tu estante de pociones \n¿Qué haremos ahorita?")
           respt1 = input("¿Qué poción harás ahora? \n1.Cura")

