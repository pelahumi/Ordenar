#Creamos la clase

class Topologica():
    pass #Ponemos un pass porque definiremos los atributos más adelante

    #Creamos el constructor, con los atributos de la clase
    def __init__(self, array):
        self.array = array

    #Creamos el método para ordenar nuestro array
    def ordenar(self):
        #Este bucle recorre los elementos del array empezando por el segundo elemento
        for i in range(1, len(self.array)):
            num = self.array[i]
            index = i - 1
            #En este bucle
            while index >= 0 and num < self.array[index]:
                self.array[index + 1] = self.array[index]
                index -= 1
            self.array[index + 1] = num
        return "La lista ordenada: {}".format(self.array)
    
if __name__ == "__main__":
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(array)
    lista_ordenar = Topologica(array) #Creamos nuestro objeto
    print(lista_ordenar.ordenar())





