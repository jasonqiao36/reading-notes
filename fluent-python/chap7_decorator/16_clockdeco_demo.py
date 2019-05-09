import time


# 把15的装饰器复制过来
def clock(func):
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        cost = time.perf_counter() - start
        print(f'{func.__name__} cost {cost}')
        return result

    return clocked


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def hello(name):
    return f'hello {name}'


if __name__ == '__main__':
    hello('jason')
    print(hello.__name__)  # clocked 。函数名被改变了
