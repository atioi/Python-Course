import math


def is_prime(n):
    """
    Check if param n is prime number.
    :param n: int
    :return: bool
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True


def prime_gen(n):
    """
    Return prime numbers generator from 2 through n
    :param n: int
    :return: generator
    """
    x = 2
    while x < n:
        if is_prime(x):
            yield x
        x += 1
