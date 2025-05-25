from pathlib import Path
from datetime import datetime
USER_HOME = Path.home()

SCRIPT_FOLDER = USER_HOME / "DataAnalytics"

EXCEL_FOLDER = SCRIPT_FOLDER / "Excel"

LOG_FOLDER = SCRIPT_FOLDER / "Logs"

SQL_FOLDER = SCRIPT_FOLDER / "Banco de dados"


OK = '[[green]✓[/green]]'

ERROR = '[[red]✗[/red]]'

MONTHS = [
    "01-Janeiro",
    "02-Fevereiro",
    "03-Março",
    "04-Abril",
    "05-Maio",
    "06-Junho",
    "07-Julho",
    "08-Agosto",
    "09-Setembro",
    "10-Outubro",
    "11-Novembro",
    "12-Dezembro"
]

CATEGORIES = [
    'Seco',
    'Resfriado',
    'Congelado',
    'Ultra Congelado'
]
