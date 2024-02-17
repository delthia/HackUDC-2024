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

from electrodatos.report_generator.Modalidad import AnnualReport, MonthlyReport, DayReport, ReportGenerator
# from Modalidad import AnnualReport, MonthlyReport, DayReport, ReportGenerator
from datetime import date
import pandas as pd

class ClientElectro:
    """"Agrupa los atributos y métodos útiles para describir a un cliente"""
    def __init__(self, id_client):
        self.id_client = id_client
    
    def electro_report(self, reporte: str = None, year: int = None, month: int = None, dt: date = None):
        if reporte == 'Annual':
            return AnnualReport(self.id_client, year)
        elif reporte == 'Monthly':
            return MonthlyReport(self.id_client, year, month)
        elif reporte == 'Day':
            return DayReport(self.id_client, dt)
        else:
            return ReportGenerator(self.id_client)

if __name__ == '__main__':
    client_0 = ClientElectro(id_client=0).electro_report(reporte='Day', dt=date(2021, 8, 5))
    # inicio = date(2023, 1, 10); fin = date(2023, 2, 28)
    # reporte_client_0 = client_0.electro_report('Annual', 2023)
    print(client_0.day_consume)
