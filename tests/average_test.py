from iterators_and_generators.average import average


def average_test():
    generator = average()
    for i in [1, 2, 3, 5, 7, 11]:
        next(generator)
        print("Average:", generator.send(i))
