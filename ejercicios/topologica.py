from collections import defaultdict

#Creamos la clase
class Topologica():
    pass #ponemos un pass porque definiremos luego los atributos de la clase

    #Definimos el constructor
    def __init__(self, v):
        self.v = v
        self.tarea = defaultdict(list)

    # Creamos un método para ir añadiendo los vértices a una lista "resultado"
    def añadir(self, index, vertice):
        self.tarea[index].append(vertice)

    #Creamos un método para ir ordenando los vértices
    def ordenar(self, vertice, lista, resultado):

        #Marca el vértice como visto
        lista[vertice] = True

        #Bucle para que aplique este método a todos los vértices de la lista
        for i in self.tarea[vertice]:
            if lista[i] == False:
                self.ordenar(i, lista, resultado)
        
        resultado.append(vertice)

    # Método que usará el anterior para odenar los vértices
    def ordenacion_topologica(self):

        #Marcamos todos los vértices como "no vistos"
        lista = [False] * self.v
        resultado = [] #Lista donde estará el resultado ordenado

        #Bucle que aplica el método anterior a los vértices
        for i in range(self.v):
            if lista[i] == False:
                self.ordenar(i, lista, resultado)

        resultado = resultado[::-1]
        return "El resultado es: {}".format(resultado)

if __name__ == "__main__":
    tarea = Topologica(5)
    tarea.añadir(0, 3)
    tarea.añadir(2, 1)
    tarea.añadir(4, 1)
    tarea.añadir(2, 3)
    tarea.añadir(0, 2)

    print(tarea.ordenacion_topologica())
            


        
