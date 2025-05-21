import logging
from constants.paths import LOG_FOLDER


def timer(func):
    from datetime import datetime
    import time
    from rich import print
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("".center(75, "="))
        print(f'[bold yellow]Function[/bold yellow]: {func.__name__}')
        print(f'[bold magenta]Arguments[/bold magenta]: {args}')
        print(f'[bold magenta]KeyWord arguments[/bold magenta]: {kwargs}')
        print(f"[bold blue]Description[/bold blue]: {func.__doc__}")
        print('[bold green]Date Time[/bold green]:', datetime.now().strftime(format="%d/%m/%Y - %H:%M:%S"))
        print("".center(75, "-"))
        
        result = func(*args, **kwargs)
        
        print("".center(75, "-"))
        end_time = time.time()
        result = end_time - start_time
        print(f"{result:.3f} seconds")
        print("".center(75, "="))

        return result

    return wrapper