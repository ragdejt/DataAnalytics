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
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

CATEGORIES = [
    'Seco',
    'Resfriado',
    'Congelado',
    'Ultra Congelado'
]
