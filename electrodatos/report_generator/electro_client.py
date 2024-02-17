from electrodatos.report_generator.Modalidad import AnnualReport, MonthlyReport, DayReport
# from Modalidad import AnnualReport, MonthlyReport, DayReport, ReportGenerator
from datetime import datetime, date

class ClientElectro:
    """"Agrupa los atributos y métodos útiles para describir a un cliente"""
    def __init__(self, id_client):
        self.id_client = id_client
    
    def electro_report(self, reporte: str = None, year: int = None, month: int = None, date: datetime = None):
        if reporte == 'Annual':
            return AnnualReport(self.id_client, year)
        elif reporte == 'Monthly':
            return MonthlyReport(self.id_client, year, month)
        elif reporte == 'Day':
            return DayReport(self.id_client, date)
        else:
            return ReportGenerator(self.id_client)

if __name__ == '__main__':
    client_0 = ClientElectro(id_client=4).electro_report()
    inicio = date(2023, 1, 10); fin = date(2023, 2, 28)
    # reporte_client_0 = client_0.electro_report('Annual', 2023)
    # x = client_0.electro_report().range_consume(inicio, fin)
    print(client_0.range_consume(inicio, fin))
