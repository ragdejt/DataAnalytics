from pathlib import Path
from rich import print

USER_HOME = Path.home()

SCRIPT_FOLDER = USER_HOME / "DataAnalytics"

SQL_FOLDER = SCRIPT_FOLDER / "Banco de dados"

EXCEL_FOLDER = SCRIPT_FOLDER / "Excel"

LOG_FOLDER = SCRIPT_FOLDER / "Logs"


OK = '[[green]✓[/green]]'

RUNNING = '[[yellow]-[/yellow]]'

ERROR = '[[red]✗[/red]]'