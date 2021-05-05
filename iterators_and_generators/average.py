def average():
    elements_sum = 0
    i = 0
    while True:
        a = (yield)
        elements_sum += a
        i += 1
        print("Got:", a)
        print("Sum:", elements_sum)
        print("i-elem: ", i)
        yield elements_sum / i
