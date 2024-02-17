import pandas as pd

class ConsumoElectrico:
    """Base de datos del consumo electrico de 11 hogares

    Base de datos que registra el consumo electrico real 
    y estimado de un hogar a una hora determinada y 
    medida en KW/h
    """
    def __init__(self):
        self.__df_electrodatos = pd.read_csv(
            # 'electrodatos/datos/electrodatos.csv'
            '/home/carlosfol/My_Documents/Git_Projects/ElectroDatos/HackUDC-2024/electrodatos/datos/electrodatos.csv'
            )
        self.__df_electrodatos.rename(
            columns = {
                'Código universal de punto de suministro': 'Cliente',
                'Método de obtención': 'Method'
            },
            inplace = True)
        # self.__df_electrodatos.set_index('Cliente', inplace = True)

    def __format_datetime(self) -> None:
        """Dar fomato a la columna relacionada con la fecha y hora de registro"""
        datetimes = pd.to_datetime(self.__df_electrodatos['datetime'])
        self.__df_electrodatos['Fecha'] = datetimes.apply(lambda x: x.date())
        self.__df_electrodatos['Hora'] = datetimes.apply(lambda x: x.time())
        self.__df_electrodatos.drop(['datetime'], axis = 1, inplace = True)

    def __date_cols(self) -> None:
        """Agregar el nombre del mes y dia
        
        Añadir columnas que referencien el año, mes y dia
        para facilitar el analsis de los datos
        """
        self.__df_electrodatos['Year'] = self.__df_electrodatos['Fecha'].apply(
            lambda x: x.year)
        self.__df_electrodatos['Month'] = self.__df_electrodatos['Fecha'].apply(
            lambda x: x.month)
        self.__df_electrodatos['Day'] = self.__df_electrodatos['Fecha'].apply(
            lambda x: x.day)
        self.__df_electrodatos['WeekDay'] = self.__df_electrodatos['Fecha'].apply(
            lambda x: x.weekday())
        
    @property
    def database(self) -> pd.DataFrame:
        """Base de datos procesada"""
        self.__format_datetime()
        self.__date_cols()
        return self.__df_electrodatos

if __name__ == '__main__':
    consumo = ConsumoElectrico()
    print(consumo.database['WeekDay'].value_counts())
