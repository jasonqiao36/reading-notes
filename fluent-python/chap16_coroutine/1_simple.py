def coroutine():
    print('started')
    x = yield
    print('received:', x)


co = coroutine()
next(co)

co.send(1)
