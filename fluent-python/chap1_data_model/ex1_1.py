import collections

card = collections.namedtuple('Card', ['suit', 'rank'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('AJQK')
    suits = '红桃 方片 梅花 黑桃'.split()

    def __init__(self):
        self._cards = [card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = {
    '黑桃': 3,
    '红桃': 2,
    '梅花': 1,
    '方片': 0,
}


def heitao_high(card):
    """
    自定义一套排序规则
    """
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def use_deck():
    c = card('红桃', '3')
    print(c)
    # output
    """
    Card(suit='红桃', rank='3')
    """

    d = Deck()
    print('牌的数量:', len(d))
    print('第一张牌：', d[0])
    print('最后一张：', d[-1])
    # output
    """
    牌的数量: 52
    第一张牌： Card(suit='红桃', rank='2')
    最后一张： Card(suit='黑桃', rank='K')
    """

    # 随机取一张
    from random import choice
    print(choice(d))
    print(choice(d))
    # output
    """
    Card(suit='黑桃', rank='9')
    Card(suit='梅花', rank='5')
    """

    # 迭代(实现__getitem__)
    for card_item in d[:3]:
        print(card_item)
    # output
    """
    Card(suit='红桃', rank='2')
    Card(suit='红桃', rank='3')
    Card(suit='红桃', rank='4')
    """

    # 反向迭代
    for card_item in reversed(d[:3]):
        print(card_item)
    # output
    """
    Card(suit='红桃', rank='4')
    Card(suit='红桃', rank='3')
    Card(suit='红桃', rank='2')
    """

    # 迭代搜索
    print(card('黑桃', 6) in d)


if __name__ == '__main__':
    use_deck()
