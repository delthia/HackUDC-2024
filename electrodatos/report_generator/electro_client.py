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