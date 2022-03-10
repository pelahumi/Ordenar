# Ordenar
La dirección de este repositorio es: [GitHub](https://github.com/pelahumi/Ordenar)

## Ejercicio ordenación por inserción

![Diagrama](https://github.com/pelahumi/Ordenar/blob/main/Diagramas_flujo/Captura%20de%20pantalla%202022-03-06%20a%20las%2018.23.21.png)

```
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
    
if __name__ == "__main__":
    array = [13, 56, 77, 2, 27, 89, 71, 19, 33]
    print(array)
    lista_ordenar = Insercion(array) #Creamos nuestro objeto
    print(lista_ordenar.ordenar())
    
    
    
    
    
