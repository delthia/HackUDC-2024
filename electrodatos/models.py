import pandas as pd

class Electrodata():
    def __init__(self, ruta):
        self.datos = pd.read_csv(ruta)

    def cabeza(self, nrows):
        return self.datos.head(nrows)

    def suministro(self, id_suministro):
        pass

    def rango(self, cliente, tiempo: tuple[datetime, datetime]):
        pass


datos = Electrodata("datos/electrodatos.csv")
print(datos.cabeza(8))
