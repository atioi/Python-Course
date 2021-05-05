def multiply_lists(a: list, b: list):
    if len(a) == len(b):
        return sum(x * y for x, y in zip(a, b))
    else:
        raise ValueError
