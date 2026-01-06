vocal = 0
vocales = ['a','e','i','o','u']

palabra = input("Escribe tú palabra: ").lower()

for i in palabra:
    if i in vocales:
        vocal+=1
      
print(f"Tú palabra contiene {vocal} vocales.")        
