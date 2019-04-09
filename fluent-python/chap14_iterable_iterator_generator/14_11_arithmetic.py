class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end
        self.count = 0

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def test_progression():
    ap = ArithmeticProgression(0, 1, 3)
    assert list(ap) == [0, 1, 2]


"""
答复（ https://mail.python.org/pipermail/python-list/2014-December/682651.html）
"""
