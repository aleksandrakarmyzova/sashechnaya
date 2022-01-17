previous = 0
for number in range(10):
    current = number
    sum = current + previous
    print(current, previous, sum)
    previous = current