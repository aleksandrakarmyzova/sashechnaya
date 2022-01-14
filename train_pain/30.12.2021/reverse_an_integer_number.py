number = int(input())
# 7509
# 9057
result = 0
while number > 0:
    a = number % 10
    number = number // 10
    result = result * 10 + a
print(result)