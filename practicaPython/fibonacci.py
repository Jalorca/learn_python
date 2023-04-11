def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i, x in enumerate(fib()):
    if i == 10:
        break
    print("{}".format(x), end="")
