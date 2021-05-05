x = 1337

def foo():
    def bar():
        nonlocal x
        x += 1

    x = 0
    print(x)
    bar()
    print(x)


