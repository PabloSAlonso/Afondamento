def pide_entero_positivo():
    try:
        numero = int (input("Escribe un numero entero positivo - "))
        while(numero < 0):
            numero = int (input("Escribe un numero entero positivo - "))
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
    with open("datos_guardados","r") as archivo_libros:
        for
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
        titulo_eliminar = input("Que libro quieres eliminar (titulo)")
        for libro in libros:
            if libro[0] == titulo_eliminar:
                libros.remove(libro)
    elif(opcion == 4):
        print("Saliendo del programa...")
    else:
        print("Introduce una opcion del menu\n")





