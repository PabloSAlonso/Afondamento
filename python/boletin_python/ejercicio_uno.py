def pedirNumero(n):
    try:
        n = input("Dame el primero numero")
    except ValueError:
        print("Debes ingresar un numero")

print("Menú de opciones")
print("1. Divisiones")
print("2. Potencia")
print("3. Rango")
print("4. Listas")
print("5. Salir")
while (opcion != 5):
    opcion = input("Elige una opcion")
    if (opcion == 1):
        #codigo opcion 1
        print
    elif (opcion == 2):
        #codigo opcion 2
        print
    elif (opcion == 3):
        #codigo opcion 3
        print
    elif (opcion == 4):
        #codigo opcion 4
        print
    elif (opcion == 5):
        print("Fin del programa")
    else:
        print("Opcion no válida")
print("Fuera del menu, hasta otra")


# 1. Menú de cálculos.
#  Haz un menú con las siguientes opciones.  
# • Divisiones: Pide dos datos y muestra el cociente, el resto y la división
#  con decimales. Usa formateo para limitarlo a 4 decimales. Si el divisor
#  es 0 indica el problema.
#  • Potencia: Pide una base y un exponente, este último será entero.
#  Muestra la potencia resultado usando 2 decimales con cadena
#  interpolada (f-string).
#  • Rango: Pide dos números enteros al usuario. Indica cual es el menor y
#  cual el mayor. Luego calcula y muestra la suma de todos los números
#  entre dichos números (incluyendo ambos números en la suma).
#  • Listas: Pide al usuario un tamaño para la lista. Crea dos listas de
#  números aleatorios (en el rango que tu quieras) del tamaño indicado
#  por el usuario. Finalmente muestra las dos listas y una tercera que
#  incluya la suma elemento a elemento de ambas listas.
#  Realiza funciones si lo consideras necesario para organizar el código y para evitar
#  repetirlo