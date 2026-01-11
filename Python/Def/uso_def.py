# entrada
palabra = input("escribe tu palabra: ").lower().strip().replace(" ", "") # reemplaza un caracter por otro

# la funcion devuelve si es o no es un palindromo
def es_palindromo(texto): # parametro

    if texto == texto[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

# llamar a la funcion
es_palindromo(palabra) # argumento
