"""
具名元组
"""
from collections import namedtuple

Product = namedtuple('Product', ('name', 'price', 'city'))

p = Product('手机', '5000', 'sh')
print(p.name, p.price)  # 手机，5000
print(p[0])  # 手机

print(Product._fields)  # ('name', 'price', 'city')
params = ('手机', '5000', 'sh')
print(Product._make(params))  # 生成实例==Product(*params)

for k, v in p._asdict().items():
    print(k, v)
