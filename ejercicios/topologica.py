#Creamos la clase

class Topologica():
    pass #ponemos un pass porque definiremos luego los atributos de la clase

    #Definimos el constructor
    def __init__(self, vertices):
        self.vertices = vertices
        self.tarea = []

    def añadir(self,vertice, importancia):
        self.tarea[vertice].append(importancia)

    def ordenar(self, v, lista, resultado):
        lista.append(v)

        for i in self.vertices[v]:
            if i not in lista:
                self.ordenar(i, lista, resultado)
        
        resultado.insert(0, v)

    def ordenacion_topologica(self):
        lista = []
        resultado = []

        for j in list(self.vertices):
            if j not in lista:
                self.ordenar(j, lista, resultado)
        
        return "El resultado es: {}".format(resultado)

if __name__ == "__main__":
    tarea = Topologica(5)
    tarea.añadir(0, 3)
    tarea.añadir(2, 1)
    tarea.añadir(4, 1)
    tarea.añadir(2, 3)
    tarea.añadir(0, 2)

    tarea.ordenacion_topologica()

            


        
