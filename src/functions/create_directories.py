from rich import print
from decorators.timer import timer
from constants.paths import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER, OK, RUNNING

LIST_DIRECTORIES = [
    SCRIPT_FOLDER,
    SQL_FOLDER,
    EXCEL_FOLDER,
    LOG_FOLDER
]
@timer
def create_directories():
    """Create necessary directories for the project."""

    print("\nStarting directory creation process.\n")

    for dir in LIST_DIRECTORIES:
        if dir.exists():
            print(f"{OK} Directory already exists: {dir}\n")
        else:
            print(f"{RUNNING} Creating directory: {dir}")

            dir.mkdir(parents=True, exist_ok=True)

            print(f"{OK} Created directory: {dir}\n")
    print("Directory creation process completed successfully!")
