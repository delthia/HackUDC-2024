from datetime import date
from .report_gen import ReportGenerator

class DayReport(ReportGenerator):
    def __init__(self, id_client: int, dt: date):
        self.dt = dt
        super().__init__(id_client)
    
    @property
    def day_consume(self):
        """Devuelve el consumo eléctrico del día seleccionado"""
        return self.database[self.database['Fecha'] == self.dt]
