base = 2
exponent = 5


def exponent_function(bas, exp):
    result = 1
    for i in range(1, exp + 1):
        result = result * bas
    return result


print(exponent_function(base, exponent))
