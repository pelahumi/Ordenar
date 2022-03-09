#Creamos la clase

class Topologica():
    pass #ponemos un pass porque definiremos luego los atributos de la clase

    #Definimos el constructor con los atributos de la clase

    def __init__(self, array):
        self.array = array
        self.new_array = []
        self.index = 0
    
    #Definimos el método de la clase que nos ordenará el array

    def ordenar(self):
        
        minimo = min(array)

        if self.index <= len(self.array):
            self.new_array.append(minimo)
            array.remove(minimo)
            self.ordenar()
        else:
            return "El array ordenado es: {}".format(self.new_array)

if __name__ == "__main__":
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(min(array))
    #Creamos el objeto
    lista = Topologica(array)
    print(lista.ordenar())

            


        
