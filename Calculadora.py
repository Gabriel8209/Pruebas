#Introducción 
calculadoraON = True
print("\nBienvenido a esta calculadora de prácticas")
print("Hecha por TCF_Gabo8209")
#Inicio del rograma
while calculadoraON == True:
    print("------------Nueva operación------------")
    print("Pueden ser números enteros e irracionales")
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    op = input("Elige que operación hacer(+, -, * o /): ")
    if op == ("+"):
        print("Elegiste la suma")
        resultado = num1 + num2
        print("El resultado es: ", resultado)
    elif op == ("-"):
        print("Elegiste la resta")
        resultado = num1 - num2
        print("El resultado es: ", resultado)
    elif op == ("*"):
        print("Elegiste la multiplicación")
        resultado = num1 * num2
        print("El resultado es: ", resultado)
    elif op == ("/"):
        if num2 == 0:
            print("¡ERROR! No se puede dividir entre 0")
        else:
            print("Elegiste la división")
            resultado = num1 / num2
            print("El resultado es: ", resultado)
    else:
        print("¡ERROR! Tienes que elegir algun tipo de operación")
    resp = input("¡Terminaste tu operación! ¿Quieres salir de la calculadora? (si/no)").strip().lower()
    if resp == ("si"):
        print("Muchas gracias por usar esta calculadora")
        calculadoraON = False