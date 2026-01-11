# entrada al input
nombre = input("escribe tu nombre: ").lower().strip()

# la funcion devuelve si es o no es un palindromo
def es_palindromo(texto): # parametro

    # la condicion que compara
    if texto == texto[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

# llamar a la funcion
es_palindromo(nombre) # argumento
