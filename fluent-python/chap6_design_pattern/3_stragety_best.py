from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  # 姓名，积分


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion  # 积分

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f}, due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):  # 第一个策略
    """为积分1000以上的顾客提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):  # 第二个策略
    """单个商品20个以上时提供10%折扣"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total * 0.1
    return discount


def large_order_promo(order):  # 第三个策略
    """订单中不同商品达到10个以上时提供7%折扣"""

    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


promos = [large_order_promo, bulk_item_promo, fidelity_promo]


def best_promo(order):
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    jason = Customer('jason', 0)
    tom = Customer('tom', 1000)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(jason, cart, fidelity_promo))
    print(Order(tom, cart, fidelity_promo))
    print(Order(tom, cart, bulk_item_promo))
    print(Order(tom, cart, large_order_promo))
