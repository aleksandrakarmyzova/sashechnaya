number1 = int(input())
number2 = int(input())


def sum_or_mult(n1, n2):
    if (n1 * n2) < 1000:
        print(n1 + n2)
    else:
        print(n1 * n2)


sum_or_mult(number1, number2)