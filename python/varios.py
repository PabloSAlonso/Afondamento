
# Se podría hacer por separado (print y luego input)
nombre = input("Dime tu nombre: ") # Peticion de datos

# input siempre devuelve un String, por lo que hay que convertirlo a entero
edad = int(input("Ahora la edad: "))
temperatura = float(input("¿Qué temperatura e ºC hace ahora?\n"))

print() # deja una línea en blanco

print(nombre + ", Welcome\nto the Python World.\n\n")

# También se importan librerías:
# El import mejor al principio
from datetime import date # del módulo datetime, importa la clase date
año_nacimiento = date.today().year - edad
print('Naciste en el año: ', año_nacimiento) # Se permite comilla simple para cadenas
# tambien permitido importar solo el módulo
# import datetime
# año_nacimiento = datetime.date.today().year - edad
letra = nombre[0] # Se indexa la cadena con []. Ojo, el carácter sigue siendo str.
print("la primera letra de tu nombre es %s" % letra) # Cadena de formato con %
# Cadena interpolada o f-string
print(f"La temperatura en Farenheit es de {32 + temperatura * 9 / 5}ºF")
print("\tNos vemos, \"ser humano\" de ", edad, " años")
# --------------------------------------------------------------------------

# En Python clásico funciona prácticamente igual a Java, pero escrito así:
# "Cadena de formato" % (elemento1, elemento2, …) → Sí, son tuplas
nombre = "Gollum"
edad = 30
peso = 34.341
print("Se llama %s, tiene %d años y pesa %.1fKg.\n" % (nombre, edad, peso))
print("%-10s%10s" % ("Personaje", "Peso (Kg)"))
print("%-10s%10.2f" % (nombre, peso))
print("%-10s%10.2f" % ("Gandalf", 78.2))
print("\nLa edad de %s en los tres sistemas de numeración:" % nombre)
print("Decimal: %d, Octal: %o, Hexadecimal: %04x" % (edad, edad, edad))

# Desde Python 3.6 en adelante se recomienda el uso de f-strings o cadenas iterpoladas
# ¿Sabes deducir cómo funcionan?
nombre = "Gollum"
edad = 30
peso = 34.341
print(f"Se llama {nombre}, tiene {edad} años y pesa {peso:.1f}Kg.\n")
print(f"{'Personaje':<10}{'Peso (Kg)':>10}") # Los > y < justifica el texto en direccion a la flecha (no interpretar como mayor o menor que...)
print(f"{nombre:<10}{peso:>10.2f}")
print(f"{'Gandalf':<10}{78.2:>10.2f}")
print(f"\nLa edad de {nombre} en los tres sistemas de numeración:")
print(f"Decimal: {edad}, Octal: {edad:o}, Hexadecimal: {edad:04x}")

# --------------------------------------------------------------------------- 

# Importamos módulo math
import math
a = int(input("Dame un nº: "))
b = int(input("Dame un otro: "))
print("División entera (cociente) :", a // b) # Diferencia // de /
print("Resto de la división", a % b)
print("División real:%.2f" % (a / b))
print("La potencia de a elevado a b es", a**b) # Existe la potencia con **
print("Area de circunferencia de radio ", a, " es: ", math.pi * (a**2))
print(f"Raiz de {a}: {math.sqrt(a):.3f}")

# ---------------------------------------------------------------------------

# Funciones
import math
# Sin parámetro ni return
def nombre_funcion():
    print("Solo muestro en pantalla")
def separador():
    print("\n-------------------\n")
# Parámetros y valor devuelto
def area_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    area_lateral = 2 * math.pi * radio * altura
    area_total = 2 * area_base + area_lateral
    return area_total
# Devolver varios valores
def calcular_todas_areas_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    area_lateral = 2 * math.pi * radio * altura
    area_total = 2 * area_base + area_lateral
    return area_total, area_lateral, area_base
# Opcionalmente se pueden indicar tipos de parámetros y valor devuelto,
# pero no se exige el cumplimiento. Solo es informativo.
def suma(a:int, b:int)-> int:
    return a+b

nombre_funcion()
separador()
print(f"Area: {area_cilindro(3,4):.2f}")
separador()
total, lateral, base = calcular_todas_areas_cilindro(3, 7)
print(f"Área total: {total:.2f}")
print(f"Área lateral: {lateral:.2f}")
print(f"Área de una base: {base:.2f}")
separador()
print(suma("33","w")) # En teoría deberían ser int, pero el tipado no impone.

# --------------------------------------------------------------------------------

# Excepciones
import math as m # Util si el nombre del módulo es largo
try:
    numero = int(input("Ingresa un número positivo: "))
    if numero < 0:
        raise ArithmeticError("No se pueden calcular raices negativas")
    inverso = 1 / numero
    raiz = m.sqrt(numero)
    print(f"Resultado del inverso: {inverso}")
    print(f"Resultado de la raíz: {raiz}")
except ValueError:
    print("Error: Debes ingresar un número")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except ArithmeticError as e:
    print(f"Error: {e}")

# --------------------------------------------------------------------------------

# Cadenas

texto = "Hola Mundo Python"
len(texto) # 17 - Longitud
"Python" in texto # True - Verifica subcadena
texto.startswith("Hola") # True - Comienza con
texto.endswith("Python") # True - Termina con
texto.find("Mundo") # 5 - Posición (o -1 si no existe)
texto.index("Mundo") # 5 - Posición (error si no existe)
texto.count("o") # 2 - Cuenta ocurrencias
texto.upper() # "HOLA MUNDO PYTHON" - Mayúsculas
texto.lower() # "hola mundo python" - Minúsculas
texto.strip() # Elimina espacios extremos
texto.replace("Mundo", "World") # "Hola World Python"
texto.split() # ["Hola", "Mundo", "Python"] - Por espacios
texto.split("o") # ["H", "la Mund", " Pyth", "n"] - Por "o"
"123".isdigit() # True - Solo dígitos
"abc".isalpha() # True - Solo letras
" ".isspace() # True - Solo espacios

#Está por lo de Gollum aun ok