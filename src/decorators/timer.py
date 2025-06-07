def timer(func):
    from datetime import datetime
    import time
    from rich import print
    from log.log import log
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("".center(75, "="))
        print(f'[bold yellow]Function[/bold yellow]: {func.__name__}')
        log().debug(f'Function: {func.__name__}')
        for arg in args:
            print(f'[bold magenta]Arg[/bold magenta]: {arg}')
            log().debug(f'Arg: {arg}')
        for kwarg in kwargs:
            print(f'[bold magenta]Kwarg[/bold magenta]: {kwarg} = {kwargs[kwarg]}')
            log().debug(f'KwArg: {kwarg}')
        if func.__doc__:
            print(f"[bold blue]Docstring[/bold blue]: {func.__doc__}")
            log().debug(f'Docstring: {func.__doc__}')
        print('[bold green]Date Time[/bold green]:', datetime.now().strftime(format="%d/%m/%Y - %H:%M:%S"))
        log().debug(f'Date Time: {datetime.now().strftime(format='%d/%m/%Y - %H:%M:%S')}')
        print("".center(75, "-"))
        
        result = func(*args, **kwargs)
        
        print("".center(75, "-"))
        end_time = time.time()
        tempo = end_time - start_time
        print(f"{tempo:.3f} seconds")
        log().debug(f'{tempo:.3f} seconds')
        log().debug('=====================================================')
        print("".center(75, "="))

        return result

    return wrapper

