from tests.multiply_lists_test import multiply_lists_test
from tests.average_test import average_test
from tests.nonlocal_1_test import nonlocal_test

# multiply_lists_test()
# average_test()
nonlocal_test()

x = 1337


def foo():
    def bar():
        x += 1

    x = 0
    print(x)
    bar()
    print(x)


print(x)
foo()
print(x)