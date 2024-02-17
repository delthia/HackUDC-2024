# ElektroGraphs - información sobre el consumo eléctrico
# Copyright (C) 2024  <Hugo H. Carlos FOL. Iago R.>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .report_gen import ReportGenerator
from math import ceil
import pandas as pd
    
class AnnualReport(ReportGenerator):
    """Reporte anual del consumo eléctrico de un cliente en específico"""
    def __init__(self, id_client: int, year: int):
        self.id_client = id_client
        self.year = year
        super().__init__(id_client)
        self.database = self.database[self.database['Year'] == self.year]
    
    @property
    def monthly_comparison(self) -> pd.DataFrame:
        """Presenta el consumo eléctrico de cada mes"""
        df_monthcons = self.database.groupby(by = 'Month').agg({'Consumo': 'sum'})
        df_monthcons.sort_index(inplace = True)
        if df_monthcons.shape[0] < 12:
            df_monthcons = df_monthcons.reindex(range(1, 13), fill_value=0)
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
