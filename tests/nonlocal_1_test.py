from locals_globals.nonlocal_1 import foo, x


def nonlocal_test():
    print(x)
    foo()
    print(x)