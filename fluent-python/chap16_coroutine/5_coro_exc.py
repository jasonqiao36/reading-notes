class DemoException(Exception):
    ...


def coro_exc_handling():
    while True:
        try:
            x = yield
        except DemoException:
            print('exception')
        else:
            print(f'receive: x={x}')
    raise RuntimeError('this line never reached')
