from random import randint


def slot_machine(n: int):
    """
    :param n: int
    :return: int
    """

    while n > 0:
        if n > 2:
            x = randint(1, 2)
            n = n - x
            yield x
        else:
            yield n
            n = 0
