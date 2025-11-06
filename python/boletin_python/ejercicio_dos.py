import string

def contar_palabras(texto):
    texto_formateado = texto.lower()
    for signo in string.punctuation:
        texto_formateado = texto_formateado.replace(signo, "")
    palabras = texto_formateado.split()
    frecuencia_cada_palabra = {}
    for palabra in palabras:
        if(palabra in frecuencia_cada_palabra):
            frecuencia_cada_palabra[palabra]+=1
        else:
            frecuencia_cada_palabra[palabra]=1
    return frecuencia_cada_palabra

def estadidisticasDeTexto(texto):
    diccionario = contar_palabras(texto)
    numero_palabras = sum(diccionario.values())
    longitud_total = 0
    for clave, valor in diccionario.items():
        longitud_total += len(clave)*valor
    longitud_media = longitud_total / numero_palabras
    palabras_mas_larga = list(diccionario.keys())[0]
    frecuencia= list(diccionario.values())[0]
    palabra_mas_frecuente= list(diccionario.keys())[0]
    
    for clave, valor in diccionario.items():
        if len(clave) > len(palabras_mas_larga):
            palabras_mas_larga = clave
        if valor > frecuencia:
            frecuencia = valor
            palabra_mas_frecuente = clave
    
    return (longitud_total, longitud_media, palabras_mas_larga, palabra_mas_frecuente)

def leerDoc():
    try:
        archivo = input("Introduce el nombre del archivo\n")
        with open(archivo, "r") as contenido_a_leer:
            return contenido_a_leer.read()
    except IOError:
        print ("Fallo de archivo")


archivo = leerDoc()
diccionario = contar_palabras(archivo)
print ("Apartado A(Diccionario)", end="\n")
for clave, valor in sorted(diccionario.items()):
    print (f"{clave} : {valor}")

print("Apartado B(Estadísticas)", end="\n")
totalPalabras, longMediaPalabras, palabraLarga, palabraMasFrecuente = estadidisticasDeTexto(archivo)
print(f"Total palabras: {totalPalabras} \nLongitud media de las palabras: {longMediaPalabras:.2f} \nPalabra más larga: {palabraLarga} \nPalabra más frecuente: {palabraMasFrecuente}")

        












# 2. Analizador de texto
# a) Función contar_palabras: Recibe un texto y devuelve un diccionario con cada
# palabra y su frecuencia (ignorando mayúsculas y signos de puntuación). Ejemplo:
# # Texto de entrada:
# texto = "El gato negro y el gato blanco juegan. El gato negro es
# rápido."
# # Diccionario que devolvería la función contar_palabras:
# {
#  'el': 3,
#  'gato': 3,
#  'negro': 2,
#  'y': 1,
#  'blanco': 1,
#  'juegan': 1,
#  'es': 1,
#  'rápido': 1
# }
# b) Función estadisticas_texto: Recibe un texto y devuelve en una tupla:
# • Número total de palabras.
# • Longitud media de las palabras.
# • Palabra más larga.
# • Palabra más frecuente.
# c) Programa principal: Pide el nombre de un archivo de texto al usuario y muestra
# primero el diccionario que devuelve contar_palabras y luego las estadísticas que
# devuelva estadisticas_texto. Presenta todos los datos de forma adecuada y bien
# alineados. 