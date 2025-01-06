u = 1234567890
f = -23443.999999999998
o = .987

sum = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

def p(x, i=0):
    c = (x - x // 1)
    if round(c, 6) == .0:
        return i
    return p(x * 10, i + 1)


def R(x):
    def r(x, o, i=0):
        if x < 1:
            return i - 1
        print(x)

        y = r(o[0](x, 10), o, o[1](i, 1))
        z = x % 10 // 1 * 10 ** -i
        return y + z

    m = 1
    if x < 0:
        m *= -1
        x *= -1


    o = (mul, sub) if x / 2 * 2 != x // 1 else (div, sum)
    y = r(x, o)


    return m * (y - y // 1) * 10 ** (y // 1)

print(R(u))
