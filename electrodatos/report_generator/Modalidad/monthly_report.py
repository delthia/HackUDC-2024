from .report_gen import ReportGenerator
import pandas as pd

class MonthlyReport(ReportGenerator):
    def __init__(self, id_client: int, year: int, month: int) -> None:
        super().__init__(id_client)
        self.year = year
        self.month = month
        self.database = self.database[(self.database['Year'] == self.year) & 
                             (self.database['Month'] == self.month)]
    
    # @property
    # def weekly_comparison(self) -> pd.DataFrame:
    #     """Presenta el consumo eléctrico total por semana"""
    #     weeks = pd.cut(
    #         self.database['Day'], 
    #         bins = 4, 
    #         labels = ['Semana_%d'%(i+1) for i in range(4)])
    #     df_weekcons = self.database.copy()
    #     df_weekcons['Week'] = weeks
    #     df_weekcons = df_weekcons.groupby(by = 'Week').agg({'Consumo': 'sum'})
    #     return df_weekcons
    