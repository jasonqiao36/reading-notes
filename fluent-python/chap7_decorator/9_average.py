def make_average():
    items = []

    def average(new_value):
        items.append(new_value)
        return sum(items) / len(items)

    return average
