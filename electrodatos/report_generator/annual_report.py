from calendar import month_name
from electrodatos.report_generator.ElectroDB import electro_data
from math import ceil
import pandas as pd

class AnnualReport:
    """Reporte anual del consumo eléctrico de un cliente en específico"""
    def __init__(self, id_client: int, year: int):
        self.year = year
        self.id_client = id_client
        self.__data_client = electro_data[electro_data['Cliente'] == id_client]
    
    @property
    def database(self) -> pd.DataFrame:
        return self.__data_client[self.__data_client['Year'] == self.year]
    
    @property
    def monthly_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada mes"""
        df_monthcons = self.database.groupby(by = 'Month').agg({'Consumo': 'sum'})
        df_monthcons.sort_index(inplace = True)
        df_monthcons.index = [month_name[m] for m in df_monthcons.index]
        return df_monthcons
    
    @property
    def trimestral_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada trimestre""" 
        q_trims = ceil(self.database['Month'].max() / 3)
        trims = pd.cut(
            self.database['Month'], 
            bins = q_trims, 
            labels = ['Trim_%d'%(i+1) for i in range(q_trims)])
        df_trimcons = self.database.copy()
        df_trimcons['Trim'] = trims
        df_trimcons = df_trimcons.groupby(by = 'Trim').agg({'Consumo': 'sum'})
        return df_trimcons

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
        df_rangecons = self.__data_client[
            (inicio <= self.__data_client.Fecha) &
            (self.__data_client.Fecha <= fin)
            ]
        df_rangecons = df_rangecons.groupby(by = 'Fecha').agg({'Consumo': 'sum'})
        return df_rangecons.loc[:, ['Fecha', 'Consumo']]
    
    @property
    def annual_comparison(self) -> pd.DataFrame:
        """Comparación con el año anterior"""
        df_oldata = AnnualReport(id_client = self.id_client, year = self.year - 1)
        df_comparison = pd.merge(
            left = self.monthly_comparison,
            right = df_oldata.monthly_comparison,
            left_index = True, right_index = True,
            suffixes = [f'_{self.year}', f'_{self.year - 1}']
        )
        return df_comparison