from collections import defaultdict

#Creamos la clase
class Topologica():
    pass #ponemos un pass porque definiremos luego los atributos de la clase

    #Definimos el constructor
    def __init__(self, v):
        self.v = v
        self.tarea = defaultdict(list)

    def añadir(self, index, vertice):
        self.tarea[index].append(vertice)

    def ordenar(self, vertice, lista, resultado):

        lista[vertice] = True

        for i in self.tarea[vertice]:
            if lista[i] == False:
                self.ordenar(i, lista, resultado)
        
        resultado.append(vertice)

    def ordenacion_topologica(self):
        lista = [False] * self.v
        resultado = []

        for i in range(self.v):
            if lista[i] == False:
                self.ordenar(i, lista, resultado)
        
        return "El resultado es: {}".format(resultado)

if __name__ == "__main__":
    tarea = Topologica(5)
    tarea.añadir(0, 3)
    tarea.añadir(2, 1)
    tarea.añadir(4, 1)
    tarea.añadir(2, 3)
    tarea.añadir(0, 2)

    print(tarea.ordenacion_topologica())
            


        
