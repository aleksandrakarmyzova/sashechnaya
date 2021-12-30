for number in range(1, 55):
    for i in range(2, number):
        if not number % i:
            break
    else:
        print(number)
