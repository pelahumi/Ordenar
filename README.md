# Ordenar
La dirección de este repositorio es: [GitHub](https://github.com/pelahumi/Ordenar)

## Ejercicio ordenación por inserción

![Diagrama](https://github.com/pelahumi/Ordenar/blob/main/Diagramas_flujo/Captura%20de%20pantalla%202022-03-06%20a%20las%2018.23.21.png)

```python3
#Creamos la clase

class Insercion():
    pass #Ponemos un pass porque definiremos los atributos más adelante

    #Creamos el constructor, con los atributos de la clase
    def __init__(self, array):
        self.array = array

    #Creamos el método para ordenar nuestro array
    def ordenar(self):
        #Este bucle recorre los elementos del array empezando por el segundo elemento
        for i in range(1, len(self.array)):
            num = self.array[i]
            index = i - 1 #Con este índice llamaremos a los elementos anteriores a num
            #En este bucle comparamos los elementos anteriores a num y si son mas grandes los intercambiamos
            while index >= 0 and num < self.array[index]:
                self.array[index + 1] = self.array[index]
                index -= 1
            self.array[index + 1] = num
        return "La lista ordenada: {}".format(self.array)
```

## Ejercicio ordenación topológica

![Diagrama]

```python3
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
        
        resultado = resultado[::-1] #Damos el resultado en orden inverso
        
        return "El resultado es: {}".format(resultado)
```

## Ejercicio especificaciones

![Diagrama](

```python3
#Creamos la clase
class Segmento():
    pass

    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla

    #Creamos el primer método
    def especificaciones(self):
        seg = []

        # Bucle que busca los elementos que son mayores al que tienen a su derecha
        for i in range(len(self.tabla) - 1):

            if self.tabla[i] >= self.tabla[i + 1]:
                seg.append(self.tabla[i])

                if self.tabla[i + 1] < self.tabla[i + 2]:
                    seg.append(self.tabla[i + 1])

                    seg2 = []

                    # Este bucle hace lo mismo que el anterior pero con un rango distinto

                    for j in range(i + 2, len(self.tabla) - 1):

                        if self.tabla[j] >= self.tabla[j + 1]:

                            seg2.append(self.tabla[j])

                            return seg, seg2
            
            else:
                pass
            
        return "Segmentado: {}, {}".format(seg, seg2)

    # Método que aplica las especificaciones del enunciado
    def explorar(self, lista):

        # Copia de seguridad
        mi = lista[0]

        # Mover los elementos un lugar a la izquierda
        lista = lista[1:] + lista[:1]

        return "Aplicando las especificaciones: {}".format(lista)




    
    
    
