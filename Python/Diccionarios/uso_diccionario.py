mi_diccionario = {
    "nombre": "Jonathan",
    "edad": 19,
    "salario": 1200.00,
    "teléfono": 123456789
}

print(mi_diccionario["teléfono"])
del mi_diccionario["teléfono"]
mi_diccionario["permiso_de_conducir"] = False
print(mi_diccionario["nombre"]) 

print(mi_diccionario.keys()) 
print(mi_diccionario.values())
