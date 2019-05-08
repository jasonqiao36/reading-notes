import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]  # 干草垛
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]  # 针

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def demo(binsect_fn):
    for needle in reversed(NEEDLES):
        position = binsect_fn(HAYSTACK, needle)
        offset = position * '  | '
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        binsect_fn = bisect.bisect_left
    else:
        binsect_fn = bisect.bisect

    print('Demo: ', binsect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(binsect_fn)
