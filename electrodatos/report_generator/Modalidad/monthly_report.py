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
import pandas as pd

class MonthlyReport(ReportGenerator):
    def __init__(self, id_client: int, year: int, month: int) -> None:
        super().__init__(id_client)
        self.year = year
        self.month = month
        self.database = self.database[(self.database['Year'] == self.year) & 
                             (self.database['Month'] == self.month)]
    