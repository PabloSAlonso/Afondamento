import random

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("introduce un número válido.")

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("introduce un número entero válido.")

print("Menú de opciones")
print("1. Divisiones")
print("2. Potencia")
print("3. Rango")
print("4. Listas")
opcion = int(input("Elige una opcion\n"))
if (opcion == 1):
    #codigo opcion 1
    num1 = pedir_float("Introduce el dividendo: ")
    num2 = pedir_float("Introduce el divisor: ")
    if num2 == 0:
        print("No se puede dividir entre 0.")
    else:
        cociente = num1 // num2
        resto = num1 % num2
        division = num1 / num2
        print(f"Cociente:{cociente:.4f}")
        print(f"Resto:{resto:.4f}")
        print(f"División:{division:.4f}")
elif (opcion == 2):
    #codigo opcion 2
    base = pedir_float("Introduce la base:")
    exponente = pedir_int("Introduce el exponente (solo numeros enteros):")
    resultado = base ** exponente
    print(f"{base} elevado a {exponente} = {resultado:.2f}")
elif (opcion == 3):
    #codigo opcion 3
    num1 = pedir_int("Introduce el primer número:")
    num2 = pedir_int("Introduce el segundo número:")
    menor = min(num1, num2)
    mayor = max(num1, num2)
    print(f"El menor es {menor} y el mayor es {mayor}.")
    suma = sum(range(menor, mayor + 1))
    print(f"La suma de todos los números entre {menor} y {mayor} es: {suma}")
elif (opcion == 4):
    #codigo opcion 4
    tamaño = pedir_int("¿De qué tamaño quieres las listas?: ")
    if tamaño <= 0:
        print("El tamaño debe ser un número positivo.")
    else:
        lista1 = [random.randint(1, 100) for _ in range(tamaño)]
        lista2 = [random.randint(1, 100) for _ in range(tamaño)]
        lista_suma = [lista1[i] + lista2[i] for i in range(tamaño)]
        print(f"Lista 1: {lista1}")
        print(f"Lista 2: {lista2}")
        print(f"Suma elemento a elemento: {lista_suma}")
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