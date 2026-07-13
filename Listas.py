#Introducción
ListaJuegos = [ ]
ListaRequisitos = [ ]
ListaObras = [ ]
ListaGeneral = [ ]

def VerLis(a):
    bucle = True
    while bucle:
        if not a:
            print("No hay nada que mostrar")
            return(None)
        elif a:
            print("Hay elementos encontrados")
            return(a)
        else:
            print("¡ERRORE! Tienes que elegir un número entre los que se encuentran disponibles.")
            print("Regresando al menú de listas")

def Add(a, b):
    a = input("¿A qué lista quieres agregar?\n" \
    "Lista de juegos\n" \
    "Lista de que haceres\n" \
    "Lista de proyectos pendientes\n" \
    "Lista general")
    b = input("¿Qué cosa quieres agregar?//" )
#Muestras de listas
Listas = True
while Listas == True:
    print("Elige qué hacer")
    print("1. Ver alguna lista")
    print("2. Agregar algo a las listas")
    print("3. Eliminar aldo de las lsitas")
    print("4. Terminar programa")
    Resp = input("¿Qué eliges?// ")

    if Resp == "1":
        op1 = True
        while op1 == True:
    #Escoger que listas ver
            print("Estas son todas las listas que hay: ")
            print("1. Lista de juegos")
            print("2. Lista de qué haceres")
            print("3. Lista de proyectos pendientes")
            print("4. Lista de cualquier cosa")
            print("Deja en blanco si quieres regresar")
            
            vista = True
            while vista:
                resp = input("¿Qué lista quieres ver?// ")
                if resp == "1":
                    VerLis(ListaJuegos)
                elif resp == "2":
                    VerLis(ListaRequisitos)
                elif resp == "3":
                    VerLis(ListaObras)
                elif resp == "4":
                    VerLis(ListaGeneral)
                elif resp == "":
                    print("Regresando...")
                    vista = False
