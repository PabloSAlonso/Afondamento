def pide_entero_positivo():
    try:
        numero = int (input("Escribe un numero entero positivo - "))
        while(numero < 0):
            numero = int (input("Ojo, has metido un neg. Debes un numero entero positivo - "))
    except ValueError :
        print ("Escribe un numero - ")
    return numero


def comprueba_isbn(isbn):
    isbn = isbn.strip().replace(" ","").replace("-","")
    if len(isbn) != 10 or not isbn[0:9].isdigit():
        return False
    if (isbn[-1] or isbn.endswith("X")):
        return True
    return False

def pide_libro():
    try:
        titulo = input("Dime el titulo de tu libro - ")
        autor = input("Dime el nombre de su autor - ")
        isbn = input("Isbn del libro? - ")
        while (not comprueba_isbn(isbn)):
            isbn = input("Introduce uno válido (longitud 10 con final en X o Dígito) - ")
        print("Dame el numero de paginas")
        numero_paginas = pide_entero_positivo()
    except ValueError:
        print("Introduce valores válidos")
    return titulo, autor, isbn, numero_paginas

#Comprobaciones

# isbn = "123456789X" 
# isbn2 = "1234567890"
# isbn3 = "1234X6789X"
# isbn4 = "1234567890546"
# isbn5 = "12-23 23451X"

# print ("1º",end="\n")
# print (comprueba_isbn(isbn),end="\n")
# print ("2º",end="\n")
# print (comprueba_isbn(isbn2),end="\n")
# print ("3º",end="\n")
# print (comprueba_isbn(isbn3),end="\n")
# print ("4º",end="\n")
# print (comprueba_isbn(isbn4),end="\n")
# print ("5º",end="\n")
# print (comprueba_isbn(isbn5),end="\n")

# PROGRAMA PRINCIPAL

libros = []

try:
    with open("GuardaDatos.txt","r") as archivo_cargar_datos:
        for linea in archivo_cargar_datos:
            linea = linea.strip()
            datos = linea.split(",")
            if (len(datos) == 4):
                libros.append((datos[0],datos[1],datos[2],int(datos[3])))
except IOError:
    print("Problemas con el archivo")

opcion = 0;
while opcion != 4:
    print("=== MENU DE OPCIONES ===\n")
    print("1.- Añadir libro: ", end="\n")
    print("2.- Mostrar lista: ", end="\n")
    print("3.- Eliminar libros: ", end="\n")
    print("4.- Salir: ", end="\n")
    opcion = pide_entero_positivo()
    if (opcion == 1):
        libros.append(pide_libro())
    elif(opcion == 2):
        print(f"{'Título':<20} {'Autor':<20} {'ISBN':<15} {'Páginas':<7}")
        for libro in libros:
            print(f"{libro[0]:<20} {libro[1]:<20} {libro[2]:<20} {libro[3]:<20}")
    elif(opcion == 3):
        titulo_eliminar = input("Que libro quieres eliminar (titulo):")
        #len(libros) -> donde empieza el bucle for(incluido, por eso se le resta 1)
        # segundo parametro que es -1, es donde acaba el bucle y no esta incluido (si pusieramos 0 no llegaria a leer la primer posicion de la coleccion)
        # i se ira incrementando o decrementando en la cantidad que se le pasa al 3º parametro de range, en este caso vamos restando 1
        for i in range(len(libros) - 1, -1, -1):
            if libros[i][0] == titulo_eliminar:
                libros.remove(libros[i])
    elif(opcion == 4):
        print ("Guardando datos...")
        with open("GuardaDatos.txt","w",True) as archivo_guarda_datos:
            for libro in libros:
                archivo_guarda_datos.write(f"{libro[0]}, {libro[1]}, {libro[2]}, {str(libro[3])}\n")
        print("Datos guardados")
        print("Saliendo del programa...")
    else:
        print("Introduce una opcion del menu\n")





