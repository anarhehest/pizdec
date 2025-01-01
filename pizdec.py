def foo(C:list):
    def reverse(x:int):
        try:
            return int(str(x)[::-1])
        except ValueError:
            if str(x).startswith("-"):
                return int("-" + str(x)[1:][::-1])
            else:
                raise

    d = {x: dict() for x in dict.fromkeys(C)}
    for a, c in [(i * j, j) for i in C for j in C]:
        b = reverse(a)
        try:
            x = (a - b) / c
            y = b / c
            z = x + y
        except ZeroDivisionError:
            continue
        if x * y != 0 and a - b != 0 and b * x != 0:
            d[c].update({(a, b): (x, y, z)})
    return d

s = [x for x in range(0, 0xff)]

for i in sorted(foo(s).items())[:20]:
    print(len(i[1]), i)