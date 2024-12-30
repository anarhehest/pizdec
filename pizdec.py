def foo(C:list):
    def reverse(x:int):
        try:
            return int(str(x)[::-1])
        except ValueError:
            if str(x).startswith("-"):
                return int("-" + str(x)[1:][::-1])
            else:
                raise

    d = dict()
    for a, c in [(i * j, j) for i in C for j in C]:
        if not c in d.keys():
            d.update({c: list()})
        b = reverse(a)
        try:
            x = (a - b) / c
            y = b / c
        except ZeroDivisionError:
            continue
        if x * y != 0 and a - b != 0 and b * x != 0:
            d[c].append((a, x, b, y))
    return d

#n = lambda x: (x, -x)
#s = list(sum(map(n, [x for x in range(0, 0xff)]), ()))

s = [x for x in range(0, 0xff)]
r = foo(s)

for i in sorted(r.items())[:20]:
    print(len(i[1]), i)