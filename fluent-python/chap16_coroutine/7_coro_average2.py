from collections import namedtuple

Result = namedtuple('Result', ('average', 'count'))


def coroaverage2():
    total = 0
    count = 0
    average = None
    while True:
        item = yield
        if item is None:
            break
        count += 1
        total += item
        average = total / count
    return Result(average, count)
