def coroaverage():
    total = 0
    count = 0
    average = None
    while True:
        item = yield average
        total += item
        count += 1
        average = total / count
