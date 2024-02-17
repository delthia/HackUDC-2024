from .report_gen import ReportGenerator

class MonthlyReport(ReportGenerator):
    def __init__(self, id_client: int, year: int, month: int) -> None:
        super().__init__(id_client)
        self.year = year
        self.month = month
    
    @property
    def month_db(self):
        return self.database[(self.database['Year'] == self.year) & 
                             (self.database['Month'] == self.month)]
