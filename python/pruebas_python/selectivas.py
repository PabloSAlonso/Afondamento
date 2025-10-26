# Estructura if-elif-else
numero = int(input("Dame un nº entero: "))
# IMPORTANTE: la identación marca si dentro o fuera de la estructura.
# Los operadores de relación son como en Java
if numero > 0:
    print("El número es positivo.")
    print("Esto también está dentro del if.")
elif numero == 0:
    print("El número es el cero.")
else:
    print("El número es negativo")
print("Esto ya está fuera de la estructura por la identación.")
respuesta = input("¿Deseas continuar?\n")
# Las cadenas sí se pueden comparar con ==
# Las operaciones lógicas son and, or y not
if respuesta =="si" or respuesta == "Si" or respuesta == "SI": # El and es literal "and"
    print("Pues lo lamento porque por ahora voy a a parar")
print("Fin del ejemplo")

# El switch se realiza con varios if-elif-else (el else será el default)

# Existe la estructura match (similar a switch) desde Python 3.10, pero está poco extendida

# Ternaria
print("Positivo o 0" if numero >= 0 else "Negativo") # Se ve natural pero limita ese acortamiento de la ternaria (parece codigo sin mas ahi metido)

# ------------------------------------------------------------------------------

# Bucle While (no hay Do-while)
cont = 1
acu = 0
while cont < 11:
    acu = acu + cont
    cont = cont + 1 # valido cont+=1 pero ++ no existe
print("Acu = ", acu)

# -------------------------------------------------------------------------------

# Bucle For

# El for es un foreach, siempre recorre una enumeración de elementos
for i in range(10): # range(n) devuelve un tipo range: secuencia de números inmutable.
    print(i)
    print("-----")
for i in range (5,30,2):
    print(i)

# Al ser solo foreach se usa mas que nada para recorrer y mostrar pero no mutar/modificar