import time


def clock(func):
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        cost = time.perf_counter() - start
        print(f'{func.__name__} cost {cost}')
        return result

    return clocked
