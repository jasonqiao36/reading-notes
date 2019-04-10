class DemoException(Exception):
    ...


def coro_finally():
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('exception')
            else:
                print(f'receive: x={x}')
    finally:
        print('coro closed')
