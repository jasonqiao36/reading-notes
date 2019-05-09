registry = set()


def register(is_active=True):
    def decorate(func):
        print(f'running register(is_active={is_active}) -> decorate({func})')
        if is_active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(is_active=False)
def f1():
    print('running f1')


@register(is_active=True)
def f2():
    print('running f2')


if __name__ == '__main__':
    f1()
