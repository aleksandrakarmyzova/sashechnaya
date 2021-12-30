number = int(input())
i = 0
while number > 0:
    number = int(number / 10)
    i = i + 1
print(i)