R = lambda x: x.real
I = lambda x: x.imag

def f(x):
    l = lambda x: str(x)[1:][::-1] if str(x).startswith("-") else str(x)[::-1]
    if isinstance(x, complex):
        return f(x.imag) + f(x.real) * 1j
    if isinstance(x, float):
        if int(x) == x:
            return f(int(x))
        return float(l(x))
    return int(l(x))


def foo(x):
    th = f(x) + x * (1 - 1j)
    r = R(th + I(th) * (1 - 1j))
    return r, th

for A in [
    foo(a)
    for a in
    [.0987654321, .987654321, 1234567890]]:
    print(A)