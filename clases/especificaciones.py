#Creamos la clase
class Segmento():
    pass

    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla

    #Creamos el primer método
    def segmentos(self):
        seg = []

        for i in range(len(self.tabla) - 1):
            if self.tabla[i] >= self.tabla[i + 1]:
                seg.append(self.tabla[i])
            else:
                pass
