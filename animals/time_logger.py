from time import perf_counter


def time_logger(func: callable):
    def wrapper(*args, **kwargs):
        t0 = perf_counter()
        func(*args, **kwargs)
        t1 = perf_counter()
        print(f'LOGGER: вызов метода {func.__name__} занял {t1 - t0:.6f} секунд')

    return wrapper
