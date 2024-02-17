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

from datetime import date
from .report_gen import ReportGenerator

class DayReport(ReportGenerator):
    def __init__(self, id_client: int, dt: date):
        self.dt = dt
        super().__init__(id_client)
    
    @property
    def day_consume(self):
        """Devuelve el consumo eléctrico del día seleccionado"""
        dia = self.database[self.database['Fecha'] == self.dt] 
        return dia['Consumo'][5:].to_list() + dia['Consumo'][:5].to_list()
