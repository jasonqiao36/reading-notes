"""
bool(x)的背后是调用x.__bool__()
如果不存在x.__bool__(), 则调用x.__len__()
"""


class Product:
    def __init__(self, price, status):
        self.price = price
        self.status = status

    def __bool__(self):
        return bool(self.price)

    def __len__(self):
        return bool(self.status)


if __name__ == '__main__':
    p = Product(1, 0)
    print(bool(p))  # True
