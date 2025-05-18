def timer(func):
    from datetime import datetime
    import time
    from rich import print
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("".center(100, "="))
        print(f"[yellow]Function[/yellow]: {func.__name__}")
        print(f"[magenta]Arguments[/magenta]: {args}, {kwargs}")
        print(datetime.now().strftime(format="%d-%m-%Y %H:%M:%S"))
        print("".center(100, "-"))
        result = func(*args, **kwargs)
        print("".center(100, "-"))
        end_time = time.time()
        result = end_time - start_time
        print(datetime.now().strftime(format="%d-%m-%Y %H:%M:%S"))
        print(f"{result:.3f} seconds")
        print("".center(100, "="))

        return result

    return wrapper