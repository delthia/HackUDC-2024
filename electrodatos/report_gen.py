from calendar import month_name
from electro_db import ConsumoElectrico
from math import ceil
import pandas as pd

class AnnualReport:
    """Reporte anual del consumo eléctrico de un cliente en específico"""
    def __init__(self, id_client: int, year: int):
        electro_data = ConsumoElectrico(path = "datos/electrodatos.csv").database
        self.year = year
        self.__data_client = electro_data[
            (electro_data['Cliente'] == id_client) & (electro_data['Year'] == year)]
    
    @property
    def year_data(self):
        return self.__data_client
    
    @property
    def monthly_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada mes"""
        df_monthcons = self.year_data.groupby(by = 'Month').agg({'Consumo': 'sum'})
        df_monthcons.sort_index(inplace = True)
        df_monthcons.index = [month_name[m] for m in df_monthcons.index]
        return df_monthcons
    
    @property
    def trimestral_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada trimestre""" 
        q_trims = ceil(self.year_data['Month'].max() / 3)
        trims = pd.cut(
            self.year_data['Month'], 
            bins = q_trims, 
            labels = ['Trim_%d'%(i+1) for i in range(q_trims)])
        df_trimcons = self.year_data.copy()
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
        df_weekcons = self.year_data.copy()
        df_weekcons = df_weekcons.groupby(by = 'WeekDay').agg({'Consumo': 'mean',
                                                             'Consumo': 'std'})
        df_weekcons.sort_index(inplace = True)
        df_weekcons.index = df_weekcons.index.map(lambda x: day_names[x])
        return df_weekcons
    
    @property
    def max_consumption(self):
        """Identifica en qué momento del dia se realiza el mayor consumo eléctrico
        
        En qué hora del día se consume más de media entre todos los días del año
        """
        df_timecons = self.year_data.groupby(by = 'Hora').agg({'Consumo': 'mean'})
        df_timecons.sort_index(inplace = True)
        return df_timecons
    
    def comparacion_mes(self, mes):
        """Comparación con el mismo mes del año anterior"""
        df_oldata = 0

if __name__ == '__main__':
    report = AnualReport(0, 2022)
    print(report.time_consume)