def square_root(x):
    return x ** 0.5


def solve(a, b, c):
    a = float(a)    # można założyć poprawny typ
    b = float(b)
    c = float(c)

    if a == b == c == 0:
        raise ValueError("All coefficients can't be zero")  # czemu?
    if type(a) != float or type(b) != float or type(c) != float:
        raise ValueError('Coefficients should be float')
    if a == 0 and b != 0:
        return -c / b
    if a == b == 0 and c != 0:
        raise ValueError("The equation is not a quadratic equation") # to we wcześniejszym if'ie też nie

    result = () # ta wartość nie jest używana
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return ()
    x1 = (-b - square_root(delta)) / 2 * a  # kolejność wykonywania działań
    x2 = (-b + square_root(delta)) / 2 * a
    x0 = -b / 2 * a
    if delta > 0:
        result = (x1, x2)
    elif delta == 0:
        result = x0

    return result
    # raz liczba, raz krotka
