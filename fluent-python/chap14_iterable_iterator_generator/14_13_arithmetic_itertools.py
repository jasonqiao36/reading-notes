import itertools


def arithmetic_progression(begin, step, end):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


def test_progression():
    ap = arithmetic_progression(0, 1, 3)
    assert list(ap) == [0, 1, 2]
