def simple_coro(a):
    print(f'receive: a={a}')
    b = yield a
    print(f'receive: b={b}')
    c = yield a + b
    print(f'receive: c={c}')
