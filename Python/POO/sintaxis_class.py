class Identidad:
    
    def __init__(self, nombre, apellido, edad):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_identidad(self):
        
        print("Te llamas %s y te apellidas %s y tienes %i años\n" % (self.nombre, self.apellido, self.edad))
        
identidad_1 = Identidad("Jonathan", "Gimenez", 19) 
identidad_1.mostrar_identidad()          

identidad_2 = Identidad("Angeline", "Alvarado", 19) 
identidad_2.mostrar_identidad() 
