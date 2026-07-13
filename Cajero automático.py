import time
#Introducción
cajeroON = True
dinero = float(1000)
print("Bienvenido a tu cajero automático. Hecho por TCF_Gabo8209")
print("Eres una persona que decide usar un cajero automático")
while cajeroON == True:
    print("Bienvenido, tienes un saldo de", dinero, " colones")
    des = input("¿Qué quieres hacer? Opción 1: Retirar dinero. Opción 2: Depositar dinero. Opción 3: Salir ")
    if des == ("Opción 1"):
        retiro = True
        while retiro == True:
            print("Tienes un saldo de ", dinero, " colones")
            resp = float(input("¿Cuanto dinero quieres sacar?: "))
            total = dinero - resp
            if total < 0:
                print("No tienes saldo suficiente")
                print("Revirtiendo la acción")
            elif total >= 0:
                print("Saldo suficiente")
                for i in range (5, 0, -1):
                    segundos = i
                    print("Espera ", segundos, " segundos")
                    time.sleep (1)
                print("Saca tu dinero")
                config = True
                while config == True:
                    for i in range (3, 0, -1):
                        segundos = i
                        print("Espera ", segundos, " s")
                        time.sleep (1)
                    final = input("¿Listo? (si/no)")
                    if final == ("si"):
                        config = False
                        retiro = False
                    elif final == ("no"):
                        print("Regresando al retiro")
                    else:
                        print("¡ERROR! Respuesta no válida")
     elief              
        

