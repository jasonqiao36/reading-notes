import time

from functools import lru_cache


# 把15的装饰器复制过来
def clock(func):
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        cost = time.perf_counter() - start
        print(f'{func.__name__}({args[0]}) cost {cost}')
        return result

    return clocked


@lru_cache()
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(30))
    print(fib.cache_info())
    print(fib.__wrapped__)