import pandas as pd

class Electrodata():
    def __init__(self, ruta):
        self.datos = pd.read_csv(ruta)
        self.datos.rename(
            columns = {
                'Código universal de punto de suministro': 'Cliente',
                },
            inplace = True)
        self.datos['etiqueta'] = self.datos['datetime']
        self.datos['datetime'] = pd.to_datetime(self.datos['datetime'], format = '%Y-%m-%d %H:%M:%S')

    def cabeza(self, nrows):    # Un ejemplo
        return self.datos.head(nrows)

    def cola(self, nrows):
        return self.datos.tail(nrows)

    def suministro(self, id_suministro):
        pass

    def cliente(self, cliente, inicio, fin):
        self.df_cliente = self.datos[self.datos['Cliente'] == cliente][self.datos['datetime'] <= fin][self.datos['datetime'] >= inicio]
        datetimes = self.df_cliente['etiqueta'].tolist()
        consumo = self.df_cliente['Consumo'].tolist()
        # SELECT date, consumo FROM tabla WHERE cliente = cliente
        # [(16-02-2024 20:46, 10), ()]
        return datetimes, consumo

# Para probar el código de pandas
if __name__ == '__main__':
    datos = Electrodata("electrodatos/datos/electrodatos.csv")
    print(datos.cliente(8))
