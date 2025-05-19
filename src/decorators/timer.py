import logging
from constants.paths import LOG_FOLDER

def logger():
    """Configure the logger for the application."""
    LOG_FOLDER.mkdir(parents=True, exist_ok=True)  
    logging.basicConfig(
        filename=LOG_FOLDER / 'DataAnalytics.log',
        filemode='a',
        format='%(message)s',
        level=logging.DEBUG,
        encoding='utf-8'
    )
    return logging.getLogger()


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

        # Log details.
        logger().debug("".center(75, "="))
        logger().debug(f'Function: {func.__name__}')
        logger().debug(f'Arguments: {args}')
        logger().debug(f'KeyWord arguments: {kwargs}')
        logger().debug(f'Description: {func.__doc__}')
        logger().debug(f'Date/Time: {datetime.now().strftime(format="%d/%m/%Y - %H:%M:%S")}')

        
        result = func(*args, **kwargs)
        
        print("".center(75, "-"))
        end_time = time.time()
        result = end_time - start_time
        print(f"{result:.3f} seconds")
        print("".center(75, "="))

        return result

    return wrapper