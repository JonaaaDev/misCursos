# creación del diccionario
mi_diccionario = {
    "nombre": "Jonathan",
    "edad": 19,
    "salario": 1200.00,
    "teléfono": 123456789
}

print(mi_diccionario["teléfono"])

# elimina la clave y valor
del mi_diccionario["teléfono"]

# creacion de una nueva clave y le asignamos un valor
mi_diccionario["permiso_de_conducir"] = False
print(mi_diccionario["nombre"]) 

# muestra claves
print(mi_diccionario.keys()) 

# muestra valores
print(mi_diccionario.values())
