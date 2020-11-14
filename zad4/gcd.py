def gcd(a: int, b: int):
    if a == 0:
        return b
    return gcd(b % a, a)


def calculate():
    print('Input the value of a and b:')
    isNumber = False
    while not isNumber:
        try:
            a, b = input().split()
            a, b = int(a), int(b)
            isNumber = True

        except ValueError:
            print("Incorrect value!")
            print("Try again:")

    return gcd(a, b)


print(calculate())
