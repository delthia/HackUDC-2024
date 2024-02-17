from calendar import month_name
from .report_gen import ReportGenerator
from math import ceil
import pandas as pd
    
class AnnualReport(ReportGenerator):
    """Reporte anual del consumo eléctrico de un cliente en específico"""
    def __init__(self, id_client: int, year: int):
        self.id_client = id_client
        self.year = year
        super().__init__(id_client)
    
    @property
    def year_db(self) -> pd.DataFrame:
        return self.database[self.database['Year'] == self.year]
    
    @property
    def monthly_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada mes"""
        df_monthcons = self.year_db.groupby(by = 'Month').agg({'Consumo': 'sum'})
        df_monthcons.sort_index(inplace = True)
        # df_monthcons.index = [month_name[m] for m in df_monthcons.index]
        return df_monthcons
    
    @property
    def trimestral_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada trimestre""" 
        q_trims = ceil(self.year_db['Month'].max() / 3)
        trims = pd.cut(
            self.year_db['Month'], 
            bins = q_trims, 
            labels = ['Trim_%d'%(i+1) for i in range(q_trims)])
        df_trimcons = self.year_db.copy()
        df_trimcons['Trim'] = trims
        df_trimcons = df_trimcons.groupby(by = 'Trim').agg({'Consumo': 'sum'})
        return df_trimcons
    
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
