from electrodatos.report_generator.ElectroDB import electro_data
import pandas as pd

class ReportGenerator:
    def __init__(self, id_client: int) -> None:
        self.id_client = id_client
        self.__df_client = electro_data[electro_data['Cliente'] == id_client]
    
    @property
    def database(self) -> pd.DataFrame:
        return self.__df_client
    
    @property
    def week_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico promedio durante la semana.
        
        Esta relación permite conocer en qué día de la semana se realiza
        el mayor consumo eléctrico de media entre todos los días del año.
        """
        day_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_names = {i: day for i, day in enumerate(day_names)}
        df_weekcons = self.database.copy()
        df_weekcons = df_weekcons.groupby(by = 'WeekDay').agg({'Consumo': 'mean',
                                                             'Consumo': 'std'})
        df_weekcons.sort_index(inplace = True)
        df_weekcons.index = df_weekcons.index.map(lambda x: day_names[x])
        return df_weekcons
    
    @property
    def max_consumption(self) -> pd.DataFrame:
        """Identifica en qué momento del dia se realiza el mayor consumo eléctrico
        
        En qué hora del día se consume más de media entre todos los días del año
        """
        df_timecons = self.database.groupby(by = 'Hora').agg({'Consumo': 'mean'})
        df_timecons.sort_index(inplace = True)
        return df_timecons
    
    def range_consume(self, inicio, fin) -> pd.DataFrame:
        """Consumo electrico en la un rango establecido"""
        df_rangecons = self.database[
            (inicio <= self.database.Fecha) &
            (self.database.Fecha <= fin)
            ]
        df_rangecons = df_rangecons.groupby(by = 'Fecha').agg({'Consumo': 'sum'})
        return df_rangecons.loc[:, ['Fecha', 'Consumo']]
