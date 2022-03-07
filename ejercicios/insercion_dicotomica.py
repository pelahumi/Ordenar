#Creamos la clase

class Insercion():
    pass #ponemos un pass porque definiremos luego los atributos de la clase

    #Definimos el constructor con los atributos de la clase

    def __init__(self, array):
        self.array = array
        self.minimo = min(self.array)
        self.new_array = []
        self.index = 0
    
    #Definimos el método de la clase que nos ordenará el array

    def ordenar(self):
        if  min(self.array) <= self.minimo:
            self.new_array.append(min(self.array))
            self.index += 1
            self.ordenar()
        else:
            

        
