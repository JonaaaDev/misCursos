# dos formas de crear listas
lista_nombre = []
lista = list()

# muestra el tipo
print(type(lista_nombre))
print(type(lista))

# agregar elemento
lista_nombre.append("Jonathan")
lista_nombre.append("Angeline")
print(lista_nombre)

# insertar posición exacta
lista_nombre.insert(1,"y")
print(lista_nombre)

# eliminar último elemento
lista_nombre.pop()
print(lista_nombre)

# eliminar
lista_nombre.remove("y")
print(lista_nombre)

# agrega una lista a la lista 
lista_nombre.extend(["Angeline","Francia", "Ecuador", "Paris", "Madrid"])
print(lista_nombre)

# muestra el index 
print(lista_nombre.index("Francia"))

# imprime el valor 
print(lista_nombre[2])

# imprime el valor desde el indice 2 al 5 el 6 es excluyente
print(lista_nombre[2:6])

# borra todo
lista_nombre.clear()
print(lista_nombre)
