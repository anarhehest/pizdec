def f(number):
    l = lambda x: "-" + str(x)[1:][::-1] if str(x).startswith("-") else str(x)[::-1]
    if isinstance(number, complex):
        return number.imag + number.real * 1j
        #cr, ci = tuple(map(float, map(f, [number.imag, number.real])))
        #return cr + ci * 1j
    if isinstance(number, float):
        return float(l(number))
    return int(l(number))


def m(a, c):
    b = f(a) + a * 1j
    return (a - b) / c, (a + b) / c


from math import fabs, sqrt, tan

def bar(a, c):

    b = f(a)
    if not isinstance(a, complex):
        b += a * 1j

    print(f">", b)

    x1, x2 = m(a, c)

    y1 = x1 * c / (a - b)

    #z1 = x1.real * -1 - x1.imag
    #z1 = (x1 + x1.imag - x1.imag * 1j)
    #z1arg = tan(x1.imag / x1.real) ** -1
    #z1mod = fabs(sqrt(x1.real ** 2 + x1.imag ** 2))
    #z1 = z1mod # * e ** (1j * z1arg)
    z1 = (x1.real + x1.imag) / 2
    y2 = x2 * c / (a + b)
    #z2 = x2.real * -1 + x2.imag
    #z2 = (x2 + x2.imag - x2.imag * 1j)
    #z2arg = tan(x2.imag / x2.real) ** -1
    #z2mod = fabs(sqrt(x2.real ** 2 + x2.imag ** 2))
    #z2 = z2mod # * e ** (1j * z2arg)
    z2 = (x2.real + x2.imag) / 2
    r1 = (x1, z1)
    r2 = (x2, z2)

    print("-", *r1)
    print("+", *r2)
    print()


from math import e, pi
y = 3
for x in [30]:
    print("-" * 2 * 0x10)
    print("direct\n*", (x, y))
    bar(x, y)
    print("reversed\n.", (f(x), y))
    bar(f(x), y)

