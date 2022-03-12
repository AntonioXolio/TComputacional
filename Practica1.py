import os
import string
import re

#def listAlphabet():
#    return list(string.ascii_lowercase)
#def listAlphabetM():
#    return list(string.ascii_uppercase)

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system("clear")
    print("Selecciona una opción")
    print("\t1 - Ingresa el alfabeto")
    print("\t2 - Leer cadenas w1 y w2")
    print("\t3 - Generación aleatoria de los lenguaje L1 y L2")
    print("\t4 - Generación del lenguaje LD")
    print("\t5 - Potencia del alfabeto")
    print("\t6 - Cadenas que contengan las 5 vocales en orden")
    print("\t7 - Cadenas de digitos que tengan por lo menos un digito repetido")
    print("\t8 - ------")
    print("\t9 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >>")
    if opcionMenu == "1":
        #print(listAlphabet())
        #print(listAlphabetM())
        #Pide numero de letras, se convierte en entero para poder usarse en el ciclo
        numero = int(input("Cuantas letras desea agregar: "))
        #Arreglo que almacena letras
        letras = []
        for i in range(numero):
            r = input("Introduce una letra: ")
            letras.append(r)
            print(letras)
        input("\npulsa Enter para continuar")
    elif opcionMenu == "2":
        def validar_palabra(palabra):
            patron = '^[{letras}]+$'

            return bool(re.search(patron,palabra))

        print("Cadenas w1 y w2")
        #print(f"alfabeto={letras}")
        print("Ingresa la cadena w1")
        w1 = input()
        print("Ingresa la cadena w2")
        w2 = input()
        print("La cadena w1 es valida:")
        print(validar_palabra(w1))
        print("La cadena w2 es valida:")
        print(validar_palabra(w2))
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("Generación de los lenguajes L1 y L2")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        print("Generación de lenguaje LD apartir de los lenguajes L1 y L2")
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "5":
        print("Generación de lenguaje LD apartir de los lenguajes L1 y L2")
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "6":
        print("Cadenas que contengan las 5 vocales en orden")
        def validar_palabra(palabra1):
            #patron = '[qwrtypsdfghjklzxcvbnm]+a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u[qwrtypsdfghjklzxcvbnm]+|a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u|a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u|[qwrtypsdfghjklzxcvbnm]+a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u[qwrtypsdfghjklzxcvbnm]+|^aeiou'
            patron1 = '[a-z]+a[a-z]+e[a-z]+i[a-z]+o[a-z]+u[a-z]+|a[a-z]+e[a-z]+i[a-z]+o[a-z]+u|a[a-z]+e[a-z]+i[a-z]+o[a-z]+u|[a-z]+a[a-z]+e[a-z]+i[a-z]+o[a-z]+u[a-z]+|^aeiou'

            return bool(re.search(patron1,palabra1))
            
        print("Ingrese una cadena")
        c1 = input()
        print("La cadena es valida:")
        print(validar_palabra(c1))
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "7":
        print("Todas las cadenas de dígitos que tengan por lo menos un dígito repetido")

        def validar_palabra(palabra):
            patron = '[r"\d+"]'
            
            return bool(re.search(patron,palabra))

        print("Ingrese una cadena")
        c2 = input()
        print("La cadena es valida:")
        print(validar_palabra(c2))
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "8":
        print("Generación de lenguaje LD apartir de los lenguajes L1 y L2")
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "9":
        break
    else:
        print("")
        input(
            "No has pulsado ninguna opción correcta...\npulsa una tecla para continuar"
        )
