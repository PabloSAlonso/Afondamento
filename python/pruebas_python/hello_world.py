# Cada sentencia en una linea distinta, hay q identar para tema estructuras, no hace falta ningun tipo de signo al final de nada 
print("Welcome to python world", end="") 
#El end sustituye espacio del final por la sentencia q pongas
print("Adios")

# Primeros pasos en python

entero = 20
print(entero)

real = 12.1
print(real)

texto = "hola" # No hay q declarar tipo (js, php etc, no tipado vaya)
print(texto)

print(type(cadena))
print(type(cadena[0])) # Saber tipos viene bien por ser no tipado el lenguaje

boleano = True
print(boleano)

# Codigo apuntes:

entero = 10
real = 12.1
string = "Hola" # También vale 'Hola', no hay char
booleano = True # Empieza por mayúscula, ojo.!!!

# Con type() conozco el tipo
print(type(entero))
print(type(real))
print(type(string)) 
print(type(booleano))

# Las variables empiezan a existir cuando se usan, el tipo depende del dato introducido
# Cualquier variable puede pasar de un tipo a otro (javascript again) ok

dato = int(real) + 3 # No hace falta explicar

print(dato, type(dato)) # El print separando con coma asi va concatenando la cadena como si cada coma fuese un espacio (se puede concatenar con + como siempre tmb) ok

# Regla de estilo: nombre de los archivos todo minus con _ las palabras separadas ok

# cuando empiece la de las 12:20 vamos a seguir, yo te subo otra vez el enlace y si quieres entra sino no vale