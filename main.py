from clases.especificaciones import Segmento
from clases.insercion import *
from clases.topologia import *
from clases.especificaciones import * 


if __name__ == "__main__":

    print("Ordenación por inserción")
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(array)
    lista_ordenar = Insercion(array)
    print(lista_ordenar.ordenar())

    print("Ordenación topológica")
    tarea = Topologica(5)
    tarea.añadir(0, 3)
    tarea.añadir(2, 1)
    tarea.añadir(4, 1)
    tarea.añadir(2, 3)
    tarea.añadir(0, 2)
    print(tarea.ordenacion_topologica())

    print("Especificaciones")
    array = [13, 4, -3, 8, 9, 10, 7]
    exploracion = Segmento(array)
    print("El array a segmentar es el siguiente: ",array)
    print(exploracion.especificaciones())
    print(exploracion.explorar(exploracion.especificaciones()))




