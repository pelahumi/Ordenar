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
        if self.index <= len(self.array):
            if  self.array[self.index] <= self.minimo:
                self.new_array.append(self.array[self.index])
                self.index += 1
                self.ordenar()
                
            else:
                self.index += 1
                self.ordenar()
        else:
            return "El array ordenado es: {}".format(self.new_array)

if __name__ == "__main__":
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    #Creamos el objeto
    lista = Insercion(array)
    print(lista.ordenar())

            


        
