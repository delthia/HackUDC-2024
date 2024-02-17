from electrodatos.report_generator.annual_report import AnnualReport
from datetime import date
import pandas as pd

class ClientElectro:
    """"Agrupa los atributos y métodos útiles para describir a un cliente"""
    def __init__(self, id_client):
        self.id_client = id_client
    
    def electro_report(self, reporte: str, year: int, month: int = None):
        if reporte == 'Annual':
            return AnnualReport(self.id_client, year)

if __name__ == '__main__':
    client_0 = ClientElectro(id_client = 0)
    inicio = date(2022, 1, 1); fin = date(2022, 12, 31)
    # reporte_client_0 = client_0.electro_report('Annual', 2023)
    x = client_0.electro_report('Annual', 2023).range_consume(inicio, fin)
    print(x)