# Lista: colección de elementos ordenada.
# Es mutable.
# se definen entre corchetes
pokemons =["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Chrizard", "Italiani", "CojoCosta"]
print(type(pokemons))
print("\nOriginal:",pokemons)
pokemons.append("Eevee") # añade al final
pokemons.insert(2,"Ratatta")
print("\nTras añadir:",pokemons)
pokemons.remove("Bulbasaur") # elimina elemento segun el valor
del pokemons[5] # elimina elemento segun el indice
print("\nTras eliminar:",pokemons)
f=pokemons.pop() # extrae y elimina el último.
print("\nExtrae y elimina:",f)
print("\nQueda:",pokemons)
pokemons[0]="Ditto" # modificar
print("\nY tras modificar:",pokemons)
print("\n")

# Tuplas
# Similar a la lista pero no se puede modificar. INMUTABLES!!!
colores=("magenta" , "cian", "amarillo")
print(type(colores))
print(colores)
print(colores[0])
# colores[0] ="amarillo" #error
print("\nOperaciones permitidas en tuplas:")
print("Longitud:", len(colores))
print("¿Está 'cian' en la tupla?", "cian" in colores)

# Iteración sobre listas y tuplas
# como un foreach clásico
print("\nPokemons")
for pokemon in pokemons:
    print(f"{pokemon:>10}")
print("\n Colores")
for color in colores:
    print(f"{color:>10}")
# Es posible hacer una lista o tupla de cualquier tipo, incluso de otra lista o tupla.
# En general cualquier estructura puede contener otra estructura.

# Array bidimensional completitooo
import random
def crear_array_bidimensional(filas, columnas):
# Así se suelen documentar las funciones, con """ que es comentario de bloque o string preformateado

    """
    Crea un array bidimensional (lista de listas) con números aleatorios entre 10 y 20.
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
    Returns:
        list: Array bidimensional con números aleatorios
    """
    array = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero_aleatorio = random.randint(10, 20)
            fila.append(numero_aleatorio)
        array.append(fila)
    return array
def mostrar_array_formateado(array):
    """
    Muestra un array bidimensional bien formateado con números de filas y columnas.
    Args:
        array (list): Array bidimensional a mostrar
    """
    filas = len(array)
    if filas == 0:
        print("Array vacío")
        return
    columnas = len(array[0])
    for i in range(filas):
        for j in range(columnas):
# Mediante end="" cambiamos el caracter
# final del print que por defecto es \n
            print(f" {array[i][j]:3} ", end="")
        print()
m=crear_array_bidimensional(3,4)
mostrar_array_formateado(m)