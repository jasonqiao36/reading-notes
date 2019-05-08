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
