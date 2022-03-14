import os
import string
import re
import random

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
    print("\t3 - Generación aleatoria de los lenguaje L1, L2 y LD")
    print("\t4 - Potencia del alfabeto")
    print("\t5 - Cadenas que contengan las 5 vocales en orden")
    print("\t6 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >>")
    if opcionMenu == "1":

        letras = []
        #Pide numero de letras, se convierte en entero para poder usarse en el ciclo
        numero = int(input("Cuantos simbolos desea agregar: "))
        for i in range(numero):
            r = input("Introduce un simbolo: ")
            letras.append(r)
        simbolo = ''.join(letras)
        print(simbolo)
        input("\npulsa Enter para continuar")
    elif opcionMenu == "2":
        
        print("Cadenas w1 y w2")
        print("Ingresa la cadena w1")
        w1 = input()
        print("Ingresa la cadena w2")
        w2 = input()
        if w1 in simbolo:
            print("La cadena w1 es valida")
        else:
            print("La cadena w1 no es valida")

        if w2 in simbolo:
            print("La cadena w1 es valida")
        else:
            print("La cadena w1 no es valida")
        
        s1=w1[0]
        s2=w1[1]
        s3=w1[1]
        s4=w1[2]

        su=s1+s2
        su2=s3+s4

        su0=w1.startswith(su)
        print("la cadena es un prefijo", su0)
        suf=w1.endswith(su2)
        print("la cadena es un sufijo", suf)

        if w1 in w2:
            print("w1 es una subcadena")
        else:
            print("w1 no es una subcadena")
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("Generación de los lenguajes L1 y L2")
        print("Ingresa el número de elementos o palabras generar para el lenguaje L1")
        number_of_strings = int(input())

        print("Ingresa la longitud de la generar para el lenguaje L1")
        length_of_string = int(input())

        print("Ingresa el número de elementos o palabras generar para el lenguaje L2")
        number_of_strings1 = int(input())

        print("Ingresa la longitud de la generar para el lenguaje L2")
        length_of_string1 = int(input())

        print("L1:")
        for x in range(number_of_strings):
            l1 = print('{'+''.join(random.choice(letras) for _ in range(length_of_string))+'}')
            
        print("L2:")
        for x in range(number_of_strings1):
            l2 = print('{'+''.join(random.choice(letras) for _ in range(length_of_string1))+'}')
        
        print("Generación de lenguaje LD apartir de los lenguajes L1 y L2")
        print(l1 in l2)
        input("\npulsa enter para continuar")
    elif opcionMenu == "4":
        print("Potencia del alfabeto")

        longitud = len(letras)
        def encontrar_potencia(secuencia):
            respuesta = True
            base = 2
            resultado = 2
            grado = 2

            while respuesta:
                if str(resultado) in secuencia:
                    grado += 1
                    resultado = pow(base,grado)
                else:
                    respuesta = False

                return grado-1

        print(encontrar_potencia('longitud'))
        input("\npulsa enter para continuar")
    elif opcionMenu == "5":
        print("Cadenas que contengan las 5 vocales en orden")
        def validar_palabra(palabra1):
            #patron = '[qwrtypsdfghjklzxcvbnm]+a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u[qwrtypsdfghjklzxcvbnm]+|a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u|a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u|[qwrtypsdfghjklzxcvbnm]+a[qwrtypsdfghjklzxcvbnm]+e[qwrtypsdfghjklzxcvbnm]+i[qwrtypsdfghjklzxcvbnm]+o[qwrtypsdfghjklzxcvbnm]+u[qwrtypsdfghjklzxcvbnm]+|^aeiou'
            patron1 = '[a-z]+a[a-z]+e[a-z]+i[a-z]+o[a-z]+u[a-z]+|a[a-z]+e[a-z]+i[a-z]+o[a-z]+u|a[a-z]+e[a-z]+i[a-z]+o[a-z]+u|[a-z]+a[a-z]+e[a-z]+i[a-z]+o[a-z]+u[a-z]+|^aeiou'

            return bool(re.search(patron1,palabra1))
            
        print("Ingrese una cadena")
        c1 = input()
        print("La cadena es valida:")
        print(validar_palabra(c1))
        if validar_palabra(c1) == True:
            print("La palabra es correcta")
        else:
            print("La palabra es incorrecta")
        input("\npulsa enter para continuar")
    elif opcionMenu == "6":
        break
    else:
        print("")
        input(
            "No has pulsado ninguna opción correcta...\npulsa enter para continuar"
        )
