from functools import wraps


def coroutine(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        c = f(*args, **kwargs)
        c.send(None)
        return c

    return _wrapper


#####
# 上一节的例子
#####

@coroutine
def coroaverage():
    total = 0
    count = 0
    average = None
    while True:
        item = yield average
        total += item
        count += 1
        average = total / count
