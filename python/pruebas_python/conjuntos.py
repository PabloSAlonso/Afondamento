# SETS (Conjuntos)
# Colección de elementos ÚNICOS y NO ORDENADOS
# Se definen entre llaves {} o con set()
# Creación de sets
frutas = {"manzana", "naranja", "plátano", "uva", "manzana"} # manzana duplicada
citricos = set(["limón", "naranja", "lima", "naranja", "pomelo"]) # Desde lista con duplicados
vacio = set()
print(f"Frutas: {frutas}") # ¡manzana aparece solo una vez!
print(f"Cítricos: {citricos}") # Los duplicados se eliminan
print(f"Set vacío: {vacio}")
print(f"Tipo: {type(frutas)}")
# Añadir elementos
frutas.add("fresa")
frutas.add("mango")
print(f"Tras añadir: {frutas}")
# Eliminar elementos
frutas.remove("naranja") # Error si no existe
frutas.discard("plátano") # No da error si no existe
print(f"Tras eliminar: {frutas}")
# NO se puede modificar elementos específicos (no tienen índice)
# frutas[0] = "sandía" # ¡ERROR! Los sets no tienen orden
# Pertenencia
print(f"¿Está 'manzana' en el set? {'manzana' in frutas}")
print(f"¿Está 'naranja' en el set? {'naranja' in frutas}")
# Admite operaciones clásicas de conjutos:
# Union (|), Intersección (&), Diferencia(-), subconjuntos...
# permite iteración aunque no tenga índices
print("Frutas en el set:")
for fruta in frutas:
    print(f" - {fruta}")
# De lista a set (elimina duplicados)
lista_con_duplicados = ["manzana", "naranja", "manzana", "uva", "naranja", "uva"] 
set_sin_duplicados = set(lista_con_duplicados)
print(f"Lista con duplicados: {lista_con_duplicados}")
print(f"Set sin duplicados: {set_sin_duplicados}")
# De set a lista (pierde la propiedad de unicidad)
lista_nueva = list(set_sin_duplicados)
print(f"De vuelta a lista: {lista_nueva}")