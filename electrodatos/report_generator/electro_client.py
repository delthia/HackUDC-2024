from annual_report import AnnualReport

class ClientElectro:
    """"Agrupa los atributos y métodos útiles para describir a un cliente"""
    def __init__(self, id_client):
        self.id_client = id_client
    
    def electro_report(self, reporte: str, year: int, month: int = None):
        if reporte == 'Annual':
            return AnnualReport(self.id_client, year)

if __name__ == '__main__':
    client_0 = ClientElectro(id_client = 0)
    reporte_client_0 = client_0.electro_report('Annual', 2023)
    print(reporte_client_0.annual_comparison)