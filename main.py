from ejercicios.insercion_dicotomica import Insercion
from ejercicios.topologica import Topologica

if __name__ == "__main__":

    print("Ordenación por inserción")
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(array)
    lista_ordenar = Insercion(array)
    print(lista_ordenar.ordenar())

    print("Ordenación topológica")


