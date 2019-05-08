class Product:
    def __str__(self):
        """展示给终端用户。str()或print时调用"""
        return 'str product'

    def __repr__(self):
        """调试、记录日志"""
        return 'repr product'


if __name__ == '__main__':
    p = Product()
    print(p)
