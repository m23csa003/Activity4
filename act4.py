def func1(a, b):
    print(f"a: {a}, b: {b}")
    return a + b, a, b


def func2(a, b):
    c = func1(a, b)
    print(f"c: {c}")
    d = c + a
    return a - b, a, b, c, d


if __name__ == "__main__":
    print(func2(1, 2))
