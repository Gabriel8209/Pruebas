# Introducción
import random
import time

# Inicio de juego
print("\n\n\nHecho por TCF_Gabo8209 \n\n\n")
rep = input("Bienvenido al juego de randomizer \nUn juego donde deberás elegir un número dentro de una secuencia de los mismos y tu objetivo es acertar el número que dé la computadora \n¿Quieres participar (y/n)// ").strip().lower()

if rep == "y":
    RandomON = True
    while RandomON:
        print(">-----------------------------------Nuevo juego>-----------------------------------<")
        print("Bienvenido otra vez, comenzaremos eligiendo primero tu número y luego la computadora elegirá uno")
        On_Off = input("Tendrás que elegir un número entre el 0 al 5 \nTendrás tres vidas en total \n¿Estás listo para probar tu suerte? \ny/n// ").strip().lower()
        
        if On_Off == "y":
            print("Empezaremos enseguida")
            time.sleep(1)
            
            # La computadora elige una sola vez por juego
            print("El primero en elegir será la computadora, suerte")
            COMPchoice = random.randint(0, 5)
            time.sleep(1)
            
            vidas = 3  # <--- CONTROL DE VIDAS
            gano = False
            
            while vidas > 0 and not gano:
                SELFchoice = input(f"\n[Vidas: {vidas}] Elige el número para probar tu suerte (0-5)// ")
                
                # CORRECCIÓN: .isdigit() con paréntesis
                if SELFchoice.isdigit() and 0 <= int(SELFchoice) <= 5:
                    num_usuario = int(SELFchoice) # Transformamos a entero para poder comparar
                    
                    print("Bien. Elegiste correctamente tu número. Vamos a ver el resultado...")
                    for i in range(3, 0, -1): # Bajado a 3 segundos para que no sea tan pesado esperar 5 en cada intento
                        print(f"¡Quedan {i} segundos restantes! ¡Te deseo mucha suerte!")
                        time.sleep(1)
                    
                    # CORRECCIÓN: Comparación de enteros
                    if COMPchoice == num_usuario:
                        print(f"¡Muchas felicidades! Acertaste. ¡Eres un gran suertudo!")
                        gano = True
                    else:
                        vidas -= 1 # Restamos una vida
                        if vidas > 0:
                            print(f"¡Mala suerte! Fallaste. Pero no te rindas, te quedan {vidas} vidas.")
                            print("Tu rival no cambiará su número.")
                        else:
                            print("\n¡Perdiste todas las oportunidades! Más suerte para la próxima.")
                            print(f"El número que tu rival escogió era {COMPchoice}")
                else:
                    print("¡ERROR! Tienes que introducir un número válido entre 0 y 5.")
            
            # Menú de reinicio único (No importa si ganó o perdió)
            elec = True
            while elec:
                FINAL = input("\n¿Quieres volver a jugar el juego completo?(y/n)// ").strip().lower()
                if FINAL == "n":
                    print("Bien. ¡Muchas gracias por jugar! ¡Espero que vuelvas pronto!")
                    elec = False
                    RandomON = False
                elif FINAL == "y":
                    print("Bien. ¡Regresando al menú principal!")
                    time.sleep(1)
                    elec = False
                else:
                    print("¡ERROR! Tienes que elegir (y) o (n)")