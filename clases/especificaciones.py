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
