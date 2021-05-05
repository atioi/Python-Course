from iterators_and_generators.list_multiplier import multiply_lists
import numpy as np


def multiply_lists_test():
    try:
        a = [5, 3, 6, 1, 9]
        b = [4, 2, 3, 5, 1]
        print('Test function result: ', multiply_lists(a, b))
        print('Using numpy: ', np.sum(np.array(a) * np.array(b)))
    except Exception as exception:
        print(exception)
