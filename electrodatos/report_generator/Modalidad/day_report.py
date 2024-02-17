from datetime import datetime
from .report_gen import ReportGenerator

class DayReport(ReportGenerator):
    def __init__(self, id_client: int, date: datetime):
        self.date = date
        super().__init__(id_client)
    
    @property
    def day_db(self):
        """Devuelve el consumo eléctrico del día seleccionado"""
        dia = self.database[self.database['Fecha'] == self.date] 
        return dia['Consumo'][5:].to_list() + dia['Consumo'][:5].to_list()
