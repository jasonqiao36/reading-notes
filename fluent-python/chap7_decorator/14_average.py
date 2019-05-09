def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return average
