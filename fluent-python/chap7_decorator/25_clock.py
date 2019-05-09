import time

DEFAULT_FMT = '[{cost:0.8f}s] ({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            cost = time.perf_counter() - start
            # print(f'{func.__name__} cost {cost}')
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate


@clock()
def f1():
    print('hello')


if __name__ == '__main__':
    f1()
