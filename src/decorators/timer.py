def timer(func):
    from datetime import datetime
    import time
    from rich import print
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("".center(75, "="))
        print(f'[bold yellow]Function[/bold yellow]: {func.__name__}')
        for arg in args:
            print(f'[bold magenta]Arg[/bold magenta]: {arg}')
        for kwarg in kwargs:
            print(f'[bold magenta]Kwarg[/bold magenta]: {kwarg} = {kwargs[kwarg]}')
        if func.__doc__:
            print(f"[bold blue]Docstring[/bold blue]: {func.__doc__}")
        print('[bold green]Date Time[/bold green]:', datetime.now().strftime(format="%d/%m/%Y - %H:%M:%S"))
        print("".center(75, "-"))
        
        result = func(*args, **kwargs)
        
        print("".center(75, "-"))
        end_time = time.time()
        tempo = end_time - start_time
        print(f"{tempo:.3f} seconds")
        print("".center(75, "="))

        return result

    return wrapper