from clases.insercion import *
from clases.topologia import *

if __name__ == "__main__":

    print("Ordenación por inserción")
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(array)
    lista_ordenar = Insercion(array)
    print(lista_ordenar.ordenar())

    print("Ordenación topológica")


